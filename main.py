import requests
from pprint import pprint
from urllib.parse import urlparse

def shorten_link(headers, url):
    data = {"long_url": url}
    short_link_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(short_link_url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["link"]


def get_cliks(headers, url):
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
    print("\n1.Сократить ссылку")
    print("2.Узнать количество кликов по сокращенной ссылке")
    print("3.Выход из программы\n")
    user_selection = int(input("Выберите функцию:"))
    print()
    if user_selection == 1:
        url = input("Напишите вашу ссылку: ")
        print("Ваша ссылка:", shorten_link(headers, url))
    if user_selection == 2:
        url = input("Напишите вашу сокращенную ссылку:")
        splited_url = urlparse(url)
        url_without_sheme = f"{splited_url.netloc}{splited_url.path}"
        print("Столько кликов:", get_cliks(headers, url_without_sheme))
    if user_selection == 3:
        exit()
