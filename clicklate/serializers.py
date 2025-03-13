from rest_framework import serializers
from .models import Clicklate, Translated

# need to add database table here too

class ClicklateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clicklate
        fields = ['id','name','description']

class TranslatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translated
        fields = ['id','user_id','text_boolean','image_boolean','date_translated','detected_language','translate_to_language']
