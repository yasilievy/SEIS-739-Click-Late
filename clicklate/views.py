from django.http import JsonResponse
from .models import Translated
from .serializers import TranslatedSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from googletrans import Translator
from django.core.files.storage import FileSystemStorage
from django.views.generic import FormView, View,TemplateView

def home(request):
    return render(request, 'home.html')

def home_user(request):
    if request.user.is_authenticated:
        return render(request, 'home-user.html',{'user':request.user})
    return redirect('home')
translator = Translator()

class translate_text_view(View):
    original_text = ''
    translated = ''
    def post(self, request):
        self.original_text = request.POST.get('text')
        target_language = request.POST.get('target_language', 'en')
        if len(target_language)==0:
            target_language = 'en'
        print(target_language)
        translation = translator.translate(self.original_text, dest=target_language)
        self.translated = translation.text
        return render(request, 'translator/translate_text.html',{'original_text': self.original_text,'translated_text': self.translated})
    def get(self,request):
        return render(request, 'translator/translate_text.html',{'original_text': self.original_text,'translated_text': self.translated})



def translate_text(request):
    translation = ''
    """Handle translation of a word or phrase."""
    if request.method == 'POST':
        text_to_translate = request.POST.get('text')
        target_language = request.POST.get('target_language', 'en')

        # Translate text
        translation = translator.translate(text_to_translate, dest=target_language)


        return render(request, 'translator/translate_text.html',{'original_text': text_to_translate,'translated_text': translation.text})
        # return JsonResponse({
        #     'original_text': text_to_translate,
        #     'translated_text': translation.text,
        #     'source_language': translation.src,
        #     'target_language': target_language
        # })
    return render(request, 'translator/translate_text.html')


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