""" Модуль, содержащий контроллеры веб-приложения """
from ts_framework.templator import render


class Index:
    def __call__(self, *args):
        return '200 OK', render('index.html')


class About:
    def __call__(self, *args):
        return '200 OK', render('about.html')


class Otchets:
    def __call__(self, *args):
        return '200 OK', render('otchets.html')


class Contacts:
    def __call__(self, *args):
        return '200 OK', render('contacts.html')
