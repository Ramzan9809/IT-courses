from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'категория'


class Course(models.Model):
    LANGUAGE = (
        ('Русский', 'Русский'),
        ('Кыргызский', 'Кыргызский'),
        ('Английский', 'Английский'),
    )
    CERTIFICATION = (
        ('Да', 'Да'),
        ('Нет', 'Нет'),
    )
    RATING_CHOICES = (
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    )
    title = models.CharField(max_length=200, verbose_name='Название курса')
    banner = models.ImageField(upload_to='media/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Цена')
    instructor = models.ForeignKey('Instructors', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES, default=5, verbose_name='Рейтинг')
    desc = RichTextField(verbose_name='Описание')
    language = models.CharField(max_length=10, choices=LANGUAGE, verbose_name='Язык обучения')
    certification = models.CharField(max_length=3, choices=CERTIFICATION, verbose_name='Наличие серфитиката', default='Да')
    count_lessons = models.IntegerField(
        verbose_name='Количество уроков', blank=True, null=True
    )
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'Курсы'

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"slug": self.slug})


class Instructors(models.Model): 
    name = models.CharField(max_length=200, verbose_name='Фамилие Имя')
    photo = models.ImageField(upload_to='instructors/', verbose_name='Фото') 
    position = models.CharField(
        verbose_name='Должность', max_length=100, 
        help_text="Например: Фронтенд мидл разработчик, Экономист"
    )
    desc = models.TextField(verbose_name='Обо мне')   
    count_courses = models.IntegerField(
       verbose_name='Количество курсов с Ментором', blank=True, null=True
    )
    count_students = models.IntegerField(
        verbose_name='Количество выпускников Ментора', blank=True, null=True
    )
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
         return f"{self.name} | {self.position}"
    
    class Meta:
        verbose_name = 'инструктор'
        verbose_name_plural = 'Инструкторы'

    def get_absolute_url(self):
        return reverse("instructor_detail", kwargs={"slug": self.slug})
