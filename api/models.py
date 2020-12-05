from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'


class User(AbstractUser):
    username = models.CharField(
        'Имя пользователя',
        max_length=50,
        blank=True,
        null=True,
        unique=True
    )
    email = models.EmailField('Электронная почта', unique=True)
    bio = models.TextField('О себе', max_length=500, blank=True, null=True)
    role = models.CharField(
        'Группа доступа',
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.USER
    )


class Category(models.Model):
    name = models.CharField('Название категории', max_length=210)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=210)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Название произведения', max_length=210)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField('Краткое описание', blank=True, null=True)
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        blank=True,
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        to_field='slug',
        related_name='category',
        verbose_name='Категория'
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField('Отзыв',)
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )
    score = models.IntegerField(
        'Рейтинг',
        validators=[
            MinValueValidator(1, message='Score can be from 1 to 10.'),
            MaxValueValidator(10, message='Score can be from 1 to 10.')
        ]
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField('Комментарий',)
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.text
