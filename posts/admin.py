from django.contrib import admin
from django.test import Client
from django.core.cache import cache

from posts.models import Post
from posts import views

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'user', 'title', 'created')
    search_fields = ('title', 'user__username', 'user__email')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Si es un post nuevo, debemos cargar la caché de la página principal
        if not change:
            res = cache.keys('*main*')
            if res:
                delete_cache = cache.delete_many(res)
            c = Client()
            response = c.get('/', SERVER_NAME='127.0.0.1:8000')

