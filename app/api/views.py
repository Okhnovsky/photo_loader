from random import randint
from time import sleep

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from photos.consumers import update_photo

from .tasks import add
from .serializers import PhotoSerializer, PhotoResponseSerializer


class PhotoLoader(APIView):
    """
    Принимает POST запрос с изображением в кодировке base64
    и сохраняет его в БД, возвращает сгенерированное случайное число
    в диапазоне от 1 до 1000.
    """

    @extend_schema(
        request=PhotoSerializer,
        responses=PhotoResponseSerializer,
        operation_id='Загрузка фото',
    )
    def post(self, request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Я тут не совсем понял насчет 20 секунд...
            # Нужно дать ответ через 20 секунд? Тогда можно имитацию
            # c sleep. Конечно, для реального проекта не сгодится, там
            # от контекста нужно исходить.
            sleep(20)
            update_photo()
            # Если имелось ввиду отдать ответ сразу, а саму картинку
            # обрабатывать 20 секунд, то ниже я написал класс, который
            # сохранит картинку асинхронно через 20 секунд, а ответ
            # отдаст сразу
            return Response(
                serializer.instance.random_int, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SecondPhotoLoader(APIView):
    """
    Принимает POST запрос с изображением в кодировке base64
    и сохраняет его в БД, возвращает сгенерированное случайное число
    в диапазоне от 1 до 1000.

    В данном случае, ответ возвращается сразу, а картинка сохранится
    только через 20 секунд. Появится сама на главной странице тоже
    только через 20 секунд.
    """

    @extend_schema(
        request=PhotoSerializer,
        responses=PhotoResponseSerializer,
        operation_id='Загрузка фото',
    )
    def post(self, request):
        number = randint(1, 1000)
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            add.apply_async(args=[serializer.data, number], countdown=20)
            return Response(
                number, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
