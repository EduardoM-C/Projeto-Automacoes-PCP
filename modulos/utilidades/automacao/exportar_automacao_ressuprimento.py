from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilidades.defs import mostrar_mensagem, navegador_google, click_js
from time import sleep
from rich import print

def automacao_ressuprimento():

    try:
        driver = navegador_google()
    except Exception as erro:
        print(f"Deu erro ao carregar o google: {erro}")

    try:
        login = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > hj-logon > div > div > div.bottom > hj-button > button")))
        click_js(caminho= login, navegador= driver)

        menu = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.ID, "menuButtonToggle")))
        click_js(caminho= menu, navegador= driver)

        pesquisa = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu > div > input[type=text]")))
        pesquisa.clear()
        pesquisa.send_keys("1653")

        ahpc = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Ressupr. em Aberto"))
        )
        click_js(caminho= ahpc, navegador= driver)
        
    except Exception as erro:
        print(f"Deu erro ao ir na tela 1653: {erro}")

    try:
        consulta = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Consulta"))
        )
        click_js(caminho= consulta, navegador= driver)

    except Exception as erro:
        print(f"erro nao clickar em consulta: {erro}")

    sleep(1)

    try:
        exportar = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= exportar, navegador= driver)

    except Exception as error:
        print(f"erro ao exportar: {error}")

    try:
        msg = mostrar_mensagem(erro= "sucesso", mensagem="Automação concluida, pode fechar navegador?")
        driver.quit()
    except Exception as erro:
        print(f"Erro ao fechar navegador {erro}")

