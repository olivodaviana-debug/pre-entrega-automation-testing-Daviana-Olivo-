import os
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    yield driver
    
    # Si el test falla, toma una captura de pantalla automáticamente
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("reports", exist_ok=True)
        test_name = request.node.name.replace("[", "_").replace("]", "_")
        driver.save_screenshot(f"reports/fallo_{test_name}.png")
        
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)