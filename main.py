"""
sites - массив со всеми ссылками, парсинг которых будет происходить
choose_func - функция, в которой прописывается, если ссылка не парсится обычным методом (функция main),
              сюда можно дописать новую функцию, которая будет парсить нужную ссылку нужным методом
main - главная функция, которая будет искать в коде html страницы нужную маску "tel:", обычно на сайтах есть гиперсылка
       для звонка, именно её и ищет мой код
hands - в данном случае, сайт https://hands.ru не подходит для функции main, её мы парсим нетривиально,
        что и написано в функции
format - приводит все номера к "красивому" формату, а так же выводит сами номера в терминал

(ссылка https://www.askona.ru добавлена для большей демонстративности фукционала кода)
"""

import requests
import re
from bs4 import BeautifulSoup
sites = [
    'https://hands.ru/company/about',
    'https://repetitors.info/',
    'https://www.askona.ru/podushki/',
]


def choose_func(link):
    if link == 'https://hands.ru/company/about':
        return hands(link)

    else:
        return main(link)

def main(link):
    res = requests.get(link)
    num = re.search(r'"tel:(.*?)"',str(res.text))
    format(num[1])

def hands(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')
    num = re.search(r'"callCenterPhone":"(.*?)"', str(res.text))
    format(num[1])

def format(number):
    number = number.replace('(','')
    number = number.replace(')', '')
    number = number.replace('-', '')
    number = number.replace(' ', '')
    if number[0]=='8':
        number = '+7'+number[1:]
    print(number)


for link in sites:
    choose_func(link)

