from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, base64
import pandas as pd
import pickle

PATH = "C:/Users/svelez/Documents/botsRPA/chromedriver.exe"
picture_options = Options()
picture_options.add_argument("--start-maximized")
init = webdriver.Chrome(PATH, chrome_options=picture_options)

# ---------------INGRESAR AL SITIO DESEADO, Y SE LOGUEA CON USUARIO Y CONTRASEÑA---------------:

# init.get("website url")
# login_button = WebDriverWait(init, 60).until(EC.presence_of_element_located((By.ID, 'uname')))
# login_button.send_keys("username")
# password_button = WebDriverWait(init, 60).until(EC.presence_of_element_located((By.ID, 'pwd'))) 
# password_button.send_keys("password")
# enter_button = WebDriverWait(init, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div[1]/div/div/table/tbody/tr[5]/td[2]/input'))).click()


# LA LINEA pickle.dump ES PARA GUARDAR EN UN ARCHIVO cookies.pkl (SE CREA SOLO) LAS COOKIES DEL SITIO UNA VEZ ESTE LOGUEADO (SE DEBE COMENTAR ESA LINEA UNA VEZ LAS COOKIES YA HAYAN SIDO RECOLECTADAS LA PRIMERA VEZ, Y SOLO SE DEJA LA PARTE QUE CARGA LAS COOKIES AL NAVEGADOR (LINEA 36 A 41)):

# pickle.dump(init.get_cookies() , open("cookies.pkl","wb"))    


# ESTA PARTE INGRESA AL SITIO DESEADO, CARGA LAS COOKIES Y LAS INGRESA EN EL SITIO WEB UNA POR UNA CON EL CICLO FOR, LUEGO REFRESCA EL SITIO PARA QUE INGRESE NUEVAMENTE YA UTILIZANDO LAS COOKIES:

init.get("website url")
cookies = pickle.load(open("C:/Users/svelez/Documents/botsRPA/RPA_consumo_xls/cookies.pkl", "rb"))
for cookie in cookies:
    init.add_cookie(cookie)
    
init.refresh()
    
        
