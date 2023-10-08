from django.shortcuts import render
from django.core.mail import send_mail
from .forms import OrderForm
from django.conf import settings

# Представление для вывода формы
def orders(request):
    # Проверка типа запроса
    if request.method == 'POST':
        form = OrderForm(request.POST)
        # Передача в контексте формы
        return render(request, 'send_email.html', context={'form': form})
    else:
        form = OrderForm()
        # Передача в контексте формы
        return render(request, 'send_email.html', context={'form': form})

# Представление для отправки электронного письма
def send_order_email(request):
    # Извлечение переданной информации из формы
    model = request.POST.get('dropdown_model')
    version = request.POST.get('versions')
    email = request.POST.get('email')
    # Тема письма
    subject = 'Робот в наличии'
    # Текст сообщения
    message = f'Добрый день!\n Недавно вы интересовались нашим роботом модели {model}, версии {version}.\n Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами'
    # Адрес отпрвителя
    from_email = settings.DEFAULT_FROM_EMAIL
    # Список адресов получателей
    recipient_list = [email,]
    # Функция отправки электронного письма
    send_mail(subject, message, from_email, recipient_list)
    # Отображения страницы с отображением успешной отправки письма
    form = OrderForm()
    return render(request, 'ok.html', context={'form': form})
