from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

from apps.courses.models import Category, Course


class Settings(models.Model):
    logo = models.ImageField(upload_to='media/', verbose_name='лого только для index')
    logo_2 = models.ImageField(upload_to='media/', verbose_name='лого для остальног сайта', null=True, blank=True)
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
    desc = RichTextField(verbose_name='Описание')

    def __str__(self):
        return self.main_title
    
    class Meta:
        verbose_name_plural = 'Слайдеры'
        verbose_name = 'слайдер'

class Faq(models.Model):
    question = models.CharField(max_length=100, verbose_name="Вопрос")
    answer = RichTextField(verbose_name='Описание')

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
    desc = RichTextField(verbose_name='Описание')
    course = models.ManyToManyField(Course, null=True, blank=True)
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
    

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {', '.join([c.title for c in self.course.all()])}"


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    

class AboutUs_blog(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    under_title = models.CharField(max_length=30, verbose_name='Под заголовок')
    desc = RichTextField(verbose_name='Описание')
    advantage_first = models.CharField(max_length=100, verbose_name='Наши приемущества/сильные стороны')
    advantage_second = models.CharField(max_length=100, verbose_name='Наши приемущества/сильные стороны', null=True, blank=True)
    advantage_third = models.CharField(max_length=100, verbose_name='Наши приемущества/сильные стороны', null=True, blank=True)
    experience = models.IntegerField(default=5, verbose_name='Количество лет опыта')
    banner_first = models.ImageField(upload_to='home', verbose_name='Баннер')

    def __str__(self):
        return f'{self.title} {self.under_title}'
    
    class Meta:
        verbose_name = 'AboutUs_blog'
        verbose_name_plural = 'AboutUs_blogs'


class AboutUs_card(models.Model):
    icon = models.ImageField(upload_to='home', verbose_name='Иконка')
    name = models.CharField(max_length=30, verbose_name='Заголовок')
    desc = RichTextField(verbose_name='Короткое описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'AboutUs_card'
        verbose_name_plural = 'AboutUs_cards'


class AboutUs_life(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    under_title = models.CharField(max_length=30, verbose_name='Под заголовок')
    desc = RichTextField(verbose_name='Описание')
    advantage_first = models.CharField(max_length=100, verbose_name='Наши приемущества/сильные стороны')
    advantage_second = models.CharField(max_length=100, verbose_name='Наши приемущества/сильные стороны', null=True, blank=True)
    advantage_third = models.CharField(max_length=100, verbose_name='Наши приемущества/сильные стороны', null=True, blank=True)
    banner_first = models.ImageField(upload_to='home', verbose_name='Баннер')

    def __str__(self):
        return f'{self.title} {self.under_title}'
    
    class Meta:
        verbose_name = 'AboutUs_life'
        verbose_name_plural = 'AboutUs_lifes'

class Partner(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    logo = models.ImageField(upload_to='home', verbose_name='logo')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'партнёр'
        verbose_name_plural = 'Партнёры'