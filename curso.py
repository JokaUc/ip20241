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
# import json
# from colorama import Fore, Style, init

# # Inicializa o Colorama
# init(autoreset=True)

# equipamentos = []

# def estilizar_texto(cor, texto):
#     """Função auxiliar para estilizar o texto com uma cor."""
#     return f"{cor}{texto}{Style.RESET_ALL}"

# def cadastrar_equipamento():
#     """Função para cadastrar um novo equipamento."""
#     nome = input(estilizar_texto(Fore.BLUE, "Digite o nome do equipamento: "))
#     tipo = input("Digite o tipo de equipamento (Computador, Dispositivo de Rede, etc.): ")
#     descricao = input("Digite uma breve descrição do equipamento: ")
    
#     if not nome or not tipo or not descricao:
#         print(estilizar_texto(Fore.RED, "Todos os campos devem ser preenchidos."))
#         return

#     for equipamento in equipamentos:
#         if equipamento["nome"].lower() == nome.lower():
#             print(estilizar_texto(Fore.RED, "Equipamento já cadastrado."))
#             return

#     equipamento = {
#         "nome": nome,
#         "tipo": tipo,
#         "descricao": descricao
#     }
#     equipamentos.append(equipamento)
#     salvar_equipamentos()
#     print(estilizar_texto(Fore.GREEN, "Equipamento cadastrado com sucesso!"))

# def buscar_equipamento():
#     """Função para buscar um equipamento pelo nome."""
#     nome = input("Digite o nome do equipamento que deseja buscar: ")
#     for equipamento in equipamentos:
#         if equipamento["nome"].lower() == nome.lower():
#             print(estilizar_texto(Fore.CYAN, f"Nome: {equipamento['nome']}"))
#             print(f"Tipo: {equipamento['tipo']}")
#             print(f"Descrição: {equipamento['descricao']}")
#             return
#     print(estilizar_texto(Fore.RED, "Equipamento não encontrado."))

# def editar_equipamento():
#     """Função para editar um equipamento existente."""
#     nome = input("Digite o nome do equipamento que deseja editar: ")
#     for equipamento in equipamentos:
#         if equipamento["nome"].lower() == nome.lower():
#             print(estilizar_texto(Fore.YELLOW, "Deixe o campo vazio para manter o valor atual."))
#             novo_nome = input(f"Novo nome (atual: {equipamento['nome']}): ")
#             novo_tipo = input(f"Novo tipo (atual: {equipamento['tipo']}): ")
#             nova_descricao = input(f"Nova descrição (atual: {equipamento['descricao']}): ")

#             if novo_nome:
#                 equipamento["nome"] = novo_nome
#             if novo_tipo:
#                 equipamento["tipo"] = novo_tipo
#             if nova_descricao:
#                 equipamento["descricao"] = nova_descricao

#             salvar_equipamentos()
#             print(estilizar_texto(Fore.GREEN, "Equipamento atualizado com sucesso!"))
#             return

#     print(estilizar_texto(Fore.RED, "Equipamento não encontrado."))

# def excluir_equipamento():
#     """Função para excluir um equipamento existente."""
#     nome = input("Digite o nome do equipamento que deseja excluir: ")
#     global equipamentos
#     equipamentos = [e for e in equipamentos if e["nome"].lower() != nome.lower()]
#     salvar_equipamentos()
#     print(estilizar_texto(Fore.GREEN, "Equipamento excluído com sucesso!"))

# def gerar_relatorio():
#     """Função para gerar um relatório de todos os equipamentos cadastrados."""
#     if not equipamentos:
#         print(estilizar_texto(Fore.YELLOW, "Nenhum equipamento cadastrado."))
#     else:
#         print(estilizar_texto(Fore.BLUE, "\nRelatório de Equipamentos"))
#         print("-" * 30)
#         for equipamento in equipamentos:
#             print(estilizar_texto(Fore.CYAN, f"Nome: {equipamento['nome']}"))
#             print(f"Tipo: {equipamento['tipo']}")
#             print(f"Descrição: {equipamento['descricao']}")
#             print("-" * 30)

# def salvar_equipamentos():
#     """Função para salvar a lista de equipamentos em um arquivo JSON."""
#     with open("equipamentos.json", "w") as arquivo:
#         json.dump(equipamentos, arquivo, indent=4)

# def carregar_equipamentos():
#     """Função para carregar a lista de equipamentos de um arquivo JSON."""
#     global equipamentos
#     try:
#         with open("equipamentos.json", "r") as arquivo:
#             equipamentos = json.load(arquivo)
#     except FileNotFoundError:
#         equipamentos = []

# def menu():
#     """Função para exibir o menu e processar a escolha do usuário."""
#     carregar_equipamentos()
    
#     while True:
#         print(estilizar_texto(Fore.BLUE, "\n1. Cadastrar Equipamento"))
#         print("2. Buscar Equipamento")
#         print("3. Editar Equipamento")
#         print("4. Excluir Equipamento")
#         print("5. Gerar Relatório")
#         print("6. Sair")
#         opcao = input("Escolha uma opção: ")

#         if opcao == "1":
#             cadastrar_equipamento()
#         elif opcao == "2":
#             buscar_equipamento()
#         elif opcao == "3":
#             editar_equipamento()
#         elif opcao == "4":
#             excluir_equipamento()
#         elif opcao == "5":
#             gerar_relatorio()
#         elif opcao == "6":
#             print(estilizar_texto(Fore.RED, "Programa Encerrado!!!"))
#             break
#         else:
#             print(estilizar_texto(Fore.RED, "Opção inválida. Tente novamente."))

# # Executa o menu principal
# menu()




    






