from django.db import models
from apps.courses.models import Category

class Settings(models.Model):
    logo = models.ImageField(upload_to='media/', verbose_name='лого')
    name = models.CharField(verbose_name='название сайта', max_length=20)
    address = models.CharField(verbose_name='адресс', max_length=200)
    phone = models.CharField(verbose_name='номер', max_length=17, help_text='+996 554 97 70 13')
    email = models.EmailField(verbose_name='emaill', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Данные'
        verbose_name = 'данные'

class Slider(models.Model):
    main_title = models.CharField(max_length=200, verbose_name='Главный заголовок')
    on_title = models.CharField(max_length=100, verbose_name='Над заголовок')
    under_title = models.CharField(max_length=50, verbose_name='Под заголовок', null=True, blank=True)
    under_title_2 = models.CharField(max_length=50, verbose_name='Под заголовок 2', null=True, blank=True)
    desc = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.main_title
    
    class Meta:
        verbose_name_plural = 'Слайдеры'
        verbose_name = 'слайдер'

class Faq(models.Model):
    question = models.CharField(max_length=100, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    def __str__(self):
         return self.question
    
    class Meta:
        verbose_name = 'вопрос/ответ'
        verbose_name_plural = 'Вопросы/Ответы'

class Reviews(models.Model):
    RATING_CHOICES = (
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    )
    WHO_CHOICES = (
        ('Студент', 'Студент'),
        ('Ментор', 'Ментор'),
    )
    main_message = models.CharField(max_length=100, verbose_name='Главное сообщение')
    desc = models.TextField(verbose_name='Подробнее')
    rating = models.IntegerField(choices=RATING_CHOICES, default=5, verbose_name='Рейтинг')
    name = models.CharField(max_length=200, verbose_name='Фио')
    who_say = models.CharField(max_length=10, choices=WHO_CHOICES, default='Студент', verbose_name='Кто вы?')
    photo = models.ImageField(upload_to='madia/', verbose_name='Фото', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Направление')

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name