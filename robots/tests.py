import requests

# Создаём заголовок для запроса
headers = {
    'Content-Type': 'application/json'
}

# Создём информацию в JSON-формате 
body = {
    'serial': '15Q33',
    'model': 'X5',
    'version': 'Q3',
    'created': '2022-12-31 23:59:59'
 }

# Выполняем POST-запрос
response = requests.post("http://127.0.0.1:8000/robots/robots/", headers=headers, json = body)

# Выводим код состояния выполнения запроса
print(response.status_code)

# Извлекаем информацию из JSON-строки 
print(response.json())
