from django.contrib import admin

# Register your models here.
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'user', 'title', 'created')
    search_fields = ('title', 'user__username', 'user__email')