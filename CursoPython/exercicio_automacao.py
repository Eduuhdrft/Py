#automatizando um formulario na web.

#importando as bibliotecas.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

#iniciando o navegado.

driver=webdriver.Edge()
driver.maximize_window()

#acesse a pagina do formulario

driver.get("https://demo.automationtesting.in/Register.html")

#aguarde a pagina carregar para clicar no item desejado.

time.sleep(2)

#preenchendo o primeiro nome.

primeiro_nome = driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[1]/div[1]/input") #quando usar xpath usar apostrofo.
primeiro_nome.send_keys("Eduardo")
time.sleep(3)  

ultimo_nome = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[1]/div[2]/input')
ultimo_nome.send_keys("Jeronimo")
time.sleep(3)

address = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[2]/div/textarea')
address.send_keys("Rua antonio pedro da silva,n145, jd marina.")
time.sleep(3)

email = driver.find_element(By.XPATH,'//*[@id="eid"]/input')
email.send_keys("Eduardo.mlj@hotmail.com")
time.sleep(3)

tel = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[4]/div/input')
tel.send_keys("(11)98239-1515")
time.sleep(3)

gender = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input')
gender.click()
time.sleep(3)

hobbie = driver.find_element(By.ID,'checkbox2')
hobbie.click()
time.sleep(3)

languages_click = driver.find_element(By.ID,'msdd')
languages_click.click()
time.sleep(3)

language_enter = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[8]')
language_enter.click()
time.sleep(2)

skills = driver.find_element(By.XPATH,'//*[@id="Skills"]/option[32]')
skills.click()
time.sleep(3)

select_contry=driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span')
select_contry.click()
time.sleep(2)

select_country2= driver.find_element(By.XPATH,'//*[@id="select2-country-results"]/li[3]')
select_country2.click
time.sleep(2)




                         