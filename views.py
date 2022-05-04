""" Модуль, содержащий контроллеры веб-приложения """
from ts_framework.templator import render


class Index:
    def __call__(self):
        return '200 OK', render('index.html')


class About:
    def __call__(self):
        return '200 OK', render('about.html')


class Products:
    def __call__(self):
        return '200 OK', render('products.html')


class Contacts:
    def __call__(self):
        return '200 OK', render('contacts.html')
