from django.db import models
from django.utils import timezone
from datetime import datetime
# models are the database table defined as classes. if added a class here, include in the admin.py and serializers.py
class Translated(models.Model):
    id = models.IntegerField(primary_key=True)
    # text_boolean = models.BooleanField()
    # image_boolean = models.BooleanField()
    # date_translated = models.DateField()
    # detected_language = models.CharField(max_length=40)
    # translate_to_language = models.CharField(max_length=40)

class TranslateHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=40)

    date = models.DateTimeField(default=datetime.now())
    email = models.CharField(max_length=40)
    text_boolean = models.BooleanField(default=False)
    image_boolean = models.BooleanField(default=False)
    image_to_translate = models.ImageField(default=None)
    text_to_translate = models.CharField(max_length=400)
    detected_language = models.CharField(max_length=30)
    translated_results = models.CharField(max_length=400)
    

