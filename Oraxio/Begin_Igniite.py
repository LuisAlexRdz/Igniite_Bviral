###Ruta server allure: http://192.168.137.1:50881/index.html###
###Ejecutar test: pytest .\Fixture_Decorate_2.py --alluredir="./allurereports"###
###abrir reporte: allure serve .\allurereports\

import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from Funciones_Excel import *
from Funciones import Funciones_Globales
from selenium.webdriver import ActionChains
t= 1


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)


@pytest.fixture(scope="module")
def setup_login_uno():
    global driver, f
    driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
    driver.get("https://test.igniite.io/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    allure.attach(driver.get_screenshot_as_png(), name="oraxio", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","(//button[contains(.,'GET STARTED')])[2]",t)
    allure.attach(driver.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)
    f.Texto_Mixto("id", "user", "LuisAlexRdz", t)
    allure.attach(driver.get_screenshot_as_png(), name="user", attachment_type=AttachmentType.PNG)
    f.Texto_Mixto("id", "password", "Alex1983", t)
    allure.attach(driver.get_screenshot_as_png(), name="psw", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'LOGIN')]", 5)
    print("Entrando al sistema")
    ##yield
    ##print("Saliendo del login dos")
    ##driver.close()


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_uno")
def test_uno_Navega():
    print("Entrando al sistema uno")
    f.Click_Mixto("xpath","//span[contains(.,'LIVE TRADING')]",t)
    allure.attach(driver.get_screenshot_as_png(),name="LIVE_TRADING", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","//span[contains(.,'ACCOUNTS')]",6)
    allure.attach(driver.get_screenshot_as_png(), name="ACCOUNTS", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","(//span[contains(.,'ADMIN')])[1]",t)
    allure.attach(driver.get_screenshot_as_png(), name="ADMIN", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","//span[contains(.,'HOME')]",t)
    allure.attach(driver.get_screenshot_as_png(), name="HOME", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath", "//span[contains(.,'RESOLVER')]", 3)
    allure.attach(driver.get_screenshot_as_png(), name="RESOLVE", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","//header/div[1]/div[3]/div[2]/div[3]/*[1]",t)
    allure.attach(driver.get_screenshot_as_png(), name="logout", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","//button[@type='button'][contains(.,'CONFIRM')]",t)
    allure.attach(driver.get_screenshot_as_png(), name="confirm", attachment_type=AttachmentType.PNG)
    time.sleep(5)

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_uno")
def test_dos_altaCuenta():
    print("Entrando al sistema dos")
    fe = Funexcel(driver)
    f.Click_Mixto("xpath", "//span[contains(.,'ACCOUNTS')]", 6)
    allure.attach(driver.get_screenshot_as_png(), name="ACCOUNTS", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","//button[@type='button'][contains(.,'LINK ACCOUNT')]",t)
    allure.attach(driver.get_screenshot_as_png(), name="Link_Account", attachment_type=AttachmentType.PNG)
    ruta = "C://Users//PRIDE OMEGA//Documents//Alex Rdz//Igniite_Selenium//Igniite_Bviral//Documentos//accounts_ok.xlsx"
    filas = fe.getRowCount(ruta, "Hoja1")

    for i in range(2, filas + 1):
        Name = fe.readData(ruta, "Hoja1", i, 1)
        Key = fe.readData(ruta, "Hoja1", i, 2)
        Secret = fe.readData(ruta, "Hoja1", i, 3)

        f.Texto_Mixto("xpath", "//input[contains(@id,'name')]", Name, t)
        allure.attach(driver.get_screenshot_as_png(), name="name", attachment_type=AttachmentType.PNG)
        f.Texto_Mixto("xpath", "//input[contains(@id,'key')]", Key, t)
        allure.attach(driver.get_screenshot_as_png(), name="key", attachment_type=AttachmentType.PNG)
        f.Texto_Mixto("xpath", "//input[contains(@id,'secret')]", Secret, t)
        allure.attach(driver.get_screenshot_as_png(), name="secret", attachment_type=AttachmentType.PNG)
        f.Click_Mixto("xpath","//button[@type='submit'][contains(.,'SAVE')]", t)
        allure.attach(driver.get_screenshot_as_png(), name="save", attachment_type=AttachmentType.PNG)
        f.Click_Mixto("xpath","//button[@type='button'][contains(.,'YES')]",5)

        e = f.Existe("xpath", "//input[contains(@id,'name')]", t)
        if (e == "Existe"):
            print("El elemento se inserto correctamente")
            fe.writeData(ruta, "Hoja1", i, 4, "Insertado")
            fe.writeData(ruta, "Hoja1", i, 5, "Sub Account: " + Name)
        else:

            print("No se inserto")
            fe.writeData(ruta, "Hoja1", i, 4, "Error")

    f.Click_Mixto("xpath", "//header/div[1]/div[3]/div[2]/div[3]/*[1]", t)
    allure.attach(driver.get_screenshot_as_png(), name="logout", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath", "//button[@type='button'][contains(.,'CONFIRM')]", t)
    allure.attach(driver.get_screenshot_as_png(), name="confirm", attachment_type=AttachmentType.PNG)

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_uno")
def test_dos_bajaCuenta():
    print("Entrando al sistema tres")
    f.Click_Mixto("xpath", "//span[contains(.,'ACCOUNTS')]", 6)
    allure.attach(driver.get_screenshot_as_png(), name="ACCOUNTS", attachment_type=AttachmentType.PNG)
    txt = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.XPATH,"//div[@class='text-base text-palette-beigde-100'][contains(.,'Sub Account:')]"))))




def teardown_function():
    print("Salida del test")
    driver.close()