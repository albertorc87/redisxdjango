# Django
from django.views.generic import DetailView, ListView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Models
from posts.models import Post

@method_decorator(cache_page(60*60, key_prefix='main'), name='dispatch')
class PostsFeedView(ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 999
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'url'
    slug_url_kwarg = 'url'