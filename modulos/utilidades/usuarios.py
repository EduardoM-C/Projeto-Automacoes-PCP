import json
from pathlib import Path
import bcrypt
from utilidades.defs import mostrar_mensagem
import sys



if getattr(sys, "frozen", False):
    # Executando como .exe
    CAMINHO = Path(sys.executable).resolve().parent
else:
    CAMINHO = Path(__file__).resolve().parent.parent.parent

CAMINHO_USUARIOS = CAMINHO/"usuarios.json"


# ==========================
# CARREGAR USUÁRIOS
# ==========================

def carregar_usuario():

    try:
        with open(
            CAMINHO_USUARIOS,
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(arquivo)

    except FileNotFoundError:

        return {}



# ==========================
# SALVAR USUÁRIOS
# ==========================

def salvar_usuario(usuarios):

    with open(
        CAMINHO_USUARIOS,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            usuarios,
            arquivo,
            indent=4,
            ensure_ascii=False
        )



# ==========================
# LOGIN
# ==========================

def validar_login(username: str, senha: str):

    usuarios = carregar_usuario()
    
    if not usuarios:
        print("Json usuarios vazio")

    username = str(username).upper().strip()
    senha = str(senha).strip()
    if username not in usuarios:
        return None

    dados = usuarios[username]

    senha_valida = bcrypt.checkpw(
        senha.encode("utf-8"),
        dados["senha"].encode("utf-8")
    )

    if not senha_valida:
        return None

    return {
        "usuario": username,
        "matricula": dados["matricula"],
        "permissao": dados["permissao"]
    }



# ==========================
# CADASTRAR USUÁRIO
# ==========================

def registrar_usuario(nome_adm,
        username: str,
        senha: str,
        confirmar_senha: str,
        matricula: str,
        permissao: str = "usuario"
):

    usuarios = carregar_usuario()


    username = str(username).upper()
    nome_adm = str(nome_adm).upper()
    senha = str(senha)
    confirmar_senha = str(confirmar_senha)
    matricula = str(matricula)


    if username in usuarios:
        return False, mostrar_mensagem(erro="Error", mensagem= "Usuário já existe!")


    if senha != confirmar_senha:
        return False, mostrar_mensagem(erro="Error", mensagem= "As senhas não conferem!")


    senha_hash = bcrypt.hashpw(
        senha.encode("utf-8"),
        bcrypt.gensalt()
    )

    dados_adm = usuarios[nome_adm]

    if dados_adm["permissao"] != "ADM":
        return False, mostrar_mensagem(erro="Error", mensagem= "Sem permissao Para tal tarefa")
     

    usuarios[username] = {

        "senha": senha_hash.decode("utf-8"),

        "matricula": matricula,

        "permissao": permissao
    }

    salvar_usuario(usuarios)


    return True


# ==========================
# ALTERAR SENHA
# ==========================

def alterar_senha(
        username: str,
        senha_antiga: str,
        nova_senha: str,
        confirmar_senha: str):

    usuarios = carregar_usuario()

    username = str(username).upper()
    senha_antiga = str(senha_antiga)
    nova_senha = str(nova_senha)
    confirmar_senha = str(confirmar_senha)

    if username not in usuarios:
        return False, "Usuário não encontrado!"

    dados = usuarios[username]

    # Verifica se a senha antiga está correta
    if not bcrypt.checkpw(
        senha_antiga.encode("utf-8"),
        dados["senha"].encode("utf-8")  # se estiver salva como str
    ):
        return False, "Senha anterior incorreta!"

    if nova_senha != confirmar_senha:
        return False, "As senhas não conferem!"

    # Gera o novo hash
    senha_hash = bcrypt.hashpw(
        nova_senha.encode("utf-8"),
        bcrypt.gensalt()
    )

    # Salva como texto para o JSON
    usuarios[username]["senha"] = senha_hash.decode("utf-8")

    salvar_usuario(usuarios)

    return True, "Senha alterada com sucesso!"


# ==========================
# REMOVER USUÁRIO
# ==========================

def remover_usuario(nome_adm, username):

    usuarios = carregar_usuario()



    nome_adm = str(nome_adm).upper()
    usuario = str(username).upper()

    dados_adm = usuarios[nome_adm]
    dados_user = usuarios[usuario]

    if usuario not in usuarios:
        return False, mostrar_mensagem(erro="Error", mensagem= "Usuário não encontrado!")

    if dados_adm["permissao"] != "ADM":
        return False, mostrar_mensagem(erro="Error", mensagem= "Sem permissao !!")

    if dados_user["permissao"] == "ADM":
        return False, mostrar_mensagem(erro="Error", mensagem= "Sem permissao !!")


    del usuarios[username]


    salvar_usuario(usuarios)


    return True, mostrar_mensagem(erro="Sucess", mensagem= "Usuário removido!")



# ==========================
# LISTAR USUÁRIOS
# ==========================

def listar_usuarios():

    usuarios = carregar_usuario()

    return usuarios
