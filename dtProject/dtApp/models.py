from django.db import models

# Create your models here.


class UserProfile(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    image = models.FileField(upload_to='', blank=True, null=True)

    class Meta:
        ordering = ['first_name']
        db_table = 'UserProfiles'