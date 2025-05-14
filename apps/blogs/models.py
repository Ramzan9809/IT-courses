from django.db import models
from apps.courses.models import Instructors, Category
from django.urls import reverse
from ckeditor.fields import RichTextField


class Blog(models.Model):
    banner = models.ImageField(upload_to='media/', verbose_name='Баннер')
    mini_banner = models.ImageField(upload_to='media/', verbose_name='Баннер поменьше', null=True, blank=True)
    title = models.CharField(max_length=150, verbose_name='Название')
    instructor = models.ForeignKey(Instructors, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    count_comments = models.IntegerField(verbose_name='Кол-во комментраиев')
    desc = RichTextField(verbose_name='Описание')
    quote = RichTextField(verbose_name='Описание')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="ФИО")
    photo = models.ImageField(upload_to='media/', verbose_name='Фото', null=True, blank=True)
    email = models.EmailField(max_length=155, verbose_name='email')
    comment = models.TextField(verbose_name='Ваш комментрий')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} | {self.blog.title}'
    
    class Meta:
        verbose_name = 'коммент'
        verbose_name_plural = 'Комменты'