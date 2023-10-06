import requests
import urllib3
from bs4 import BeautifulSoup


def checkTickedAcademiaDelCine(url):
    try:
        urllib3.disable_warnings()
        response = requests.get(url, verify=False)
        print(response)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            link_element = soup.find('a', class_='actividad-entradas-enlace')

            return link_element

    except requests.exceptions.RequestException as e:
        print('Se produjo un error al realizar la solicitud:', str(e))
    except Exception as e:
        print('Se produjo un error inesperado:', str(e))


def checkTickedMK2(url):
    try:
        urllib3.disable_warnings()
        response = requests.get(url, verify=False)
        print(response)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            link_element = soup.find('p', class_='gibsonL sinopsis')

            return link_element

    except requests.exceptions.RequestException as e:
        print('Se produjo un error al realizar la solicitud:', str(e))
    except Exception as e:
        print('Se produjo un error inesperado:', str(e))
