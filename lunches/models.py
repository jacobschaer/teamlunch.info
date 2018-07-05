from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Lunch(models.Model):
    team = models.ForeignKey('teams.Team', related_name='lunches', on_delete=models.CASCADE)
    date = models.DateTimeField()
    name = models.CharField(max_length=255)
    phone = PhoneNumberField(blank=True)
    yelp_id = models.CharField(max_length=255, blank=True)
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
        blank=True
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=1024,
    )

    country = models.CharField(
        "Country",
        max_length=3,
    )