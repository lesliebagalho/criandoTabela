from datetime import datetime

def limparTela():
    import os
    os.system("cls" if os.name == "nt" else "clear")

usuarios = []
idUsuario = 1
def adicionarUsuario():
    global idUsuario
    print("\nAdicionando novos usuários")
    anoAtual = datetime.now().year
    
    try:
        # idUsuario = int(input("Digite o Id: "))
        nomeUsuario = input("Digite o seu nome: ")
        idadeUsuario = int(input("Digite sua idade: "))
        anoNascimento = anoAtual - idadeUsuario
        
        usuarios.append({
            "Id": idUsuario,
            "Nome": nomeUsuario,
            "Idade": idadeUsuario,
            "Ano de Nascimento": anoNascimento
        })
        idUsuario += 1
        print("Usuário adicionado com sucesso!")
    except ValueError:
        print("Erro: Por favor, insira valores válidos.")
    
    return idUsuario - 1, nomeUsuario, idadeUsuario, anoNascimento

def menuUsuario():
    while True:
        print("[1] Adicionar")
        print("[2] Buscar")
        print("[3] Excluir")
        print("[4] Tabela")
        print("[0] Sair")
        
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            adicionarUsuario()
        elif opcao == 2:
            # buscarusuario()
            pass
        elif opcao == 3:
            # ExcluirUsuario()
            pass
        elif opcao == 4:
            pass
        elif opcao == 0:
            print("Sainddo do cadastro de usuários")
            break
    return

