#automação de uma pesquisa no site Wikipedia.

from selenium import webdriver 

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

#inicializa o navegador

driver= webdriver.Edge()

driver.maximize_window()

#abrindo o link do site

driver.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")

#localizando o campo de pesquisa no site wikipedia.

caixa_pesquisa = driver.find_element (By.NAME, "search")
caixa_pesquisa.send_keys("Python")
time.sleep(3)
#btn_pesquisar = driver.find_element(By.XPATH,"//*[@id='searchform']/div/button")
#btn_pesquisar.click()  ou
caixa_pesquisa.send_keys(Keys.ENTER)




 
time.sleep(6)