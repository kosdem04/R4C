from django.shortcuts import render
from django.http import JsonResponse
import json
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from .models import Robot


# Представление для первого задания
# @csrf_exempt — декоратор в Django, который используется для отключения проверки CSRF
@csrf_exempt
def robots(request):
    # Проверяем тип запроса
    if request.method == 'POST':
        try:
            # Загружаем информацию в формате JSON из запроса
            data = json.loads(request.body)
            # Передаём полученную информацию в модель для последующей проверки
            robots = Robot(**data)
            # Проверяем входные данные, в случае ошибки происходит исключение ValidationError
            robots.full_clean()
            # Делаем проверку, есть ли робот с входным серийным номером в базе данных
            for rob in Robot.objects.all():
                if robots.serial == rob.serial:
                    print('Робот с таким серийным номером уже есть в базе данных')
                    return JsonResponse({'message':'Робот с таким серийным номером уже есть в базе данных'})
            # Сохраняем информацию в базе данных
            robots.save()
            return JsonResponse({'message': 'Robot created successfully'}, status=200)
        # Обработка исключения ValidationError
        except ValidationError as error:
            return JsonResponse({'error': str(error)}, status=400)
    # Обработка GET-запроса
    else:
        return JsonResponse({'message':'Нет активных функций для GET-запроса'})
