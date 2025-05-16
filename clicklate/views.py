from .models import TranslateHistory
from .serializers import TranslatedHistorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from googletrans import Translator, LANGUAGES
from django.core.files.storage import FileSystemStorage
from PIL import Image
import pytesseract

# initializing translator
translator = Translator()
# initializing tesseract
pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'
# initializing language acronym and language dictionary for dropdown options
concat_tess_languages = [f'{key} || {value}' for key,value in settings.PYTESS_LANGUAGE.items()]
concat_gt_languages = [f'{key} || {value}' for key,value in LANGUAGES.items()]
concat_gt_languages.insert(0,' || ')

# home screen (click login to go to login view)
def home(request):
    return render(request, 'home.html')

# home screen for logged on user
def home_user(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'home-user.html',{'user':request.user})

# translate text view
def translate_text(request):
    if not request.user.is_authenticated:
        return redirect('home')
    """Handle translation of a word or phrase."""
    if request.method == 'POST':
         # retrieves the text to translate
        text_to_translate = request.POST.get('text')

        # cache to retain previously selected language_detect
        previous_language_to_detect = request.POST.get('language_dropdown')

        # parsing (language/acronym) the selected language_detect from dropdown option. becomes a bit more technical when there is an option for none
        # checks whether the langauge_detect returns a one specific list size
        language_init_detect = previous_language_to_detect.split(' || ')
        if len(language_init_detect)==1:
            language_detect_acr = ''
            language_detect = ''
        else:
            language_detect_acr, language_detect = language_init_detect

        # cache to retain previously selected target_language
        previous_target_language = request.POST.get('target_language')
        
        # parsing (language/acronym) the selected target_language from dropdown option
        target_language_acr, target_language = previous_target_language.split(' || ')

       # translation success boolean
        translation_boolean = True

        # tries to translate based on the settings. error can occur if an obvious incorrect language to detect is paired with a text to translate
        # if unsuccessful, translation_boolean is false, else, translation boolean remains true
        try:
            if len(language_detect_acr) == 0:
                translation = translator.translate(text_to_translate, dest=target_language_acr)
                # if no language to detect was selected, translator will automatically detect it. as a result,
                # pulling language to detect from the translator object for serializer
                language_detect = LANGUAGES[translation.src]   
            else:
                translation = translator.translate(text_to_translate, dest=target_language_acr, src=language_detect_acr)
            data = {
                    'user_id': request.user.id,
                    'text_boolean': True,
                    'text_to_translate': text_to_translate,
                    'detected_language': language_detect,
                    'target_language': target_language,
                    'translated_results': translation.text
                }
            serializer = TranslatedHistorySerializer(data=data)
        except Exception as e:
            print(e)
            translation_boolean = False

        if translation_boolean and serializer.is_valid():
            print('serializer was valid')
            serializer.save()
            return render(request, 'translator/translate_text.html',
                            {'original_text': text_to_translate,
                            'translated_text': translation.text,
                            'detected_language': language_detect,
                            'target_language':target_language,
                            'tess_languages':concat_tess_languages,
                            'gt_languages':concat_gt_languages,
                            'previous_target_lang':previous_target_language,
                            'previous_detect_lang':previous_language_to_detect})
        else:
            print('serializer was not valid')
            return render(request, 'translator/translate_text.html',
                {'original_text':text_to_translate,
                 'target_language':target_language,
                 'error_message':'an error occurred, please check the translation settings',
                 'tess_languages':concat_tess_languages,
                 'gt_languages':concat_gt_languages,
                 'previous_target_lang':previous_target_language,
                 'previous_detect_lang':previous_language_to_detect})
    return render(request,  'translator/translate_text.html',{
                            'tess_languages':concat_tess_languages,
                            'gt_languages':concat_gt_languages})

# translate image view
def translate_image(request):
    if not request.user.is_authenticated:
        return redirect('home')
    """Handle translation of text in an uploaded image."""
    if request.method == 'POST' and request.FILES.get('image'):
        # retrieves uploaded image that was part of POST
        image_file = request.FILES['image']
        
        # cache to retain previously selected language_detect
        previous_language_to_detect =request.POST.get('language_dropdown') 

        # parsing (language/acronym) the selected language_detect from dropdown option
        language_detect_acr, language_detect = previous_language_to_detect.split(' || ')

        # cache to retain previously selected target_language
        previous_target_language = request.POST.get('target_language')
        
        # parsing (language/acronym) the selected target_language from dropdown option
        target_language_acr, target_language = previous_target_language.split(' || ')

        # Save the image temporarily
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        uploaded_image_path = fs.url(filename)
        
        # Open the image using PIL
        image_path = fs.location + '/' + filename
        img = Image.open(image_path)

        # translation success boolean
        translation_boolean = True

        # tries to translate based on the settings. error can occur if an obvious incorrect language to detect is paired with a text to translate
        # if unsuccessful, translation_boolean is false, else, translation boolean remains true
        try:
            # use tesseract to extract text from the image
            if language_detect_acr == 'eng':
                # one edge case scenario where it is not good to remove spaces
                extracted_text = pytesseract.image_to_string(img, lang=language_detect_acr)
            else:
                extracted_text = pytesseract.image_to_string(img, lang=language_detect_acr).replace(' ','')
            
            # translate the extracted text
            translation = translator.translate(extracted_text, dest=target_language_acr)
        except:
            translation_boolean = False

        data = {
            'user_id': request.user.id,
            'image_boolean': True,
            'image_to_translate': uploaded_image_path,
            'text_to_translate': extracted_text,
            'detected_language': language_detect,
            'target_language': target_language,
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
                           'detected_language':language_detect,
                           'target_language':target_language,
                           'translated_text': translation.text,
                           'tess_languages':concat_tess_languages,
                           'gt_languages':concat_gt_languages,
                            'previous_target_lang':previous_target_language,
                            'previous_detect_lang':previous_language_to_detect})
        else:
            print('serializer was not valid')
            return render(request, 'translator/translate_image.html',
                          {'language_detected': language_detect,
                           'target_language':target_language,
                           'tess_languages':concat_tess_languages,
                           'gt_languages':concat_gt_languages,
                           'error_message':'an error occurred, please check the translation settings',
                            'previous_target_lang':previous_target_language,
                            'previous_detect_lang':previous_language_to_detect})
    return render(request, 'translator/translate_image.html',
                  {'tess_languages':concat_tess_languages,
                   'gt_languages':concat_gt_languages})

# translate text history view
def translate_text_history(request):
    if not request.user.is_authenticated:
        return redirect('home')
    history = TranslateHistory.objects.filter(user_id=request.user.id)
    return render(request, 'translator/translate_text_history.html',{'translated_history': history})

# translate image history view
def translate_image_history(request):
    if not request.user.is_authenticated:
        return redirect('home')
    history = TranslateHistory.objects.filter(user_id=request.user.id)
    return render(request, 'translator/translate_image_history.html',{'translated_history': history})

# created backend API, but has not direct use at the moment
@api_view(['POST','DELETE'])
def translate_handle(request, id, format=None):
    try:
        translate_event = TranslateHistory.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        translate_event.delete()
        return Response(status.HTTP_200_OK)
