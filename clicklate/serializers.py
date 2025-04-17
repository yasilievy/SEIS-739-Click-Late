from rest_framework import serializers
from .models import Translated, TranslateHistory

# need to add database table here too

class TranslatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translated
        fields = ['id']#,'text_boolean','image_boolean','date_translated','detected_language','translate_to_language']

class TranslatedHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslateHistory
        fields = ['id','username','email','text_boolean','image_boolean','detected_language'] #,'translate_to_language']