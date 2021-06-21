import requests
import pyperclip
from colorama import init,Fore


init()
def imgur():

    url = "https://api.imgur.com/3/upload.json"
    client_id = "-- CLİENT İD --"
    headers = {'Authorization': 'Client-ID ' + client_id}

    while True:
        print(Fore.RED+"\n[-] Resmin yolunu girin > ",end=""+Fore.RESET)
        user_path = input()
        try:
            respone = requests.post(url=url,headers=headers,files={
                "image":open(user_path,"rb") })
            pyperclip.copy("[img]" + respone.json()["data"]["link"] + "[/img]")
            print(f"\n[img]{respone.json()['data']['link']}[/img]")
            print(Fore.CYAN + "\nUrl Kopyalandı..")

        except FileNotFoundError:
            print(Fore.BLUE+"\nHata! Tekrar Deneyiniz...")



if __name__ == "__main__":
    imgur()

