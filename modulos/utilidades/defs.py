import os
import subprocess
from functools import lru_cache

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options

from webdriver_manager.microsoft import EdgeChromiumDriverManager 

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tkinter import messagebox, Tk

from rich import print as print
from time import sleep

import customtkinter as ctk


def options_edge() -> Options:
    options = Options()

    from utilidades.usuarios import CAMINHO
    caminho_download: str = str(CAMINHO/"dwns")

    if not os.path.exists(caminho_download):
        os.makedirs(caminho_download)

    preferencias = {
        # Define o caminho da nova pasta de download
        "download.default_directory": caminho_download,
        # Desativa a janela de perguntar "Onde deseja salvar"
        "download.prompt_for_download": False,
        # Atualiza o diretório de downloads nas configurações internas
        "download.directory_upgrade": True,
        # Desativa avisos de segurança sobre baixar arquivos
        "safebrowsing.enabled": True,
        "download_bubble.partial_view_enabled": False,
    }

    options.add_experimental_option("prefs", preferencias)
    options.add_argument(
    "--disable-features=DownloadBubble,DownloadBubbleV2"
    )

    # CORREÇÃO 1: Faltava retornar o objeto de opções configurado
    return options


@lru_cache(maxsize=1)
def obter_edgedriver() -> str:
    """Resolve e cacheia o caminho do Edgedriver para o processo atual."""
    return EdgeChromiumDriverManager().install()

def criar_service() -> EdgeService:
    """
    Cria um Service do Chrome de forma consistente entre maquinas.
    No Windows, forca o processo do chromedriver sem janela de console.
    """
    service = EdgeService(
        executable_path=obter_edgedriver(),
        log_output=subprocess.DEVNULL,
    )

    if os.name == "nt":
        create_no_window = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)
        service.creation_flags = create_no_window
    return service

def registrar_progresso(text: str, endereco, sucesso=True, file_path="progresso.txt"):
    """Registra o progresso das operacoes em um arquivo."""
    with open(file_path, "a", encoding="utf-8") as arquivo:
        status = "SUCESSO" if sucesso else "FALHA"
        arquivo.write(f"{text} {endereco} - Status: {status}\n")

def navegador_google():

    options = options_edge()
    service = criar_service()
    navegador = webdriver.Edge(service=service, options= options)
    navegador.get("https://wmsweb-prd.martins.com.br/core/Default.html")
    navegador.maximize_window()

    return navegador

def clicar_quando_estavel(navegador, locator, timeout=20, tentativas=3):
    ultimo_erro = None

    for tentativa in range(tentativas):
        try:
            elemento = WebDriverWait(
                navegador,
                timeout,
                ignored_exceptions=(StaleElementReferenceException,),
            ).until(EC.element_to_be_clickable(locator))

            navegador.execute_script(
                "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                elemento,
            )

            try:
                elemento.click()
            except ElementClickInterceptedException:
                navegador.execute_script("arguments[0].click();", elemento)

            return elemento
        except StaleElementReferenceException as erro:
            ultimo_erro = erro

            if tentativa < tentativas - 1:
                sleep(0.3)

        raise ultimo_erro

def mostrar_mensagem(erro, mensagem):
    
    root = Tk()
    root.withdraw()              # Esconde a janela
    root.attributes("-topmost", True)
    root.lift()


    messagebox.showinfo(
        erro,
        mensagem,
        parent=root
    )

    root.destroy()

def limpar_tela():
    limpar = os.system("cls" if os.name =="nt" else "clear")
    return limpar

def erro_login(master):
    
    janela = ctk.CTkToplevel(master)

    janela.title("Erro")
    janela.geometry("300x140")
    janela.resizable(False, False)

    # Deixa a janela modal
    janela.transient(master)
    janela.grab_set()

    # Centraliza na janela principal
    janela.update_idletasks()

    x = master.winfo_rootx() + (master.winfo_width() // 2) - 150
    y = master.winfo_rooty() + (master.winfo_height() // 2) - 70

    janela.geometry(f"300x140+{x}+{y}")

    # Frame principal
    frame = ctk.CTkFrame(
        janela,
        fg_color="transparent"
    )
    frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # Ícone pequeno
    ctk.CTkLabel(
        frame,
        text="❌",
        font=("Segoe UI Emoji", 24),
        text_color="#FF0000"
    ).pack(pady=(10, 5))

    # Mensagem
    ctk.CTkLabel(
        frame,
        text="Usuário ou senha incorretos.",
        font=("Arial", 14)
    ).pack()

    # Botão
    ctk.CTkButton(
        frame,
        text="OK",
        width=80,
        command=janela.destroy
    ).pack(pady=10)


def click_js(caminho, navegador):
    navegador.execute_script("arguments[0].click();", caminho)
