from django.http import JsonResponse, HttpRequest
from .models import TranslateHistory
from .serializers import TranslatedSerializer, TranslatedHistorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from googletrans import Translator
from django.core.files.storage import FileSystemStorage
from PIL import Image
import pytesseract 

# import detectlanguage
# from . import detectlanguage_config

# detectlanguage.configuration.api_key = "6dd8715b0219b1a87976ddfced65fe59"
translator = Translator()

def home(request):
    return render(request, 'home.html')

def home_user(request):
    if request.user.is_authenticated:
        return render(request, 'home-user.html',{'user':request.user})
    return redirect('home')

@api_view(['POST','GET'])
def translate_text(request):
    translation = ''
    """Handle translation of a word or phrase."""
    if request.method == 'POST':
        text_to_translate = request.POST.get('text')
        print(text_to_translate)
        target_language = request.POST.get('target_language', 'en')
        if len(target_language) ==0 :
            target_language = 'en'
        translation = translator.translate(text_to_translate, dest=target_language)
        # print(translation)
        # print(translation.extra_data)

        data = {
            'id': 0,
            'username': request.user.username,
            # 'date': datetime.now(),
            'email': request.user.email,
            'text_boolean': True,
            'text_to_translate': text_to_translate,
            'detected_language': translation.src,
            'translated_results': translation.text
        }
        serializer = TranslatedHistorySerializer(data=data)
        if serializer.is_valid():
            print('serializer was valid')
            
            existing_size = len(TranslateHistory.objects.all())
            serializer.validated_data['id'] = existing_size + 1
            serializer.save()
            return render(request, 'translator/translate_text.html',{'original_text': text_to_translate,
                                                                 'translated_text': translation.text,
                                                                 'language_detected': translation.src,
                                                                 'target_language':target_language})
        else:
            print('serializer was not valid')
    if request.method == 'GET':
        return render(request, 'translator/translate_text.html')
            

        
 
    return render(request, 'translator/translate_text.html')


@api_view(['POST'])
def translate_handle(request):

    if request.method == 'POST':
        print('handled request')

        print(request)
        print(type(request))
        print(request.data)
        serializer = TranslatedHistorySerializer(data=request.data)

        if serializer.is_valid():
            
            existing_size = len(TranslateHistory.objects.all())
            serializer.validated_data['id'] = existing_size + 1
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # if request.method == 'GET':
    #     history = TranslateHistory.objects.get(id=pk)
    #     serializer = TranslatedHistorySerializer(history)
    #     return Response(serializer.data)
    # if request.method == 'DELETE':
    #     pass
    # if request.method == 'PUT':
    #     pass


def translate_image(request):
    """Handle translation of text in an uploaded image."""
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        
        # Save the image temporarily
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        uploaded_image_path = fs.url(filename)
        
        # Open the image using PIL
        image_path = fs.location + '/' + filename
        img = Image.open(image_path)

        # Use Tesseract to extract text from the image
        extracted_text = pytesseract.image_to_string(img)
        
        # Translate the extracted text
        translated_text = translator.translate(extracted_text, dest='en').text

        return JsonResponse({
            'original_text': extracted_text,
            'translated_text': translated_text,
            'image_url': uploaded_image_path
        })

    return render(request, 'translator/translate_image.html')


def translate_history(request):
    username = ''
    if request.user.is_authenticated:
        username= request.user.username
        print(username)
    # history = TranslateHistory.objects.all()
    history = TranslateHistory.objects.filter(username=username)
    serializer = TranslatedHistorySerializer(history, many=True)
    # return JsonResponse(serializer.data, safe=False)
    return render(request, 'translator/translate_history.html',{'translated_history': serializer.data})
