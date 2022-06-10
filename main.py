import requests
from  pprint import pprint
headers = {
    'Authorization': 'Bearer ac8678968bd58d3dddad020cdd2a9c8da75ce925',
    'Content-Type': 'application/json'
}

#response = requests.get('https://api-ssl.bitly.com/v4/user', headers=headers)
#token = "ac8678968bd58d3dddad020cdd2a9c8da75ce925"

#pprint(response.json()["emails"][0]["email"])
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
        data = {"long_url": url}

        response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=data)
        response.raise_for_status()
        print("Ваша ссылка!: ", response.json()["link"])
    if otvet == 2:
        print("50")
    if otvet == 3:
        exit()
