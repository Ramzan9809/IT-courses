from django.db import models
from django.urls import reverse
from apps.courses.models import Instructors
from ckeditor.fields import RichTextField


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    desc = RichTextField(verbose_name='Описание')
    price = models.CharField(max_length=6, verbose_name='Цена')
    day = models.CharField(max_length=2, verbose_name='День мероприятия')
    month = models.CharField(max_length=10, verbose_name='Месяц мероприятия')
    start_date = models.CharField(max_length=50, verbose_name='Дата начала', help_text='25 мая, 2025')
    time = models.CharField(max_length=50, verbose_name='Время проведения', help_text='12.30 - 02.30')
    count_people = models.IntegerField(default=10, verbose_name='Количество участников')
    location = models.CharField(max_length=100, verbose_name='Адрес')
    instructors = models.ManyToManyField(Instructors, verbose_name='Инструкторы')
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
         return self.title
    
    class Meta:
        verbose_name = 'мероприятие'
        verbose_name_plural = 'Мероприятия'

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"slug": self.slug})
 