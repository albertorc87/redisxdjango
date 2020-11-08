from django.contrib import admin

from posts.models import Post
from posts import tasks

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'user', 'title', 'created')
    search_fields = ('title', 'user__username', 'user__email')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Si es un post nuevo, debemos cargar la caché de la página principal
        if not change:
            tasks.reboot_cache_main()

