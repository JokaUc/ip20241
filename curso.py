#nome = input('Qual é o seu nome?')
#print('olá prazer em conhecer você !',nome)
#(----------------------------------------------------------)
#dia = input('Que dia você nasceu ?')
#print("\n")
#mes = input('Qual mês você nasceu ?')
#print("\n")
#ano = input('Qual ano você nasceu ?')
#print("\n")
#print('você nasceu' ,dia ,mes,ano ,'correto!')
#(-----------------------------------------------------------)
#numero1 = int(input ('Digite numero1: '))
#print("\n")
#numero2 = int(input ('Digite numero2: '))
#print("\n")
#print('A soma  dos  numeros é: ' ,numero1 + numero2 )
#print("\n")
#(-------------------------------------------------------------)
#tempo=int(input('Quantos anos tem seu carro?'))
#if tempo <=3:
    #print('Carro novo')
#else:
    #print('Carro velho') 
#(--------------------------------------------------------------)
#print('--FIM--') 
#numero1 = int(input('Digite numeoro 1:'))
#numero2 = int(input('Digite numeoro 2:'))
#soma = numero1 + numero2
#print('A soma entre {} e {} vale: {}' .format(numero1, numero2, soma ))

# nome = "lucas"
# idade = "29"
# sexo = "masculino"

# print(f"Olá seja bem vindo: {nome}\n Sua idade é: {idade}\n E seu sexo é: {sexo}\n Está coreto?\n")

# dia = int(input("Digite o dia:"))
# print(dia)

# match  dia:
#     case 1:
#         print("Domigo")
#     case 2:
#         print("Segunda")
#     case 3:
#         print("Terça")
#     case 4:
#         print("Quarta")
#     case 5:
#         print("Quinta")
#     case 5:
#         print("Sexta")
#     case 6:
#         print("Dia invalido")
    
    # Gestão de Equipamentos: Computadores, Dispositivos de Rede
from colorama import Fore, Style, init
equipamentos = []

def cadastrar_equipamento():
    nome = input("Digite o nome do equipamento: ")
    tipo = input("Digite o tipo de equipamento (Computador, Dispositivo de Rede, etc.): ")
    descricao = input("Digite uma breve descrição do equipamento: ")
    equipamento = {
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao
    }
    equipamentos.append(equipamento)
    print("Equipamento cadastrado com sucesso!")

def buscar_equipamento():
    nome = input(Fore.BLUE +"Digite o nome do equipamento que deseja buscar: ")
    for equipamento in equipamentos:
        if equipamento["nome"].lower() == nome.lower():
            print(f"Nome: {equipamento['nome']}")
            print(f"Tipo: {equipamento['tipo']}")
            print(f"Descrição: {equipamento['descricao']}")
            return
    print("Equipamento não encontrado.")

def gerar_relatorio():
    if not equipamentos:
        print("Nenhum equipamento cadastrado.")
    else:
        print("\nRelatório de Equipamentos")
        print("-" * 30)
        for equipamento in equipamentos:
            print(f"Nome: {equipamento['nome']}")
            print(f"Tipo: {equipamento['tipo']}")
            print(f"Descrição: {equipamento['descricao']}")
            print("-" * 30)

def menu():
    while True:
        print("\n1. Cadastrar Equipamento")
        print("2. Buscar Equipamento")
        print("3. Gerar Relatório")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_equipamento()
        elif opcao == "2":
            buscar_equipamento()
        elif opcao == "3":
            gerar_relatorio()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu principal
menu()





    






