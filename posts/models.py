# Django
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Model
class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    post = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    url = models.SlugField(max_length=255, unique=True)


    class Meta:
        ordering = ('-id',)


    def __str__(self):
        return f'{self.title} by {self.user.username}'


    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)