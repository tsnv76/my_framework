from wsgiref.simple_server import make_server
from ts_framework.main import Framework
from urls import routes

# Создаем объект WSGI-приложения
application = Framework(routes)

with make_server('', 8082, application) as httpd:
    print("Запуск на порту 8082...")
    httpd.serve_forever()
