dinossauros = {}

def criar_dino():
    nome = input("Nome do dinossauro: ")
    if nome in dinossauros:
        print("Dinossauro já cadastrado.")
        return
    especie = input("Espécie do dinossauro: ")
    dinossauros[nome] = {"especie": especie, "saldo": 0.0}
    print(f"Conta criada para {nome} ({especie}) com saldo 0.0")

def depositar():
    nome = input("Nome do dinossauro: ")
    if nome not in dinossauros:
        print("Dinossauro não encontrado.")
        return
    valor = float(input("Valor a depositar: "))
    if valor <= 0:
        print("Valor inválido.")
        return
    dinossauros[nome]["saldo"] += valor
    print(f"Depósito de {valor} realizado. Novo saldo de {nome}: {dinossauros[nome]['saldo']}")

def sacar():
    nome = input("Nome do dinossauro: ")
    if nome not in dinossauros:
        print("Dinossauro não encontrado.")
        return
    valor = float(input("Valor a sacar: "))
    if valor <= 0 or valor > dinossauros[nome]["saldo"]:
        print("Saldo insuficiente.")
        return
    dinossauros[nome]["saldo"] -= valor
    print(f"Saque de {valor} realizado. Novo saldo de {nome}: {dinossauros[nome]['saldo']}")

def exibir_saldo():
    nome = input("Nome do dinossauro: ")
    if nome not in dinossauros:
        print("Dinossauro não encontrado.")
        return
    dados = dinossauros[nome]
    print(f"Saldo de {nome} ({dados['especie']}): {dados['saldo']}")

def listar_dinossauros():
    if not dinossauros:
        print("Nenhum dinossauro cadastrado.")
        return
    for nome, dados in dinossauros.items():
        print(f"- {nome} ({dados['especie']}): Saldo {dados['saldo']}")

def menu():
    while True:
        print("\n=== Sistema Bancário de Dinossauros ===")
        print("1. Criar conta de dinossauro")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Exibir saldo")
        print("5. Listar dinossauros")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            criar_dino()
        elif escolha == '2':
            depositar()
        elif escolha == '3':
            sacar()
        elif escolha == '4':
            exibir_saldo()
        elif escolha == '5':
            listar_dinossauros()
        elif escolha == '6':
            print("Saindo do sistema bancário.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()