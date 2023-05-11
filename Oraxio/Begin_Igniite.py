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
#from Funciones_Excel import *
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
    f.Click_Mixto("xpath","//button[@type='button'][contains(.,'CONFIRM')]",t)
    time.sleep(5)

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_uno")
def test_dos_altaCuenta():
    print("Entrando al sistema dos")
    f.Click_Mixto("xpath", "//span[contains(.,'ACCOUNTS')]", 6)
    allure.attach(driver.get_screenshot_as_png(), name="ACCOUNTS", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","//button[@type='button'][contains(.,'LINK ACCOUNT')]",t)
    allure.attach(driver.get_screenshot_as_png(), name="Link_Account", attachment_type=AttachmentType.PNG)
    f.Texto_Mixto("xpath","//input[contains(@id,'name')]","AlexRdz3", t)
    allure.attach(driver.get_screenshot_as_png(), name="name", attachment_type=AttachmentType.PNG)


def teardown_function():
    print("Salida del test")
    driver.close()