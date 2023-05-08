# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://the-internet.herokuapp.com/login')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva


# completam username in f de atribuit=valoare

chrome.find_element(By.XPATH, '//input[@id="username"]').send_keys('tomsmith')

# completam username in f de atribuit=valoare

chrome.find_element(By.XPATH, '//input[@id="password"]').send_keys('SuperSecretPassword')

# dam click pe elemental selenium link in f de textul elementului
# * cautam prin toate elementele

chrome.find_element(By.XPATH, '//*[text()=" Login"]').click()

# verificam ca am ajuns pe pagina corecta

expected = 'https://the-internet.herokuapp.com/secure'
actual = chrome.current_url
assert expected == actual, 'Incorrect url, was expecting' + expected

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')

# fail
