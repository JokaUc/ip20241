#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
#defq:01
#numero1 = int(input('Digite o primeiro numero: '))
#numero2 = int(input('digite o segundo numero: ')) 
#adição = numero1 + numero2 + 1
#print(adição)

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
#def:02 

#numero1 = int(input('Digite numero1:'))
#numero2 = int(input('Digite numero2:'))
#soma = numero1 + numero2
#if soma > 20:
    #print(f'A soma dos dois numeros é maior que 20 então soam - se com 8 sendo o resultado é: {soma + 8}')
#else:
    #print(f'a soma dos dois  numeros é menor ou igual a 20 então subtrae - se com 5 sendo que o resultado é: {soma - 5}')
#def:03

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#  "É múltiplo de 3"ou "Não é múltiplo de 3".

#def verifica_multiplo_de_tres(numero):
    #if numero % 3 == 0:
        #print("É múltiplo de 3")
    #else:
        #print("Não é múltiplo de 3")

#numero = int(input("Digite um número inteiro: "))
#verifica_multiplo_de_tres(numero)


#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
#def04:
#def verifica_divisibilidade_por_cinco(numero):
    #if numero % 5 == 0:
        #print("É divisível por 5")
    #else:
        #print("Não é divisível por 5")
#numero = int(input("Digite um número inteiro: "))
#verifica_divisibilidade_por_cinco(numero)

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
#def05:
#def verifica_divisibilidade_por_3_e_7(numero):
    #if numero % 3 == 0 and numero % 7 == 0:
        #print("É divisível por 3 e por 7")
    #else:
        #print("Não é divisível por 3 e por 7")
#numero = int(input("Digite um número inteiro: "))
#verifica_divisibilidade_por_3_e_7(numero)

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
#def06:
#def verificar_emprestimo(salario_bruto, prestacao):
    #limite_prestacao = salario_bruto * 0.30
    #if prestacao <= limite_prestacao:
        #print("Empréstimo concedido!")
    #else:
        #print("Empréstimo não pode ser concedido. A prestação excede 30% do salário bruto.")
#salario_bruto = float(input("Digite o salário bruto: "))
#prestacao = float(input("Digite o valor da prestação: "))
#verificar_emprestimo(salario_bruto, prestacao)

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
#def07:
#def verificar_intervalo(numero):
    #if 20 <= numero <= 50:
        #print("O número está compreendido entre 20 e 50.")
    #else:
        #print("O número não está compreendido entre 20 e 50.")
#numero = float(input("Digite um número: "))
#verificar_intervalo(numero)

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
#def compara_numero(numero):
#def08:
    #if numero > 20:
        #print("Maior do que 20")
    #elif numero == 20:
        #print("Igual a 20")
    #else:
        #print("Menor do que 20")
#numero = float(input("Digite um número: "))
#compara_numero(numero)

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.

# dia = int(input('Digite seu dia de nascimento: '))
# mes = int(input('Digite seu mes de nascimento: '))
# ano = int(input('Digite seu ano de nascimento: ')) 

# ano_atual = 2024

# if (ano > ano_atual):
#     print('ano digitado é maios que o ano atual')
# else:
#     idade = ano_atual - ano
#     print(f'A sua idade é {idade}')
 

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.

# primeiro = int(input('Digite primeiro:'))
# segundo = int(input('Digite segundo:'))
# terceiro = int(input('Digite terceiro:'))
# numeros = [primeiro,segundo,terceiro]
# print(numeros)

#11. Faça um programa que leia 3 números e imprima o maior deles.

# numero1 = int(input('Digite numero1:'))
# numero2 = int(input('Digite numero1:'))
# numero3 = int(input('Digite numero1:'))

# print(numero1, numero2, numero3)

# if (numero1 > numero2) and (numero1 > numero3):
#     print(f'{numero1} é maior numero')


