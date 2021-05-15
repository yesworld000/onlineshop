from django.core.validators import FileExtensionValidator
from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

from auth_.models import MainUser


class Category(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='category images', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'img': self.img,
        }


class Photo(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='photo images', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    price = models.FloatField(default=42500)
    description = models.TextField(default='')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, null=True, related_name="photos")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="photos")

    def __str__(self):
        return f'Photo id={self.id}, name={self.name}'


class Comment(models.Model):
    username = models.CharField(max_length=300)
    text = models.TextField(default='')
    date = models.DateTimeField(default=timezone.now)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True, related_name="comments")

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'text': self.text
            ,
            'date': self.date
        }
