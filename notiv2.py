# coding=utf-8
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Env Variables
date_url = "https://www.exteriores.gob.es/Consulados/cordoba/es/Comunicacion/Noticias/Paginas/Articulos/Instrucciones-para-solicitar-cita-previa-para-LMD.aspx"
token = "EAAVTfyhlZCvsBAAgl3FtLVGwZAxpFuIFIZCanb0gtge0W6ywyV6ZCZAD1ZCf3MRgw4ZCmsCz4YDju2lZAh6Rby0Ye6CDv4ZC5dm4i6Hjpc73tLrhyZAHLzCMfKShLlR3VnZAYMA3FWZCUQOI0zZBgkswcAQqwlFBPHJcEb7c8Kt1r6ZCapNiyRD3iu5KyPmcWC7uvyG2aYQ0oPZAJLOJgZDZD"
PATH = "chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(PATH, chrome_options=options)


def send_whatsapp(message, num_tel):
    pywhatkit.sendwhatmsg_instantly(num_tel,
                                    message,
                                    10, tab_close=True
                                    )


def date_available(i):    
    driver.get(date_url)
    link = driver.find_element_by_partial_link_text("AQU")
    link.click()

    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Historial y cancelaciones"))
        )
        try:
            driver.implicitly_wait(40)
            link = driver.find_element("id", "1idDivNotAvailableSlotsTextTop")
            print("No hay horarios 8" + "=" * i + "D 😮️ ")

        except:
            send_whatsapp("hello_world", "+543512709882")
            print("por fín hay horarios wachín 🤘️")
    except:
        print("la pagina no carga wachín 💥️")


i = 1
while 1 != 2:
    if i % 30 == 0:
        i = 1
    print("execution number " + str(i))
    date_available(i)
    i += 1
    time.sleep(30)



