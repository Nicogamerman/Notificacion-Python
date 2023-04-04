# coding=utf-8
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Env Variables
date_url = "https://www.exteriores.gob.es/Consulados/cordoba/es/Comunicacion/Noticias/Paginas/Articulos/Instrucciones-para-solicitar-cita-previa-para-LMD.aspx"
token = "EAAK6axYSFUYBAOQbRdhMVZBjZBXXbttHgKTrCkR8mTTPgWZAJFGRDrZBJnyEaZAMPVmrQ6a913f5Mq9hrxvk83v1ygeOHMoFHwfq48PFzG2YCEWgHUQMe4hPUTctXr8Lbrh8FIYW4IqIZArP7Cw5uYBR4YH6chd94JDsDlgscsM8fNwcfNF8yfd7odTtYWe9iEG6oVwJjKOHzKCZCctxvWpWDfOYgkXKuQZD"
PATH = "chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(PATH, chrome_options=options)


def send_whatsapp(message, num_tel, url):
    myobj = {
        "messaging_product": "whatsapp",
        "to": num_tel,
        "type": "template",
        "template": {
            "name": message,
            "language": {
                "code": "en_US"
            }
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }

    x = requests.post(url, json=myobj, headers=headers)
    print(x.content)
    return None


def date_available(i):
    driver.get(date_url)
    link = driver.find_element_by_partial_link_text("AQU")
    link.click()

    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Historial y cancelaciones"))
        )

        time.sleep(1)
        text = driver.find_element("id", "idDivBktServicesContainer").text

        if text:
            if "No hay horas disponibles" in driver.find_element("id", "idDivBktServicesContainer").text:
                print("No hay horarios")

            else:
                send_whatsapp("hello_world", "543512709882","https://graph.facebook.com/v16.0/105614359164039/messages")
                print("por fín hay horarios 🤘️")

    except:
        print("la pagina no carga 💥️")


# i = 1
# while 1 != 2:
#     if i % 30 == 0:
#         i = 1
#     print("execution number " + str(i))
#     date_available(i)
#     i += 1