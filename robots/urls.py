from django.urls import path
from .views import robots, upload_exel, exel_file

urlpatterns = [
    # Прописываем url-адрес для первого задания
    # Тестовый POST-запрос с информацией в формате JSON будет отправлен в файле test.py
    path('robots/', robots, name='robots'),
    # Прописываем url-адреса для второго задания
    # Url-адрес для отображения ссылки для скачивания exel-файла
    path('exel_file/', exel_file, name='exel_file'),
    # Url-адрес скачивания самого exel-файла
    path('exel_file/upload_exel/', upload_exel, name='upload_exel')
]