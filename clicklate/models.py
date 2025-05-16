from django.db import models
from datetime import datetime

class TranslateHistory(models.Model):
    user_id = models.IntegerField()
    date = models.DateTimeField(default=datetime.now())
    text_boolean = models.BooleanField(default=False)
    image_boolean = models.BooleanField(default=False)
    image_to_translate = models.CharField(null=True,max_length=400) # uses directory location to display in html template
    text_to_translate = models.CharField(max_length=400)
    detected_language = models.CharField(max_length=30)
    target_language = models.CharField(max_length=30)
    translated_results = models.CharField(max_length=400)
    

