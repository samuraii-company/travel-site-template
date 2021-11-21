from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Destinations(models.Model):
    images = models.ImageField(verbose_name="Изображение")
    name = models.CharField(max_length=50, verbose_name="Название")
    discription = models.CharField(max_length=100, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Места назначения"


class Blog(models.Model):
    images = models.ImageField(verbose_name="Изображение")
    name = models.CharField(max_length=50, verbose_name="Название Статьи")
    discription = models.CharField(max_length=100, verbose_name="Описание")
    data = models.DateField(verbose_name="Дата публикации", auto_now_add=True)
    author = models.CharField(max_length=20, verbose_name="Автор")
    blog_url = models.URLField(verbose_name="Ссылка на статью", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Статьи блога"


class UserData(models.Model):
    name = models.CharField(max_length=50, verbose_name="ФИО")
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=50, verbose_name="Email")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Заявки от пользователей"


class Subscirbe_Emails(models.Model):
    email = models.EmailField(max_length=50, verbose_name="Email")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Почты для рассылки"
