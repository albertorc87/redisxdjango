# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='blog'
    ),
    path(
        route='posts/<slug:url>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
]
