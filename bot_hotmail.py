from selenium import webdriver
import time

x = str(input("Digite seu email: "))
y = str(input("Digite sua senha: "))
#Abre o Google Chrome
navegador = webdriver.Chrome()

#Link do site desejado abrir 
navegador.get("https://login.live.com/")

#->Clicar e Escrever no local desejado 

#Login
navegador.find_element_by_name("loginfmt").send_keys(x)
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(1)

#Senha
navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys("55943851")
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
