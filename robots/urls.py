from django.urls import path
from .views import robots

urlpatterns = [
    # Прописываем url-адрес для первого задания
    # Тестовый POST-запрос с информацией в формате JSON будет отправлен в файле test.py
    path('robots/', robots, name='robots'),
]