from django.db import models
from datetime import datetime

class TranslateHistory(models.Model):
    user_id = models.IntegerField() # foreign key
    date = models.DateTimeField(default=datetime.now()) # date of the translation event
    text_boolean = models.BooleanField(default=False) # the translated text
    image_boolean = models.BooleanField(default=False) # is this an image translation?
    image_to_translate = models.CharField(null=True,max_length=400) # uses directory location to display in html template
    text_to_translate = models.CharField(max_length=400) # is this a text translation?
    detected_language = models.CharField(max_length=30) # what language was detected
    target_language = models.CharField(max_length=30) # what is the intended language to translate to
    translated_results = models.CharField(max_length=400) # the translated results
    

