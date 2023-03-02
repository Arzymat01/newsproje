from django.db import models


# Create your models here.


class Contact_us(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.TextField()
    phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.full_name
