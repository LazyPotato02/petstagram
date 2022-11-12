# pets/models.py
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.utils.text import slugify

from petstagram.core.model_mixins import StrFromFieldsMixin

UserModel = get_user_model()


class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name', 'slug')
    MAX_NAME = 30

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )
    personal_photo = models.URLField(
        null=False,
        blank=False,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)

    # def __str__(self):
    #     return f'Id: {self.id} | Name: {self.name}'
