from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, null=True)
    date = models.DateField( null=True)
    image = models.ImageField(null=True, upload_to='media/')
    city = models.CharField(max_length=128, null=True)

    def __str__(self):
       return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название Категории')
    def __str__(self):
        return self.name
class AppointMeeting(models.Model):
    title = models.CharField(max_length=128, null=True, verbose_name='Заголовок')
    description = models.TextField(max_length=256, null=True, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
