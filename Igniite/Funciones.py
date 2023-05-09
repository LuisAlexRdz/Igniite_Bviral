import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from  selenium.webdriver import ActionChains

class Funciones_Globales():

    def __init__(self,driver):
        self.driver=driver

    def Tiempo(self,tie):
        t = time.sleep(tie)
        return t

#Funcion Navega Pagina
    def Navegar(self, Url, tiempo):
        self.driver.get(Url)
        #self.driver.maximize_window()
        print("Pagina abierta: "+str(Url))
        t = time.sleep(tiempo)
        return t

#Funcion selecciona elemento
    def SelElXp(self,elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def SelElId(self,elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, elemento)
        return val

#Funcion Valida Texto
    def Texto_Mixto(self, tipo, selector, texto, tiempo):
        if (tipo=="xpath"):
            try:
                val = self.SelElXp(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
                return t
        if (tipo=="id"):
            try:
                val = self.SelElId(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)

#Funcion Click
    def Click_Mixto(self, tipo,selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SelElXp(selector)
                val.click()
                print("Damos click en boton {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
        elif (tipo == "id"):
            try:
                val = self.SelElId(selector)
                val.click()
                print("Damos click en boton {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)

#Funcion Select
    def Select_Xpath_Type(self, xpath,tipo,dato, tiempo):
        try:
            val = self.SelElXp(xpath)
            val = Select(val)
            if (tipo=="text"):
                val.select_by_visible_text(dato)
            elif (tipo=="index"):
                val.select_by_index(dato)
            elif (tipo=="value"):
                val.select_by_value(dato)
            print("El texto seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + xpath)

    def Select_ID_Type(self, ID,tipo,dato, tiempo):
        try:
            val = self.SelElId(ID)
            val = Select(val)
            if (tipo=="text"):
                val.select_by_visible_text(dato)
            elif (tipo=="index"):
                val.select_by_index(dato)
            elif (tipo=="value"):
                val.select_by_value(dato)
            print("El texto seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + ID)

#Funcion Cargar Imagen
    def Upload_Xpath(self, xpath, ruta, tiempo):
        try:
            val = self.SelElXp(xpath)
            val.send_keys(ruta)
            print("Se carga la imagen {} ".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro la imagen " + xpath)

    def Upload_ID(self, ID, ruta, tiempo):
        try:
            val = self.SelElId(ID)
            val.send_keys(ruta)
            print("Se carga la imagen {} ".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro la imagen " + ID)


#Funcion Radio y Check
    def Check_Xpath(self, xpath,  tiempo):
        try:
            val = self.SelElXp(xpath)
            val.click()
            print("Se activa casilla checkbox {} ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + xpath)


    def Check_ID(self, id,  tiempo):
        try:
            val = self.SelElId(id)
            val.click()
            print("Se activa casilla checkbox {} ".format(id))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + id)


    def Check_Xpath_Multiple(self, tiempo, *args):
        try:
            for num in args:
                val = self.SelElXp(num)
                val.click()
                print("Se activa casilla checkbox {} ".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro el elemento " + num)

#Funcion existe elemento
    def Existe(self, tipo,selector, tiempo):
        if (tipo=="xpath"):
            try:
                val = self.SelElXp(selector)
                print("El elemento {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
                return "No existe"
        elif (tipo=="id"):
            try:
                val = self.SelElId(selector)
                print("El elemento {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
                return "No existe"

#Funcion Mouse
    def Mouse_Double(self, tipo, selector, tiempo=2):
        if (tipo=="xpath"):
            try:
                val = self.SelElXp(selector)
                action = ActionChains(self.driver)
                action.double_click(val).perform()
                print("DoubleClick en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
                return t
        if (tipo=="id"):
            try:
                val = self.SelElId(selector)
                action = ActionChains(self.driver)
                action.double_click(val).perform()
                print("DoubleClick en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)

#Mouse Click Derecho
    def Mouse_Right_Click(self, tipo, selector, tiempo=2):
        if (tipo=="xpath"):
            try:
                val = self.SelElXp(selector)
                action = ActionChains(self.driver)
                action.context_click(val).perform()
                print("Click derecho en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
                return t
        if (tipo=="id"):
            try:
                val = self.SelElId(selector)
                action = ActionChains(self.driver)
                action.context_click(val).perform()
                print("Click derecho en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)

#Funcion Drag and Drop
    def Mouse_Drag_Drop(self, tipo, selector, destino, tiempo=2):
        if (tipo=="xpath"):
            try:
                val = self.SelElXp(selector)
                val2 = self.SelElXp(destino)
                action = ActionChains(self.driver)
                action.drag_and_drop(val, val2).perform()
                print("Se solto el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
                return t
        if (tipo=="id"):
            try:
                val = self.SelElId(selector)
                val2 = self.SelElId(destino)
                action = ActionChains(self.driver)
                action.drag_and_drop(val, val2).perform()
                print("Se solto el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)

    def Mouse_Drag_DropXY(self, tipo, selector, x,y, tiempo=2):
        if (tipo=="xpath"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SelElXp(selector)
                action = ActionChains(self.driver)
                action.drag_and_drop_by_offset(val, x,y).perform()
                print("Se movio el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
                return t
        if (tipo=="id"):
            try:
                #self.driver.switch_to.frame(0)
                val = self.SelElId(selector)
                action = ActionChains(self.driver)
                action.drag_and_drop_by_offset(val, x,y).perform()
                print("Se movio el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)

    def Click_XY(self, tipo, selector, x,y, tiempo=2):
        if (tipo=="xpath"):
            try:
                #self.driver.switch_to.frame(0)
                val = self.SelElXp(selector)
                action = ActionChains(self.driver)
                action.move_to_element_with_offset(val, x,y).click().perform()
                print("Click al elemento {} coordenada {}, {}".format(selector,x,y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
                return t
        if (tipo=="id"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SelElId(selector)
                action = ActionChains(self.driver)
                action.move_to_element_with_offset(val, x,y).click().perform()
                print("Click al elemento {} coordenada {}, {}".format(selector,x,y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)

    def Salida(self):
        print("Se termina la prueba exitosamente")
