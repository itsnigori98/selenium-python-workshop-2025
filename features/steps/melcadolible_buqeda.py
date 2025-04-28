from behave import given, when, then 
from selenium import webdriver
from pages.busqueda_mercadoLibre import MercadoLibreSearch 

@given('el usualio busca un producto en el bucadol')
def step_given_search_mercadoLibre(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co/')
    context.busqueda_mercadoLibre = MercadoLibreSearch(context.driver)

@when('el usuario escribe iPhone 13')
def step_when_search_iphone(context):
    context.busqueda_mercadoLibre.buca("iPhone 13")

@then('aparece texto con iPhone')
def step_then_search_do(context):
    body_text = context.driver.find_element("tag name", "body").text
    print(f"Texto encontrado en el body: {body_text}") 
    assert "iPhone" in body_text
