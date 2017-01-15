#После изменения модели сделать:
# makemigrations blog
# sqlmigrate blog 0001
# migrate

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES =(
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title  = models.CharField(max_length=250)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ('-publish',)

def __str__(self):
    return self.title


