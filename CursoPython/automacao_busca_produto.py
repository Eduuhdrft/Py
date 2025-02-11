#automatizando busca de produtos.

#importanto as bibliotecas

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# iniciando o navegador

driver= webdriver.Edge()

#abrindo o link.

driver.get("https://www.casasbahia.com.br/?utm_source=bing_branding&utm_medium=cpc&utm_campaign=gg_brd_inst_cb_exata&msclkid=724bb5b3c6f41294ec48d308335a6bf7")

#colocando tempo para o navegador esperar

time.sleep(8)

#interagindo com a barra de pesquisa]
0
barra_pesquisa = driver.find_element(By.ID,"search-form-input")
barra_pesquisa.send_keys("Geladeira")
time.sleep(6)