from django.db import models
from django.utils.translation import gettext_lazy as _

from mysite.models.abstract import TimeStampMixin


class Cat(TimeStampMixin):
    class CatGender(models.TextChoices):
        MALE = 'male', _('boy')
        FEMALE = 'female', _('girl')
    name = models.CharField(max_length=256, blank=True)
    gender = models.CharField(max_length=64,
                              choices=CatGender.choices,
                              default=CatGender.MALE
                              )

    class Meta:
        db_table = 'cat'
