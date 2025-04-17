from django.db import models

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
    email = models.CharField(max_length=40)
    text_boolean = models.BooleanField(default=False)
    image_boolean = models.BooleanField(default=False)
    detected_language = models.CharField(max_length=2)

