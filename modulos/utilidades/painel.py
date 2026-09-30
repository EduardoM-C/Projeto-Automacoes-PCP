from rich import print
from rich.text import Text

from utilidades.automacao.exportar_rastreabilidade import automacao_rastreabilidade
from utilidades.automacao.exportar_automacao_ressuprimento import automacao_ressuprimento
from utilidades.automacao.exportar_automacao_pendencias import automacao_pendencia
from utilidades.defs import limpar_tela


def painel(user: str = ""):

    automacoes = {
        "1": automacao_pendencia,
        "2": automacao_rastreabilidade,
        "3": automacao_ressuprimento,
    }


    try:
        while True:

            limpar_tela()


            # Removidos os espaços de indentação da string para não quebrar no terminal
            menu = """
            [blue]╔════════════════════════════════════════════════════════════════════════════════╗[/blue]
            [blue]║[/blue]                                [bold green]Sistema Automações[/bold green]                              [blue]║[/blue]
            [blue]╠════════════════════════════════════════════════════════════════════════════════╣[/blue]
            [blue]║[/blue]    [bold green]Automatização WMS - KORBER,  PCP - Planejamento e Controle da Produção[/bold green]      [blue]║[/blue]
            [blue]╚════════════════════════════════════════════════════════════════════════════════╝[/blue]"""

            # Converte a marcação de cor mantendo o texto bruto
            m_menu = Text.from_markup(menu)
            print(m_menu)

            menu = """
                [bold red]➤[/bold red]  1 • Exportar Pendencias.
                [bold red]➤[/bold red]  2 • Exportar Rastreabilidade.
                [bold red]➤[/bold red]  3 • Exportar Ressuprimento.
                [bold red]➤[/bold red]  4 • Configuraçôes.
                [bold red]➤[/bold red]  0 • Voltar.
                [bold red]➤[/bold red]  exit • Sair.

            """
            print(Text.from_markup(menu))

            print("Digite o numero da opção desejada:")
            escolha = str(input("> ").strip().lower())

            if escolha == "0":
                 limpar_tela()
                 from main import main
                 return print("Voltando a tela de login..."), main()
                 
            
            if escolha == "exit":
                 print("saindo...")
                 break
            
            if escolha == "4":
                from utilidades.painel_login import menu_config
                username = user
                menu_config(user = username)
                break

            if escolha in ["1", "2", "3"]: 
                funcao = automacoes.get(escolha)
                print(f"iniciando a funcao: {funcao.__name__}")
                funcao()
            



    except Exception as erro:
        print(f"Erro {erro}")

