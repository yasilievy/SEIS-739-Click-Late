from django.forms import ModelForm
from .models import TranslateHistory

class TranslateForm(ModelForm):
    class Meta:
        model = TranslateHistory
        fields = ['id',
                  'username',
                  'date',
                  'email',
                  'text_boolean',
                  'image_boolean',
                  'image_to_translate',
                  'text_to_translate',
                  'detected_language',
                  'translated_results']