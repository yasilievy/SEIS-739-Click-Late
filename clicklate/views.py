from .models import TranslateHistory
from .serializers import TranslatedHistorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from googletrans import Translator, LANGUAGES
from django.core.files.storage import FileSystemStorage
from PIL import Image
import pytesseract
# import detectlanguage
# from . import detectlanguage_config

# detectlanguage.configuration.api_key = "6dd8715b0219b1a87976ddfced65fe59"
translator = Translator()
pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'

def home(request):
    return render(request, 'home.html')

def home_user(request):
    if request.user.is_authenticated:
        return render(request, 'home-user.html',{'user':request.user})
    return redirect('home')

def translate_text(request):
    """Handle translation of a word or phrase."""
    if request.method == 'POST':
        translation_boolean = True

        text_to_translate = request.POST.get('text')

        target_language = request.POST.get('target_language')

        language_detect = request.POST.get('detect_language')

        if len(target_language) == 0:
            target_language = 'en'
        
        try:
            if len(language_detect) == 0:
                translation = translator.translate(text_to_translate, dest=target_language)
                data = {
                        'user_id': request.user.id,
                        'text_boolean': True,
                        'text_to_translate': text_to_translate,
                        'detected_language': LANGUAGES[translation.src],
                        'translated_results': translation.text
                    }
            else:
                if len(language_detect) == 3:
                    language_detect = language_detect[:-1]
                translation = translator.translate(text_to_translate, dest=target_language, src=language_detect)
                data = {
                        'user_id': request.user.id,
                        'text_boolean': True,
                        'text_to_translate': text_to_translate,
                        'detected_language': LANGUAGES[language_detect],
                        'translated_results': translation.text
                    }
            serializer = TranslatedHistorySerializer(data=data)
        except:
            translation_boolean = False

        if translation_boolean and serializer.is_valid():
            print('serializer was valid')
            serializer.save()
            return render(request, 'translator/translate_text.html',
                          {'original_text': text_to_translate,
                           'translated_text': translation.text,
                           'language_detected': LANGUAGES[translation.src],
                           'target_language':target_language})
        else:
            print('serializer was not valid')
            return render(request, 'translator/translate_text.html',
                {'original_text':text_to_translate,
                 'target_language':target_language,
                 'error_message':'an error occurred, please check the translation settings'})
    return render(request, 'translator/translate_text.html')


def translate_image(request):
    """Handle translation of text in an uploaded image."""
    if request.method == 'POST' and request.FILES.get('image'):
        translation_boolean = True
        image_file = request.FILES['image']
        
        language_detect = request.POST.get('detect_language')

        # Save the image temporarily
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        uploaded_image_path = fs.url(filename)
        
        # Open the image using PIL
        image_path = fs.location + '/' + filename
        img = Image.open(image_path)

        try:
            # Use Tesseract to extract text from the image
            extracted_text = pytesseract.image_to_string(img, lang=language_detect).replace(' ','')
            
            # Translate the extracted text
            translation = translator.translate(extracted_text, dest='en')

            target_language = request.POST.get('target_language')
            if len(target_language) ==0 :
                target_language = 'en'

            translation = translator.translate(extracted_text, dest=target_language,src=language_detect[:-1])
        except:
            translation_boolean = False

        data = {
            'user_id': request.user.id,
            'image_boolean': True,
            'image_to_translate': uploaded_image_path,
            'text_to_translate': extracted_text,
            'detected_language': LANGUAGES[translation.src],
            'translated_results': translation.text
        }
        serializer = TranslatedHistorySerializer(data=data)
        if translation_boolean and len(language_detect) > 0 and serializer.is_valid():
            print('serializer was valid')
            serializer.save()
            return render(request, 'translator/translate_image.html',
                          {'image_to_translate': uploaded_image_path,
                           'original_text': extracted_text,
                           'language_detect': language_detect,
                           'target_language':target_language,
                           'translated_text': translation.text})
        else:
            print('serializer was not valid')
            return render(request, 'translator/translate_image.html',
                          {'language_detected': language_detect,
                           'target_language':target_language,
                           'error_message':'an error occurred, please check the translation settings'})
    return render(request, 'translator/translate_image.html')

def translate_history(request):
    history = TranslateHistory.objects.filter(user_id=request.user.id)
    return render(request, 'translator/translate_history.html',{'translated_history': history})
    # return render(request, 'translator/translate_history.html',{'translated_history': serializer.data})

def translate_image_history(request):
    history = TranslateHistory.objects.filter(user_id=request.user.id)
    return render(request, 'translator/translate_image_history.html',{'translated_history': history})

@api_view(['POST','DELETE'])
def translate_handle(request, id, format=None):
    try:
        translate_event = TranslateHistory.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        translate_event.delete()
        return Response(status.HTTP_200_OK)
