from django.contrib import admin
from django.urls import path
from .views import orders, send_order_email

urlpatterns = [
    # url-адес для предоствления выбора модели и версии робота, а также для указывания адреса электронной почты, на которую нужно отправить письмо
    path('orders/', orders, name='orders'),
    # url-адес для отправки электронного письма
    path('orders/send_email/', send_order_email, name='send_order_email'),
]
