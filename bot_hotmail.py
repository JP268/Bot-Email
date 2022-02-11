from selenium import webdriver
import time

def main():
    #Dados
    x = str(input("Digite seu email: "))
    y = str(input("Digite sua senha: "))
       
    #Abre o Google Chrome
    navegador = webdriver.Chrome()

    #Link do site desejado abrir 
    navegador.get("https://login.live.com/")

    #Login
    navegador.find_element_by_name("loginfmt").send_keys(x)
    navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(1)

    #Senha
    navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys(y)
    navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()

    navegador.find_element_by_xpath('//*[@id="KmsiCheckboxField"]').click()
    time.sleep(1)
    navegador.find_element_by_class_name("win-button button_primary button ext-button primary ext-primary").click()

main()