# elif (numero2 > numero1) and (numero2 > numero3):
#     print(f'{numero2} é maior numero')

    
# elif (numero3 > numero1) and (numero3 > numero2):
#     print(f'{numero3} é maior numero')


#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos

# idade = int(input('Qual é sua idade:'))

# if(idade > 65):
#     #• Se é maior de 65 anos
#     print('maior que 65 anos ')

# elif (idade >= 18):
#     #• Se é maior de idade
#     print('maior de idade ')

# elif (idade < 18):
#     #• Se é menor de idadea
#     print('menor de idade ')


#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).;

# nome = str(input('Digite seu nome:'))
# print("\n")
# nota1 = float(input('Digite sua nota1:'))
# print("\n")
# nota2 = float(input('Digite sua nota2:'))
# print("\n")
# media = (nota1 + nota2) / 2
# print("\n")
# print(f'{nome}: SUA NOTA DA PROVA1 É : {nota1} SUA NOTA DA PROVA 2 É : {nota2} SUA MEDIA É : {media}')
# print("\n")
# if (media >=7):
#     print("\n")
#     print('APROVADO!!!')
#     print("\n")
# elif(media <= 3):
#     print("\n")
#     print('Reprovado')
#     print("\n")
# else:
    
#     print('REPROVADO!!!')

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

# salario = float(input('Digite seu salario: '))

# if (salario <= 600):

   

# elif (salario > 600) and (salario <= 1200):

#      desconto = salario*20/100

# elif (salario > 1200) and (salario <= 2000):

# elif (salario > 2000): and (salario <= 2000): 


#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.

# produto = float(input('Digite o valor da compra R$:'))

# if 'valor_da_compra' < 20:
#     lucro = 0.45
# else:
#     lucro = 0.30
#     print(f'O valor da compra é ')

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

# idade = int(input('Digite a idade:'))
# if idade <= 5 and idade <=7:
#     print(idade)
# if idade <= 8 and idade <=10:
#     print(idade)
# if idade <= 11 and idade <=13:
#     print(idade)
# if idade <=14 and idade <=17:
#     print(idade)
# if idade >18:
#     print(idade)

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

# nome = str(input('Digite nome:'))
# idade = int(input('Digite idade:'))
# if idade <=10:
#     print(idade)
# if idade <= 29:
#     print(idade)
# if idade <= 45:
#     print(idade)
# if idade <= 59:
#     print (idade)
# if idade <= 65:
#     print(idade)

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

# numero = int(input('Digite numero:'))
# mes = str(input('Digite o mes: ')) 
# meses = numero + mes / 12
# print(meses)

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

# if jogador1 > jogador2 and jogador1  > jogador3:

#     print(f"{jogador1},{jogador2},{jogador3}")

# elif jogador2 > jogador1 and jogador2  > jogador3:

#     print(f"{jogador2},{jogador1},{jogador3}")  

# elif jogador3 > jogador1 and jogador3  > jogador2:

#     print(f"{jogador3},{jogador2},{jogador1}")

# if   jogador1 + jogador2 + jogador3 > 100:

#     soma = jogador1 + jogador2 + jogador3 / 3 

#     print(f"A media aritimetica é {soma}")

# else:

#     print("equipe desclassificada{jogador1},{jogador2},{jogador3}")


#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

# saldo_medio = float(input('Digite saldo medio:')) 

# if saldo_medio >= 0 and saldo_medio <= 500:

#     valor_credito = 0

# elif 501 <= saldo_medio <= 1000:

#     valor_credito = 0.3 

# elif 1001 <= saldo_medio <= 3000:

#     valor_credito = 0.4

# else: 

#     valor_credito = 0.5

# valor_credito = saldo_medio * valor_credito 

# print(f"saldo medio é {saldo_medio}")

# print(f"valor do credito é {valor_credito}")

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

