import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from Funciones import Funciones_Globales
from  selenium.webdriver import ActionChains
t= 5

def get_Data():
    return [
        ("AlexRdzPdr", "Alex1983")
    ]


@pytest.mark.parametrize("user,clave", get_Data())
def test_login(user,clave):
    global  driver, f
    driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
    driver.get("https://test.igniite.io/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.Texto_Mixto("xpath","//input[contains(@id,'user')]", user, t)
    f.Texto_Mixto("xpath","//input[contains(@id,'password')]", clave, t)
    f.Click_Mixto("xpath","//button[@type='submit'][contains(.,'LOGIN')]",t)
    print("Entrando al sistema")

def teardown_function():
    print("Salida del test")
    driver.close()
