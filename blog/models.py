from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250) #CharField = varChar
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')  #SlugField = URL?
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts') #внешний ключ,ссылается на таблицу User, из системы логина пользователей
    body = models.TextField() # текст = TEXT
    publish = models.DateTimeField(default=timezone.now)  # Дата
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')  #varChar домен с ограничениями draft, published(то есть можно выбрать только эти значения)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

# Create your models here.
