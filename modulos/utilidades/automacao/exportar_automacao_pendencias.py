from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilidades.defs import mostrar_mensagem, navegador_google, click_js
from time import sleep
from rich import print


def automacao_pendencia():

    data: str = str(input("Data: ").strip())
    data_2: str = str(input("Data-Hora Inicio: ").strip())
    data_3: str = str(input("Data-Hora Fim: ").strip())
    
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
        pesquisa.send_keys("2031")

        ahpc = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acomp. Hora da Produção Carreg."))
        )
        click_js(caminho= ahpc, navegador= driver)
    except Exception as erro:
        print(f"Deu erro ao ir na tela 2031: {erro}")

    try:
        data_1 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div > div.hj-spaces-page-template-wrap > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > hj-template > div > hj-field-table > div > hj-field-table-row > div > hj-field-group > div > div > hj-field-group-row:nth-child(2) > div > hj-field-cell > div > hj-field-control > div > div > span.control-container > hj-template > div > hj-date-picker > span > span > input"))
        )
        data_1.clear()
        data_1.send_keys(data)

        consultar = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Consulta")))
        click_js(caminho= consultar, navegador= driver)

    except Exception as erro:
        print(f"Deu erro ao colocar data ou consultar. {erro}")

    try:
        data_s = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(2) > div.hj-spaces-page-template-wrap > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > hj-template > div > hj-field-table > div > hj-field-table-row > div > hj-field-group > div > div:nth-child(2) > hj-field-group-row:nth-child(3) > div > hj-field-cell > div > hj-field-control > div > div > span.control-container > hj-template > div > hj-datetime-picker > span > span > input"))
        )
        data_s.clear()
        data_s.send_keys(data_2)

        data_a = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(2) > div.hj-spaces-page-template-wrap > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > hj-template > div > hj-field-table > div > hj-field-table-row > div > hj-field-group > div > div:nth-child(2) > hj-field-group-row:nth-child(4) > div > hj-field-cell > div > hj-field-control > div > div > span.control-container > hj-template > div > hj-datetime-picker > span > span > input"))
        )
        data_a.clear()
        data_a.send_keys(data_3)
        
        consultar_1 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Consulta")))
        click_js(caminho= consultar_1, navegador= driver)

    except Exception as erro:
        print(f"ERRO AO COLOCAR DATAs ou consulta: {erro}")

    
    # thread = threads()

    try:
        pend_1 = WebDriverWait(driver=driver, timeout=20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(3) > div.hj-spaces-page-template-wrap > hj-flex-container > div > hj-flex-grow > div > div > hj-grid > div.hj-grid-container.hj-grid-full-height-container > div > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(1) > td:nth-child(13) > a > hj-label"))
        )
        click_js(caminho= pend_1, navegador= driver)

        sleep(1)
        

        export_1 = WebDriverWait(driver=driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= export_1, navegador= driver)

        voltar1_1 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento - Pendência Gerada"))
        )
        click_js(caminho= voltar1_1, navegador= driver)

        voltar2_1 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento"))
        )
        click_js(caminho= voltar2_1, navegador= driver)

    except Exception as erro:
        print(f"Erro ao entrar para exportar pendencias 1: {erro}")
    #---------------------------------------------------------------------------------------
    try:
        pend_2 = WebDriverWait(driver=driver, timeout=20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(3) > div.hj-spaces-page-template-wrap > hj-flex-container > div > hj-flex-grow > div > div > hj-grid > div.hj-grid-container.hj-grid-full-height-container > div > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(2) > td:nth-child(13) > a > hj-label > span"))
        )
        click_js(caminho= pend_2, navegador= driver)

        sleep(1)


        export_2 = WebDriverWait(driver=driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= export_2, navegador= driver)

        sleep(1)

        voltar1_2 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento - Pendência Gerada"))
        )
        click_js(caminho= voltar1_2, navegador= driver)

        sleep(1)

        voltar2_2 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento"))
        )
        click_js(caminho= voltar2_2, navegador= driver)

    except Exception as erro:
        print(f"Erro ao entrar para exportar pendencias 2: {erro}")        
        #---------------------------------------------------------------------------------------
    try:
        pend_3 = WebDriverWait(driver=driver, timeout=20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(3) > div.hj-spaces-page-template-wrap > hj-flex-container > div > hj-flex-grow > div > div > hj-grid > div.hj-grid-container.hj-grid-full-height-container > div > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(3) > td:nth-child(13) > a > hj-label > span"))
        )
        click_js(caminho= pend_3, navegador= driver)

        sleep(1)


        export_3 = WebDriverWait(driver=driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= export_3, navegador= driver)

        sleep(1)

        voltar1_3 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento - Pendência Gerada"))
        )
        click_js(caminho= voltar1_3, navegador= driver)

        sleep(1)

        voltar2_3 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento"))
        )
        click_js(caminho= voltar2_3, navegador= driver)

    except Exception as erro:
        print(f"Erro ao entrar para exportar pendencias 3: {erro}")
        #---------------------------------------------------------------------------------------
    try:
        pend_4 = WebDriverWait(driver=driver, timeout=20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(3) > div.hj-spaces-page-template-wrap > hj-flex-container > div > hj-flex-grow > div > div > hj-grid > div.hj-grid-container.hj-grid-full-height-container > div > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(4) > td:nth-child(13) > a > hj-label > span"))
        )
        click_js(caminho= pend_4, navegador= driver)

        sleep(1)


        export_4 = WebDriverWait(driver=driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= export_4, navegador= driver)

        sleep(1)

        voltar1_4 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento - Pendência Gerada"))
        )
        click_js(caminho= voltar1_4, navegador= driver)

        sleep(1)

        voltar2_4 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento"))
        )
        click_js(caminho= voltar2_4, navegador= driver)

    except Exception as erro:
        print(f"Erro ao entrar para exportar pendencias 4: {erro}")
        
        #---------------------------------------------------------------------------------------

    try:
        pend_5 = WebDriverWait(driver=driver, timeout=20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(3) > div.hj-spaces-page-template-wrap > hj-flex-container > div > hj-flex-grow > div > div > hj-grid > div.hj-grid-container.hj-grid-full-height-container > div > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(5) > td:nth-child(13) > a > hj-label > span"))
        )
        click_js(caminho= pend_5, navegador= driver)

        sleep(1)


        export_5 = WebDriverWait(driver=driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= export_5, navegador= driver)

        sleep(1)

        voltar1_5 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento - Pendência Gerada"))
        )
        click_js(caminho= voltar1_5, navegador= driver)

        sleep(1)

        voltar2_5 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento"))
        )
        click_js(caminho= voltar2_5, navegador= driver)

    except Exception as erro:
        print(f"Erro ao entrar para exportar pendencias 5: {erro}")

        #---------------------------------------------------------------------------------------

    try:
        pend_6 = WebDriverWait(driver=driver, timeout=20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(3) > div.hj-spaces-page-template-wrap > hj-flex-container > div > hj-flex-grow > div > div > hj-grid > div.hj-grid-container.hj-grid-full-height-container > div > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(6) > td:nth-child(13) > a > hj-label > span"))
        )
        click_js(caminho= pend_6, navegador= driver)

        sleep(1)


        export_6 = WebDriverWait(driver=driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= export_6, navegador= driver)

        sleep(1)

        voltar1_6 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento - Pendência Gerada"))
        )
        click_js(caminho= voltar1_6, navegador= driver)

        sleep(1)

        voltar2_6 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento"))
        )
        click_js(caminho= voltar2_6, navegador= driver)

    except Exception as erro:
        print(f"Erro ao entrar para exportar pendencias 6: {erro}")

    #---------------------------------------------------------------------------------------

    try:
        pend_7 = WebDriverWait(driver=driver, timeout=20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(3) > div.hj-spaces-page-template-wrap > hj-flex-container > div > hj-flex-grow > div > div > hj-grid > div.hj-grid-container.hj-grid-full-height-container > div > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(7) > td:nth-child(13) > a > hj-label > span"))
        )
        click_js(caminho= pend_7, navegador= driver)

        sleep(1)
        

        export_7 = WebDriverWait(driver=driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= export_7, navegador= driver)

        sleep(1)

        voltar1_7 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento - Pendência Gerada"))
        )
        click_js(caminho= voltar1_7, navegador= driver)

        sleep(1)

        voltar2_7 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento"))
        )
        click_js(caminho= voltar2_7, navegador= driver)

    except Exception as erro:
        print(f"Erro ao entrar para exportar pendencias 7: {erro}")

        #---------------------------------------------------------------------------------------

    try:
        pend_8 = WebDriverWait(driver=driver, timeout=20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(3) > div.hj-spaces-page-template-wrap > hj-flex-container > div > hj-flex-grow > div > div > hj-grid > div.hj-grid-container.hj-grid-full-height-container > div > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(8) > td:nth-child(13) > a > hj-label > span"))
        )
        click_js(caminho= pend_8, navegador= driver)

        sleep(1)
       

        export_8 = WebDriverWait(driver=driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= export_8, navegador= driver)

        sleep(1)

        voltar1_8 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento - Pendência Gerada"))
        )
        click_js(caminho= voltar1_8, navegador= driver)

        sleep(1)

        voltar2_8 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento"))
        )
        click_js(caminho= voltar2_8, navegador= driver)

    except Exception as erro:
        print(f"Erro ao entrar para exportar pendencias 8: {erro}")

        #---------------------------------------------------------------------------------------

    try:
        pend_9 = WebDriverWait(driver=driver, timeout=20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(3) > div.hj-spaces-page-template-wrap > hj-flex-container > div > hj-flex-grow > div > div > hj-grid > div.hj-grid-container.hj-grid-full-height-container > div > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(9) > td:nth-child(13) > a > hj-label > span"))
        )
        click_js(caminho= pend_9, navegador= driver)

        sleep(1)        

        export_9 = WebDriverWait(driver=driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= export_9, navegador= driver)

        sleep(1)

        voltar1_9 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento - Pendência Gerada"))
        )
        click_js(caminho= voltar1_9, navegador= driver)

        sleep(1)

        voltar2_9 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento"))
        )
        click_js(caminho= voltar2_9, navegador= driver)

    except Exception as erro:
        print(f"Erro ao entrar para exportar pendencias 9: {erro}")        
        #---------------------------------------------------------------------------------------

    try:
        pend_10 = WebDriverWait(driver=driver, timeout=20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(3) > div.hj-spaces-page-template-wrap > hj-flex-container > div > hj-flex-grow > div > div > hj-grid > div.hj-grid-container.hj-grid-full-height-container > div > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(10) > td:nth-child(13) > a > hj-label > span"))
        )
        click_js(caminho= pend_10, navegador= driver)

        sleep(1)
       

        export_10 = WebDriverWait(driver=driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= export_10, navegador= driver)

        sleep(1)

        voltar1_10 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento - Pendência Gerada"))
        )
        click_js(caminho= voltar1_10, navegador= driver)

        sleep(1)

        voltar2_10 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento"))
        )
        click_js(caminho= voltar2_10, navegador= driver)

    except Exception as erro:
        print(f"Erro ao entrar para exportar pendencias 10: {erro}")
        #---------------------------------------------------------------------------------------
    
    try:
        pend_11 = WebDriverWait(driver=driver, timeout=20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.page-wrap > div.content-wrap > div > div > div > hj-flex-container > div > hj-flex-grow > div > hj-flex-scroll > div > div:nth-child(2) > div:nth-child(3) > div.hj-spaces-page-template-wrap > hj-flex-container > div > hj-flex-grow > div > div > hj-grid > div.hj-grid-container.hj-grid-full-height-container > div > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(11) > td:nth-child(13) > a > hj-label > span"))
        )
        click_js(caminho= pend_11, navegador= driver)

        sleep(1)
       

        export_11 = WebDriverWait(driver=driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Exportar"))
        )
        click_js(caminho= export_11, navegador= driver)

        sleep(1)

        voltar1_11 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento - Pendência Gerada"))
        )
        click_js(caminho= voltar1_11, navegador= driver)

        sleep(1)

        voltar2_11 = WebDriverWait(driver= driver, timeout= 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Acompanhamento por Hora do Carregamento"))
        )
        click_js(caminho= voltar2_11, navegador= driver)

    except Exception as erro:
        print(f"Erro ao entrar para exportar pendencias 11: {erro}")        

    mostrar_mensagem("Sucesso!", "Exportação de Pendências Concluída!")
    driver.quit()