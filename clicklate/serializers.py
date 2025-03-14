from rest_framework import serializers
from .models import Translated

# need to add database table here too

class TranslatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translated
        fields = ['id','text_boolean','image_boolean','date_translated','detected_language','translate_to_language']
