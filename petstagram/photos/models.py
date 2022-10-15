# photos/models.py
from django.core.validators import MinLengthValidator
from django.db import models

# create your models here.
from petstagram.core.model_mixins import StrFromFieldsMixin
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_less_than_5mb


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('pk','photo', 'location')
    min_description_length = 10
    max_description_length = 300
    max_location_length = 30
    photo = models.ImageField(
        upload_to='mediafiles/pet_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb,),
    )
    description = models.CharField(
        # db validation
        max_length=max_description_length,
        validators=(
            # django/python validation
            MinLengthValidator(min_description_length),
        ),
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=max_location_length,
        null=True,
        blank=True,
    )
    publication_date = models.DateField(
        # automatically sets current date on `save` (update or create)
        auto_now=True,
        blank=True,
        null=False,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    # def __str__(self):
    #     return f'{self.id}'
