
#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
# def q01():
#     lista = []
#     for x in range(15):
#         lista.append(random.randrange(100))
#     print(lista)
#     busca = int(input('Digite um número a ser localizado: '))
#     try:
#         posicao = lista.index(busca)
#         print(f'Posição do número {busca}: {posicao}')
#     except ValueError:
#         print(f'Valor {busca} não existe na lista!')

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada.
# def q02():
#     lista = []
#     i = 0
#     for x in range(10):
#         lista.append(chr(random.randrange(65,91))) # ord() é o inverso de chr()
#         print(f'{i}: {lista[i]}')
#         i+=1


#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
# def q03():
#     lista = []
#     for x in range(15):
#         lista.append(random.randrange(100))
#     i = 0
#     for n in lista:
#         print(f'{i+1}: {n} é {"PAR" if n%2==0 else "IMPAR"}')
#         i+=1
#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.


#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
# def q05():
#     alunos = []
#     for x in range(3):
#         aluno = dict()
#         aluno['nome'] = input('Nome: ')
#         aluno['n1'] = float(input('Nota 1: '))
#         aluno['n2'] = float(input('Nota 2: '))
#         aluno['media'] = (aluno['n1'] + aluno['n2']) / 2
#         aluno['situacao'] = 'APROVADO' if aluno['media']>=6 else 'REPROVADO'
#         alunos.append(aluno)
#     print('NOME\tN1\tN2\tMEDIA\tSITUACAO')
#     for a in alunos:
#         print(f'{a["nome"]}\t{a["n1"]}\t{a["n2"]}\t{a["media"]}\t{a["situacao"]}')
# q05()

#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
# def q06():
#     salario = []
#     for x in range(20):
#         salario = dict()
#         salario['nome'] = input ('nome:')
#         salario['n1'] =  float(input('Salario1:  '))
#         salario['n2'] =  float(input('Salario2:  '))

#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%
# def q06():
#     pessoas = []
#     for _ in range(3):
#         pessoa = dict()
#         pessoa['nome'] = input('Nome: ')
#         pessoa['salario'] = float(input('Salário: '))
#         pessoa['salario_novo'] = pessoa['salario'] * 1.08
#         pessoas.append(pessoa)
    
#     print('NOME\tSAL\t\tSAL_NOVO')
#     for p in pessoas:
#         print(f'{p["nome"]}\tR$ {p["salario"]}\tR$ {p["salario_novo"]}')
# q06()
 
#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.

# codigo = int(input("Digite o codigo:"))
# valor_venda = int(input("valor venda:"))
# valor_compra = int(input("valor compra:"))
# for x in range(30):
#     print(codigo,valor_venda,valor_compra)

#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.

# numero1 = int(input("Digite numero1"))
# numero2 = int(input("Digite numero2"))
# for x in range(10):
#     print(numero1,numero2)

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

# lista = int(input("Digite o valor:"))
# elementos = int(input("Digite o valor:"))
# for x in range(10):
#     print(lista,elementos)


#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

media = int(input("Digite o valor:"))
valor = int(input("Digite o valor:"))
elementos = int(input("Digite um valor:"))for x in range:(10)
print(media,valor,elementos)



#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.