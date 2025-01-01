from rich.table import Table
from rich.console import Console
from datetime import datetime

def limparTela():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def menuUsuario():
    while True:
        print("\nMenu:")
        print("[1] Adicionar")
        print("[2] Buscar")
        print("[3] Excluir")
        print("[4] Tabela")
        print("[0] Sair")
        
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            adicionarUsuario()
        elif opcao == 2:
            buscarUsuario(usuarios)
            pass
        elif opcao == 3:
            # ExcluirUsuario()
            pass
        elif opcao == 4:
            exibirTabela()
        elif opcao == 0:
            print("Sainddo do cadastro de usuários")
            break
    return

usuarios = []
idUsuario = 1

# [1] Adicionar usuário
def adicionarUsuario():
    global idUsuario
    print("\nAdicionando usuários")
    anoAtual = datetime.now().year
    
    while True:
        try:
            nomeUsuario = input("Digite o seu nome: ")
            idadeUsuario = int(input("Digite sua idade: "))
            anoNascimento = anoAtual - idadeUsuario
            
            usuarios.append({
                "Id": idUsuario,
                "Nome": nomeUsuario,
                "Idade": idadeUsuario,
                "Ano de Nascimento": anoNascimento
            })
            print(f"Usuário {nomeUsuario} adicionado com sucesso!")
            print(f"Id: {idUsuario}, Nome: {nomeUsuario}, Idade: {idadeUsuario}")
            idUsuario += 1
            break
            
        except ValueError:
            print("Erro: Por favor, insira valores válidos.")
        
        return idUsuario - 1, nomeUsuario, idadeUsuario, anoNascimento

# [2] Buscar usuário
def buscarUsuario(usuarios):
    print("\nUsuário(s) encontrado(s):")
    for usuario in usuarios:
        print(f"{usuario['Nome']}")
        
    nomeBusca = input("\nDigite o nome do usuário para buscar: ")
    if not nomeBusca.strip():
        print("Você não digitou um nome válido. Tente novamente.\n")
        return
    
    console = Console()
    table = Table(title="Resultado da Busca")
    table.add_column("Id", justify="right", style="cyan", no_wrap=True)
    table.add_column("Nome", style="magenta")
    table.add_column("Idade", justify="right", style="green")
    table.add_column("Ano de Nascimneto", justify="right", style="yellow")
    
    usuarioEncontrado = False
    for usuario in usuarios:
        if usuario["Nome"].lower() == nomeBusca.lower():
            table.add_row(
                str(usuario["Id"]),
                usuario["Nome"],
                str(usuario["Idade"]),
                str(usuario["Ano de Nascimento"]),
            )
            usuarioEncontrado = True
    
    if usuarioEncontrado:
        console.print(table)
    else:
        print("Usuário não encontrado")
    
# [4] Exibir tabela
def exibirTabela():
    console = Console()
    table = Table(title="Cadastro de Usuários")
    table.add_column("Id", justify="right", style="cyan", no_wrap=True)
    table.add_column("Nome", style="magenta")
    table.add_column("Idade", justify="right", style="green")
    table.add_column("Ano Nascimneto", justify="right", style="yellow")
    
    for usuario in usuarios:
        table.add_row(str(usuario["Id"]), usuario["Nome"], str(usuario["Idade"]), str(usuario["Ano de Nascimento"]))
    
    console.print(table)


