from django.db import models

class UserProfile(models.Model):
    # id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=40)
    user_password = models.CharField(max_length=40)