# def imprimir_recibo(nome_livro, tipo_usuario):
#     if tipo_usuario.lower() == "professor":
#         total_dias = 10
#     elif tipo_usuario.lower() == "aluno":
#         total_dias = 3
#     else:
#         print("Tipo de usuário inválido.")
#         return

#     print("\nRecibo:")
#     print("Nome do livro:", nome_livro)
#     print("Tipo de usuário:", tipo_usuario)
#     print("Total de dias para devolução:", total_dias)


# nome_livro = input("Digite o nome do livro: ")
# tipo_usuario = input("Digite o tipo de usuário (professor ou aluno): ")


# imprimir_recibo(nome_livro, tipo_usuario)

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

# def calcular_consumo(percurso, tipo_carro):
#     consumo = 0
#     if tipo_carro.upper() == "A":
#         consumo = percurso / 12
#     elif tipo_carro.upper() == "B":
#         consumo = percurso / 9
#     elif tipo_carro.upper() == "C":
#         consumo = percurso / 8
#     else:
#         print("Tipo de carro inválido.")
#         return

#     return consumo


# percurso_km = float(input("Digite o percurso em quilômetros: "))
# tipo_carro = input("Digite o tipo do carro (A, B ou C): ")


# consumo_estimado = calcular_consumo(percurso_km, tipo_carro)


# if consumo_estimado:
#     print("Consumo estimado de combustível:", consumo_estimado, "litros")

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano 180cal Abacaxi 75cal   Chá 20cal
#Peixe 230cal   Sorvete diet 110cal Suco de laranja 70cal
#Frango 250cal  Mousse diet 170cal  Suco de melão 100cal
#Carne 350cal   Mousse chocolate 200cal Refrigerante diet 65cal


# tabela_calorias = {
#     "Vegetariano": {"prato": 180, "sobremesa": 75, "bebida": 20},
#     "Peixe": {"prato": 230, "sobremesa": 110, "bebida": 70},
#     "Frango": {"prato": 250, "sobremesa": 170, "bebida": 100},
#     "Carne": {"prato": 350, "sobremesa": 200, "bebida": 65}
# }


# prato = input("Escolha o prato (Vegetariano, Peixe, Frango, Carne): ")
# sobremesa = input("Escolha a sobremesa (Abacaxi, Sorvete diet, Mousse diet, Mousse chocolate): ")
# bebida = input("Escolha a bebida (Chá, Suco de laranja, Suco de melão, Refrigerante diet): ")


# if prato in tabela_calorias and sobremesa in tabela_calorias[prato] and bebida in tabela_calorias[prato]:
#     total_calorias = tabela_calorias[prato]["prato"] + tabela_calorias[prato]["sobremesa"] + tabela_calorias[prato]["bebida"]
#     print("A quantidade total de calorias da refeição é:", total_calorias)
# else:
#     print("Opção inválida. Por favor, escolha uma combinação válida de prato, sobremesa e bebida.")


#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

# def obter_mes_renovacao(placa):
#     ultimo_numero = int(placa[-1])
#     meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
#     mes_renovacao = meses[(ultimo_numero - 1) % 12]
#     return mes_renovacao


# placa = input("Digite o número da placa do carro: ")


# if placa.isdigit() and len(placa) == 7:  
#     mes_renovacao = obter_mes_renovacao(placa)
#     print("O emplacamento do carro deve ser renovado em", mes_renovacao)
# else:
#     print("Placa inválida. Por favor, digite a placa corretamente (formato: ABC1D23).")

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos

# def verificar_intimacao(indice):
#     if indice > 0.4:
#         print("Intimação para todas as indústrias dos 1º, 2º e 3º grupos")
#     elif indice > 0.3:
#         print("Intimação para todas as indústrias dos 1º e 2º grupos")
#     elif indice > 0.25:
#         print("Intimação para todas as indústrias do 1º grupo")
#     else:
#         print("Nenhuma intimação necessária")

# indice = float(input("Digite o índice de poluição: "))


# verificar_intimacao(indice)
