from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciar_sesion(driver):
    driver.get("https://saucedemo.com")
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

def obtener_datos_primer_producto(driver):
    """Espera el catálogo y retorna el nombre y precio del primer producto."""
    primer_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    nombre = primer_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_item.find_element(By.CLASS_NAME, "inventory_item_price").text
    return {"nombre": nombre, "precio": precio}

def agregar_primer_producto_al_carrito(driver):
    """Hace clic en el botón Añadir al carrito del primer producto."""
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id^='add-to-cart']"))
    )
    boton.click()