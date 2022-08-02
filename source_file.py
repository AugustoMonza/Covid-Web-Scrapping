from tkinter.ttk import Style
from urllib import request
import requests
from bs4 import BeautifulSoup

def scrap():
    url = 'https://ourworldindata.org/covid-deaths'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    download = soup.find_all('a', style = 'display: inline-block; margin-left: 0.5rem;')
    fil = download[1].get('href')
    page = requests.get(fil)
    status = page.status_code

    if status == 200:
        with open('datos Covid.csv', 'wb') as archivo:
                    archivo.write(page.content)
    else:
        print(f'Error de conexión: {status}')

if __name__ == '__main__':
    scrap()
                