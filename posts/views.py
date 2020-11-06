# Django
from django.views.generic import DetailView, ListView

# Models
from posts.models import Post


class PostsFeedView(ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 10
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'url'
    slug_url_kwarg = 'url'