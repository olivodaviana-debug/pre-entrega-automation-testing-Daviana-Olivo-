import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.funciones import (
    iniciar_sesion, 
    obtener_datos_primer_producto, 
    agregar_primer_producto_al_carrito
)

def test_automatizacion_login(driver):
    """Caso 1: Verificar Login Exitoso y elementos de cabecera."""
    iniciar_sesion(driver)
    
    assert "/inventory.html" in driver.current_url
    
    titulo_header = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo_header == "Products"
    
    logo_app = driver.find_element(By.CLASS_NAME, "app_logo").text
    assert logo_app == "Swag Labs"

def test_verificacion_catalogo(driver):
    """Caso 2: Verificar título, presencia de productos e interfaz."""
    iniciar_sesion(driver)
    
    titulo_pagina = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo_pagina == "Products"
    
    datos_prod = obtener_datos_primer_producto(driver)
    assert len(datos_prod["nombre"]) > 0
    print(f"\n[INFO] Producto: {datos_prod['nombre']} | Precio: {datos_prod['precio']}")
    
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()

def test_interaccion_carrito(driver):
    """Caso 3: Añadir producto, verificar contador y validar ítem en carrito."""
    iniciar_sesion(driver)
    
    # Guardamos los datos esperados antes de añadirlo
    datos_esperados = obtener_datos_primer_producto(driver)
    
    agregar_primer_producto_al_carrito(driver)
    
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1"
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))
    
    nombre_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_en_carrito == datos_esperados["nombre"]