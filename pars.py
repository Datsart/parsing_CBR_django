import requests
from bs4 import BeautifulSoup

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
    print(numcode, charcode, nominal, name, value)
