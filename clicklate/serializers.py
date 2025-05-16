from rest_framework import serializers
from .models import TranslateHistory

class TranslatedHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslateHistory
        fields = ['user_id',
                  'date',
                  'text_boolean',
                  'image_boolean',
                  'image_to_translate',
                  'text_to_translate',
                  'detected_language',
                  'target_language',
                  'translated_results'
                  ]