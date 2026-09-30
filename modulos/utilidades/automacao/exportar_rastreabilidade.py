from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilidades.defs import mostrar_mensagem, navegador_google, click_js
from time import sleep
from rich import print


def automacao_rastreabilidade():

    data_inicial: str = str(input("Data inicial: ").strip())
    data_final: str = str(input("Data final: ").strip())
    
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
        pesquisa.send_keys("1697")

        rt = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Rastreabilidade Transações"))
        )
        click_js(caminho= rt, navegador= driver)
        
    except Exception as erro:
        print(f"Deu erro ao ir na tela 2031: {erro}")

    try:
        dropdawn_301 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div > div.hj-spaces-page-template-wrap > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > hj-template > div > hj-field-table > div > hj-field-table-row > div > hj-field-group > div > div > hj-field-group-row:nth-child(2) > div > hj-field-cell > div > hj-field-control > div > div > span.control-container > hj-template > div > hj-dropdownlist > span > span > span.k-input"))
        )
        click_js(caminho= dropdawn_301, navegador= driver)

        dropdawn_click_301 = driver.find_elements(
            By.XPATH,
            "//li[contains(., '301-Separação (pick)')]"
            )

        sleep(1)

        for i in dropdawn_click_301:
            if i.is_displayed():
                click_js(caminho= i, navegador= driver)
                break

    except Exception as erro:
        print(f"{erro}")

    hora = " 05:00:00"
    data_hi = data_inicial + hora
    data_hf = data_final + hora

    try:
        data_inicial_301 = WebDriverWait(driver= driver , timeout= 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div > div.hj-spaces-page-template-wrap > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > hj-template > div > hj-field-table > div > hj-field-table-row > div > hj-field-group > div > div > hj-field-group-row:nth-child(3) > div > hj-field-cell > div > hj-field-control > div > div > span.control-container > hj-template > div > hj-datetime-picker > span > span > input"))
        )
        data_inicial_301.clear()
        data_inicial_301.send_keys(data_hi)

    except Exception as erro:
        print(f"Erro ao colocar data inicial: {erro}")

    try:
        data_final_301 = WebDriverWait(driver= driver , timeout= 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div > div.hj-spaces-page-template-wrap > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > hj-template > div > hj-field-table > div > hj-field-table-row > div > hj-field-group > div > div > hj-field-group-row:nth-child(4) > div > hj-field-cell > div > hj-field-control > div > div > span.control-container > hj-template > div > hj-datetime-picker > span > span > input"))
        )
        data_final_301.clear()
        data_final_301.send_keys(data_hf)

    except Exception as erro:
        print(f"Erro ao colocar data final: {erro}")

    try:
        consulta_2 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Consulta"))
        )
        click_js(caminho= consulta_2, navegador= driver)

    except Exception as erro:
            print(f"Erro ao clickar em consulta_2: {erro}")
    
    sleep(1)
    
    try:
        exportar_301 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= exportar_301, navegador= driver)

    except Exception as erro:
            print(f"Erro ao clickar em exportar_301: {erro}")

    sleep(1)            
    try:
        voltar_301 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Rastreabilidade Transações"))
        )
        click_js(caminho= voltar_301, navegador= driver)

    except Exception as erro:
            print(f"Erro ao clickar em voltar_301: {erro}")
    
    sleep(1)            
    try:
        voltar_301_ = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Consultar Rastreabilidade Transações"))
        )
        click_js(caminho= voltar_301_, navegador= driver)

    except Exception as erro:
            print(f"Erro ao clickar em voltar_301_: {erro}")


    try:
        dropdawn_geral = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div > div.hj-spaces-page-template-wrap > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > hj-template > div > hj-field-table > div > hj-field-table-row > div > hj-field-group > div > div > hj-field-group-row:nth-child(2) > div > hj-field-cell > div > hj-field-control > div > div > span.control-container > hj-template > div > hj-dropdownlist > span > span > span.k-input"))
        )
        click_js(caminho= dropdawn_geral, navegador= driver)

        dropdawn_click_geral = driver.find_elements(
            By.XPATH,
            "//li[contains(., '<Qualquer>')]"
            )

        sleep(1)

        for i in dropdawn_click_geral:
            if i.is_displayed():
                click_js(caminho= i, navegador= driver)
                break

    except Exception as erro:
        print(f"dropdawn_geral_: {erro}") 

    try:
        data_inicial_geral = WebDriverWait(driver= driver , timeout= 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div > div.hj-spaces-page-template-wrap > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > hj-template > div > hj-field-table > div > hj-field-table-row > div > hj-field-group > div > div > hj-field-group-row:nth-child(3) > div > hj-field-cell > div > hj-field-control > div > div > span.control-container > hj-template > div > hj-datetime-picker > span > span > input"))
        )
        data_inicial_geral.clear()
        data_inicial_geral.send_keys(data_hi)

    except Exception as erro:
        print(f"Erro ao colocar data_inicial_geral: {erro}")

    try:
        data_final_geral = WebDriverWait(driver= driver , timeout= 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div > div.hj-spaces-page-template-wrap > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > hj-template > div > hj-field-table > div > hj-field-table-row > div > hj-field-group > div > div > hj-field-group-row:nth-child(4) > div > hj-field-cell > div > hj-field-control > div > div > span.control-container > hj-template > div > hj-datetime-picker > span > span > input"))
        )
        data_final_geral.clear()
        data_final_geral.send_keys(data_hf)

    except Exception as erro:
        print(f"Erro ao colocar data_final_geral: {erro}")

    try:
        consulta_2_geral = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Consulta"))
        )
        click_js(caminho= consulta_2_geral, navegador= driver)

    except Exception as erro:
            print(f"Erro ao clickar em consulta_2_geral: {erro}")
    
    sleep(4)
    
    try:
        exportar_geral = WebDriverWait(driver= driver, timeout= 50).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= exportar_geral, navegador= driver)

    except Exception as erro:
            print(f"Erro ao clickar em exportar_geral: {erro}")                   

    
    mostrar_mensagem("Sucesso!", "Exportação de Rastreabilidade Concluída!")
    driver.quit()