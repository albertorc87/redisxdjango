# Python
import os
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redisxdjango.settings')

# Django
import django
django.setup()
from django.utils.text import slugify

# Model
from posts.models import Post
from django.contrib.auth.models import User


with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    u = User.objects.get(pk=1)
    for row in csv_reader:
        try:
            obj = Post.objects.get(url=slugify(row[0]))
        except Post.DoesNotExist:
            post = f'{row[1]}. ' * 20
            p = Post(title=row[0], post=post, user=u)
            p.save()