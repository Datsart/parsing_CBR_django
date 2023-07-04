from django.core.management.base import BaseCommand

# из приложения импортируем модель
from cbr.models import CbrPars

# ctrl C,  ctrl V из pars (файл создавали в начале самом)
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
    help = 'Парсинг ЦБР в модель'

    def handle(self, *args, **options):
        # кидаем запрос на страницу http
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        print(response.status_code)
        # берем ответ от сервера , получаем все видимые данные, и приводим к читаемому формату lxml
        soup = BeautifulSoup(response.content, 'lxml')
        # получаем все данные которые находятся в тегах валют
        all_valute = soup.find_all('valute')
        # print(all_valute)

        for el in all_valute:
            # метод text для получения данных из тегов
            numcode = int(el.find('numcode').text)
            charcode = el.find('charcode').text
            nominal = int(el.find('nominal').text)
            name = el.find('name').text
            value = float(el.find('value').text.replace(',', '.'))


            models_pars = CbrPars(
                numcode=numcode,
                charcode=charcode,
                nominal=nominal,
                name=name,
                value=value,
            )
            models_pars.save()
        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы'))