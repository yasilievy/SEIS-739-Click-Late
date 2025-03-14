from django.http import JsonResponse
from .models import Translated
from .serializers import TranslatedSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.forms import UserCreationForm
# read
@api_view(['GET','POST'])
def click_translate(request, format=None):
    pass
    # if request.method == 'GET':

    #     clicks = Clicklate.objects.all()
    #     serializer = ClicklateSerializer(clicks, many=True)
    #     return JsonResponse({'click_translate':serializer.data}, safe=False)
    # if request.method == 'POST':
    #     serializer = ClicklateSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    # if request.method =='GET':

@api_view(['GET','PUT','DELETE'])
def click_translate_get_one(request, id, format=None):
    pass
    # try:
    #     clicklate_one = Clicklate.objects.get(pk=id)
    # except Clicklate.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
    # if request.method == 'GET':
    #     serializer = ClicklateSerializer(clicklate_one)
    #     return Response(serializer.data)
    # elif request.method == 'PUT':
    #     serializer = ClicklateSerializer(clicklate_one, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(seralizer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'DELETE':
    #     clicklate_one.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
