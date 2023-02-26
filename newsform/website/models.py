import uuid
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


class News(models.Model):
    state_choice = (
        ('FRU', 'Bishkek'),
        ('CH', 'Chuy'),
        ('OSH', 'Osh'),
        ('NN', 'Naryn'),
        ('IK', 'Issyk Kul'),
        ('JA', 'Jalal Abad'),
        ('BN', 'Batken'),
        ('TS', 'Talas'),
    )

    year_choise = [(r, r) for r in range(2000, (datetime.now().year + 1))]
    year_choise = tuple(year_choise)

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    year = models.IntegerField(('year'), choices=year_choise)
    home = RichTextField()
    business = RichTextField()
    sport = RichTextField()
    technology = RichTextField()
    health = RichTextField()
    politika = RichTextField()
    news_photo = models.ImageField(
        upload_to='photos/cars/%Y/%m/%d/', null=True, blank=True)
    sport_photo = models.ImageField(
        upload_to='photos/cars/%Y/%m/%d/', null=True, blank=True)
    bisiness_photo = models.ImageField(
        upload_to='photos/cars/%Y/%m/%d/', null=True, blank=True)
    health_photo = models.ImageField(
        upload_to='photos/cars/%Y/%m/%d/', null=True, blank=True)
    politika_photo = models.ImageField(
        upload_to='photos/cars/%Y/%m/%d/', null=True, blank=True)
    technology_photo = models.ImageField(
        upload_to='photos/cars/%Y/%m/%d/', null=True, blank=True)
    news_title = models.CharField(max_length=255)
    sport_title = models.CharField(max_length=255)
    healh_title = models.CharField(max_length=255)
    business_title = models.CharField(max_length=255)
    technology_title = models.CharField(max_length=255)
    politika_title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
