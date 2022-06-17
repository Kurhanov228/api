import requests
from pprint import pprint
from urllib.parse import urlparse

def url_short(headers, url):
    data = {"long_url": url}
    short_link_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(short_link_url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["link"]


def url_cliks(headers, url):
    total_clicks_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'
    response = requests.get(total_clicks_url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]

headers = {
    'Authorization': 'Bearer ac8678968bd58d3dddad020cdd2a9c8da75ce925',
    'Content-Type': 'application/json'
}

print("Программа работы со ссылками битли")
while True:
    print()
    print("1.Сократить ссылку")
    print("2.Узнать количество кликов по сокращенной ссылке")
    print("3.Выход из программы")
    print()
    otvet = int(input("Выберите функцию:"))
    print()
    if otvet == 1:
        url = input("Напишите вашу ссылку: ")
        print("Ваша ссылка:", url_short(headers, url))
    if otvet == 2:
        url = input("Напишите вашу сокращенную ссылку:")
        splited_url = urlparse(url)
        url_without_sheme = f"{splited_url.netloc}{splited_url.path}"
        print("Столько кликов:", url_cliks(headers, url_without_sheme))
    if otvet == 3:
        exit()
