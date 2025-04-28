from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class MercadoLibreSearch(BasePage):
    BUSQUEDA_TEXT = (By.ID, 'cb1-edit')
    BUSQUEDA_BUTTON = (By.XPATH, '/html/body/header/div/div[2]/form/button')
    RESULTADO = (By.XPATH, '/html/body/main/div/div[2]/section/div[7]/ol/li[1]/div/div/div/div[2]/h3/a/text()')

    def buca(self, busqueda):
        self.enter_text(self.BUSQUEDA_TEXT, busqueda)
        self.click(self.BUSQUEDA_BUTTON)
       

    def isElementPresent(self):
        elemento = self.find_element(self.RESULTADO)
        texto =elemento.text
        return texto 
    

    


