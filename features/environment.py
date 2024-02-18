from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure

def before_scenario(context, driver):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    
def after_scenario(context, driver):
    context.driver.quit()
    
def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", 
                      attachment_type=allure.attachment_type.PNG)