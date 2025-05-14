from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'категория',
            },
        ),
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Фамилие Имя')),
                ('photo', models.ImageField(upload_to='instructors/', verbose_name='Фото')),
                ('position', models.CharField(help_text='Например: Фронтенд мидл разработчик, Экономист', max_length=100, verbose_name='Должность')),
                ('desc', models.TextField(verbose_name='Обо мне')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'инструктор',
                'verbose_name_plural': 'Инструкторы',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название курса')),
                ('banner', models.ImageField(upload_to='media/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('rating', models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=5, verbose_name='Рейтинг')),
                ('desc', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('language', models.CharField(choices=[('Русский', 'Русский'), ('Кыргызский', 'Кыргызский'), ('Английский', 'Английский')], max_length=10, verbose_name='Язык обучения')),
                ('certification', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Да', max_length=3, verbose_name='Наличие серфитиката')),
                ('count_lessons', models.CharField(help_text='Например: 24 урока за 1 месяц', max_length=100, verbose_name='Количество уроков')),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=models.CASCADE, to='courses.Category')),
                ('instructor', models.ForeignKey(on_delete=models.CASCADE, to='courses.Instructors')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
