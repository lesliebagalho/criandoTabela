from rich.table import Table
from rich.console import Console
from datetime import datetime
from function import menuUsuario, limparTela, adicionarUsuario

limparTela()
print()

console = Console()
table = Table(title="Cadastro de Usuários")

table.add_column("Id", justify="right", style="cyan", no_wrap=True)
table.add_column("Nome", style="magenta")
table.add_column("Idade", justify="right", style="green")
table.add_column("Ano Nascimneto", justify="right", style="yellow")

print()

while True:
    idUsuario, nomeUsuario, idadeUsuario, anoNascimento = adicionarUsuario()
    table.add_row(str(idUsuario), nomeUsuario, str(idadeUsuario), str(anoNascimento))
    break

console.print(table)

print("\nDeseja adicionar outro usuário? ")
menuUsuario()
