from pwinput import pwinput
from utilidades.usuarios import (
                                 carregar_usuario,
                                 validar_login,
                                 registrar_usuario,
                                 alterar_senha
                                )
from utilidades.painel import painel
from time import sleep

from rich import print
from rich.text import Text
from rich.rule import Rule

from utilidades.defs import limpar_tela




def validacao_login(user_: str, senha_: str, event= None):

    usuarios = carregar_usuario()

    usuario = str(user_).upper().strip()
    senha = str(senha_).strip()

    try: 

        resultado = validar_login(usuario, senha)

        user = str(usuario).upper()
        usuarios = usuarios[user]

        if resultado:
            print("[green]Login realizado com sucesso.[/green]")
            return resultado

        else:
            print("Erro ao no login")


    except KeyError:
        print("Usuario nao existe no banco de dados.")

def painel_alterar_registro(user):

    usuarios = carregar_usuario()
    
    user_adm = str(user).upper().strip()
    limpar_tela()

    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║                Registrar Novo Usuário                  ║
    ╚════════════════════════════════════════════════════════╝
    ''')

    username = input(f"\nDigite o nome do novo usuário\n> ").upper().strip()

    if username in usuarios:
        print(f"Usuário [ {username} ] já existe no banco de dados!")
    else:
        cont = 0
        while cont <= 2:
            senha = pwinput(f"\nDigite a senha para o novo usuário: ", mask="*").strip()
            senha2 = pwinput("Confirme a senha: ", mask="*").strip()
            cont += 1
            if senha == senha2:
                break
            else:
                print(f"\nSenha de confirmação NÃO esta de acordo com a senha descrita!")

    matricula = str(input("Digite a matricula: ").strip())

    result = registrar_usuario(nome_adm= user_adm, username= username, senha= senha, confirmar_senha= senha2, matricula= matricula)
    if result:
        print("Usuario Registrado com sucesso!")
        painel()        
        
def painel_login():
    try:
        limpar_tela()
        menu =  Text.from_markup("""[bold blue]
  
         █░░░ █▀▀█ █▀▀▀ ░▀░ █▀▀▄   █▀▀▄ █▀▀   █░░█ █▀▀ █░░█ █▀▀█ ░▀░ █▀▀█   █▀▄▀█ █▀▀█ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀▄ █▀▀
         █░░░ █░░█ █░▀█ ▀█▀ █░░█   █░░█ █▀▀   █░░█ ▀▀█ █░░█ █▄▄▀ ▀█▀ █░░█   █▒█▒█ █▄▄█ █▄▄▀ ░░█░░ ▀█▀ █░░█ ▀▀█
         █▄▄█ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀░░▀   ▀▀▀░ ▀▀▀   ░▀▀▀ ▀▀▀ ░▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀▀   █░░▒█ ▀░░▀ ▀░▀▀ ░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀

            [/bold blue]""")
        
        print(menu)
        print(Text.from_markup("""

        [bold red]➤[/bold red]  1 • login.
        [bold red]➤[/bold red]  2 • Alterar Senha.
        [bold red]➤[/bold red]  0 • sair.
        """))

        print("Digite o numero da opção desejada:")
        escolha = str(input("> ").strip().lower())

        if escolha == "1":
            cont = 0
            while cont <2:

                print(Rule(style="blue"))

                user = str(input("Usuario: ").strip())
                senha = str(input("Senha: ").strip())

                print(Rule(style="blue"))

                result = validacao_login(user_= user, senha_= senha)
                cont += 1
                sleep(1.3)
                if result:
                    painel(result["usuario"])
                    return result
                    

        if escolha == "2":
            painel_alterar_senha()
    
        if escolha == "0":
            return print("")
        
        if escolha not in ["1", "2"]:
            return painel_login()

        

        
            
    except Exception as erro:
        print(f"[blue red]ocorreu um erro no processo de login[/blue red]: {erro}")

def painel_alterar_senha():


    usuarios = carregar_usuario()
    limpar_tela()
    print(Text.from_markup(f'''
    ╔════════════════════════════════════════════════════════╗
    ║                     Alterar Senha                      ║
    ╚════════════════════════════════════════════════════════╝
    '''))

    username = input(f"\nDigite o nome do usuário\n> ").upper().strip()

    if username not in usuarios:
        print(f"Usuário [ {username} ] Não existe no banco de dados!")
        print("voltando...")
        sleep(0.6)
        painel_login()


    senha_an = str(pwinput("Digite senha antiga: ", mask="*").strip())

    while True:
        senha = pwinput(f"Digite a senha para o novo usuário: ", mask="*").strip()
        senha2 = pwinput("Confirme a senha: ", mask="*").strip()
        if senha == senha2:
            break
        else:
            print(f"\nSenha de confirmação NÃO esta de acordo com a senha descrita!")

    result = alterar_senha(username= username, senha_antiga= senha_an, nova_senha= senha, confirmar_senha= senha2)

    if result:
        print("Senha alterada com sucesso.")
        painel_login()

def menu_config(user: str):

    configuracoes = {
        "1": painel_alterar_registro,
        "2": "",
        "3": "",
        "4": ""
    }
    limpar_tela()

    menu_config = """
        [bold red]➤[/bold red]  1 • Registrar usuarios.
        [bold red]➤[/bold red]  2 • Alterar Permissão.
        [bold red]➤[/bold red]  3 • Deletar usuario.
        [bold red]➤[/bold red]  4 • Alterar senha de usuario.
        [bold red]➤[/bold red]  0 • Voltar.
    """
    
    print(menu_config)
    print("Digite o numero da opção desejada:")
    escolha = str(input("> ").strip().lower())

    if escolha == "0":
            limpar_tela()
            print("Voltando ao Menu...")
            painel()
    username = user
    if escolha in ["1", "2", "3", "4"]: 

        funcao = configuracoes.get(escolha)

        print(f"iniciando a funcao: {funcao.__name__}")

        if funcao.__name__ == "painel_alterar_registro":
            funcao(user=username)    
        funcao()