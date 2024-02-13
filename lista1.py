
#print("---------------------------------exe 1---------------------------------------------")
#1. Faça um programa que imprima o seu nome.
#print("\n")
#nome = str(input ('DIGITE SEU NOME: '))
#print(nome)

#print("\n")

#print("-------------------------------exe 2-----------------------------------------------")
#2. Faça um programa que imprima o produto dos valores 30 e 27.
#print("\n")
#valor1 = int(input ('DIGITE O PRIMEIRO NUMERO: '))
#valor2 = int(input ('DIGITE O SEGUNDO NUMERO: '))
#produto = (valor1 * valor2)
#print(f'O valor do produto é: {produto}')

#print("\n")

#print("--------------------------------exe 3------------------------------------------")
#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
#valor1 = int(input ('DIGITE O PRIMEIRO NUMERO: '))
#valor2 = int(input ('DIGITE O SEGUNDO NUMERO: '))
#valor3 = int(input ('DIGITE O TERCEIRO NUMERO: '))
#media = ((valor1 + valor2 + valor3)/3)
#print("\n")
#print(f'a media entre os 3 numeros é: {media}')

#print("\n")

#print("----------------------------------------exe 4--------------------------------------")
#4. Faça um programa que leia e imprima um número inteiro.
#numero = int(input ('DIGITE UM NUMERO INTEIRO: '))
#print(f'o numero inteiro digitado é: {numero}')

#print("\n")

#print("------------------------------------exe 5------------------------------------------")
#5. Faça um programa que leia dois números reais e os imprima.
#num1 = input('digite num1: ')
#num2 = input('digite num2: ')
#print(num1)
#print(num2)

#print("\n")

#print("-------------------------------------------exe 6-----------------------------------")
#6. Faça um programa que leia um número inteiro e imprima o seu
#antecessor e o seu sucessor.
#print("\n")
#num = int(input('digite um numero:'))
#num_suc = num + 1
#num_ant = num - 1
#print('o numero informado foi {} seu sucessor e {} e seu antecessor e {}'.format(num,num_suc,num_ant))

#print("\n")

#print("--------------------------------------exe 7----------------------------------------")
#7. Faça um programa que leia o nome o endereço e o telefone de
#um cliente e ao final, imprima esses dados.
#nome = input(str('digite seu nome:' ))
#endereço = input(str('digite seu endereço:'))
#telefone = input(str('digite seu nome:'))
#print(nome)
#print(endereço)
#print(telefone)

#print("\n")

#print("--------------------------------------exe 9----------------------------------------")
#8. Faça um programa que leia dois números inteiros e imprima a
#subtração deles.
#print("\n")
#numero1 = int(input('digite numero1: '))
#numero2 = int(input('digite numero2: '))
#print(+numero1 - numero2)

#print("\n")

#print("--------------------------------------exe 10----------------------------------------")
#9. Faça um programa que leia um número real e imprima ¼ deste número.
#print("--------------------------------------exe 10----------------------------------------")
#10. Faça um programa que leia três números reais e calcule a
#média aritmética destes números. Ao final, o programa deve
#imprimir o resultado do cálculo.

#print("\n")

#numero1 = float(input('digite num1: '))
#numero2 = float(input('digite num2: '))
#numero3 = float(input('digite num3: '))
#print(numero1 + numero2 + numero3)/3
  #print("--------------------------------------exe 10----------------------------------------")
#11. Faça um programa que leia dois números reais e calcule as
#quatro operações básicas entre estes dois números, adição,
#subtração,multiplicação e divisão. Ao final, o programa
#deve imprimir os resultados dos cálculos

#print("\n")

#numero1 = float(input('digite num1: '))
#numero2 = float(input('digite num2: '))
#soma = numero1 + numero2 
#print("a soma é:" ,soma)
#subtração = numero1 - numero2
#print("a subtração é:" ,subtração)
#divisão = numero1 / numero2
#print("a divisão é:" ,divisão)
#multiplicação = numero1 * numero2
#print("a multiplicação é:" ,multiplicação)

#print("\n")

#print("--------------------------------------exe 10----------------------------------------")
#12. Faça um programa que leia um número real e calcule o
#quadrado deste número. Ao final, o programa deve
#imprimir o resultado do cálculo.

#print("\n")

#def calcular_quadrado(numero):
    #return numero ** 2

#numero = float(input("Digite um número: "))
#quadrado = calcular_quadrado(numero)
#print("O quadrado de", numero, "é", quadrado)

#print("\n")

  #print("--------------------------------------exe 10----------------------------------------")
#13. Faça um programa que leia o saldo de uma conta poupança e
#imprima o novo saldo, considerando um reajuste de 2%.

#print("\n")

#def calcular_novo_saldo(saldo):
#reajuste = saldo * 0.02
#novo_saldo = saldo + reajuste
#return novo_saldo

#saldo_atual = float(input("Digite o saldo atual da conta poupança: "))
#novo_saldo = calcular_novo_saldo(saldo_atual)

#print("O novo saldo após o reajuste de 2% é:", novo_saldo)

#print("\n")

#print("--------------------------------------exe 10----------------------------------------")
#14. Faça um programa que leia a base e a altura de um retângulo
# e imprima o perímetro (base + altura) e a área (base * altura).
#def calcular_perimetro(base, altura):
    #return 2 * (base + altura)

#def calcular_area(base, altura):
    #return base * altura

#def main():
    #base = float(input("Digite a medida da base do retângulo: "))
    #altura = float(input("Digite a medida da altura do retângulo: "))

    #perimetro = calcular_perimetro(base, altura)
    #area = calcular_area(base, altura)

    #print("O perímetro do retângulo é:", perimetro)
    #print("A área do retângulo é:", area)

#if __name__ == "__main__":
    #main(

      #print("\n")

#print("--------------------------------------exe 10----------------------------------------")
#15. Faça um programa que leia o valor de um produto, o percentual
#do desconto desejado e imprima o valor do desconto e o valor
#do produto subtraindo o desconto.
#def calcular_desconto(valor_produto, percentual_desconto):
    #desconto = valor_produto * (percentual_desconto / 100)
    #return desconto

#def main():
    #valor_produto = float(input("Digite o valor do produto: "))
    #percentual_desconto = float(input("Digite o percentual de desconto desejado: "))

    #desconto = calcular_desconto(valor_produto, percentual_desconto)
    #valor_com_desconto = valor_produto - desconto

    #print("O valor do desconto é: R$", desconto)
    #print("O valor do produto com desconto é: R$", valor_com_desconto)

#if __name__ == "__main__":
    #main()

    #print("\n")
  
#print("--------------------------------------exe 10----------------------------------------")
#16. Faça um programa que calcule o reajuste do salário de um
#funcionário. Para isso, o programa deverá ler o salário atual
#do funcionário e ler o percentual de reajuste. Ao final imprimir
#o valor do novo salário.
#def calcular_novo_salario(salario_atual, percentual_reajuste):
    #novo_salario = salario_atual * (1 + percentual_reajuste / 100)
    #return novo_salario

#def main():
    #salario_atual = float(input("Digite o salário atual do funcionário: "))
    #percentual_reajuste = float(input("Digite o percentual de reajuste do salário: "))

    #novo_salario = calcular_novo_salario(salario_atual, percentual_reajuste)

    #print("O novo salário do funcionário é: R$", novo_salario)

#if __name__ == "__main__":
    #main()

     #print("\n")


#print("--------------------------------------exe 10----------------------------------------")
#17. Faça um programa que calcule a conversão entre graus centígrados
#e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#com base na fórmula a seguir. Após calcular o programa deve
#imprimir o resultado da conversão.
#F = (9 x C + 160) / 5
#def converter_para_fahrenheit(celsius):
    #fahrenheit = (9 * celsius + 160) / 5
    #return fahrenheit

#def main():
    #celsius = float(input("Digite a temperatura em graus Celsius: "))
    
    #fahrenheit = converter_para_fahrenheit(celsius)
    
    #print("A temperatura em Fahrenheit é:", fahrenheit)

#if __name__ == "__main__":
    #main()

    #print("\n")
    
  #print("--------------------------------------exe 10----------------------------------------")
#18. Faça um programa que calcule a quantidade de litros de combustível
#consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#12 km por litro de combustível. O programa deverá ler o tempo
#decorrido na viagem e a velocidade média e aplicar as fórmulas:
#D = T x V       L = D / 12
#Em que:
#• D = Distância percorrida em horas
#• T = Tempo
#• V = Velocidade média
#• L = Litros de combustível consumidos
# Ao final, o programa deverá imprimir a distância percorrida e a
#quantidade de litros consumidos na viagem.
#def calcular_litros_consumidos(tempo, velocidade_media):
    #distancia_percorrida = tempo * velocidade_media
    #litros_consumidos = distancia_percorrida / 12
    #return distancia_percorrida, litros_consumidos

#def main():
    #tempo = float(input("Digite o tempo decorrido na viagem (em horas): "))
    #velocidade_media = float(input("Digite a velocidade média durante a viagem (em km/h): "))

    #distancia_percorrida, litros_consumidos = calcular_litros_consumidos(tempo, velocidade_media)

    #print("Distância percorrida na viagem:", distancia_percorrida, "km")
    #print("Quantidade de litros consumidos na viagem:", litros_consumidos, "litros")

#if __name__ == "__main__":
    #main()

#print("\n")

#print("--------------------------------------exe 10----------------------------------------")
#19. Faça um programa que calcule o valor de uma prestação em atraso.
#Para isso, o programa deve ler o valor da prestação vencida, a
#taxa periódica de juros e o período de atraso. Ao final, o
#programa deve imprimir o valor da prestação atrasada, o período
#de atraso, os juros que serão cobrados pelo período de atraso, o
#valor da prestação acrescido dos juros. Considere juros simples.
#def calcular_prestacao_atrasada(valor_prestacao_vencida, taxa_juros, periodo_atraso):
    #juros = valor_prestacao_vencida * (taxa_juros / 100) * periodo_atraso
    #valor_prestacao_atrasada = valor_prestacao_vencida + juros
    #return juros, valor_prestacao_atrasada

#def main():
    #valor_prestacao_vencida = float(input("Digite o valor da prestação vencida: "))
    #taxa_juros = float(input("Digite a taxa periódica de juros (%): "))
    #periodo_atraso = int(input("Digite o período de atraso (em meses): "))

    #juros, valor_prestacao_atrasada = calcular_prestacao_atrasada(valor_prestacao_vencida, taxa_juros, periodo_atraso)

    #print("Valor da prestação atrasada:", valor_prestacao_atrasada)
    #print("Período de atraso:", periodo_atraso, "meses")
    #print("Juros cobrados pelo período de atraso:", juros)
    #print("Valor da prestação acrescido dos juros:", valor_prestacao_atrasada)

#if __name__ == "__main__":
    #main()

    #print("\n")

#print("--------------------------------------exe 10----------------------------------------")
#20. Faça um programa que efetue a apresentação do valor da conversão
#em real (R$) de um valor lido em dólar (US$). Para isso, será
#necessário também ler o valor da cotação do dólar.
#def converter_dolar_para_real(valor_dolar, cotacao_dolar):
    #valor_real = valor_dolar * cotacao_dolar
    #return valor_real

#def main():
    #valor_dolar = float(input("Digite o valor em dólar (US$): "))
    #cotacao_dolar = float(input("Digite a cotação do dólar (R$/US$): "))

    #valor_real = converter_dolar_para_real(valor_dolar, cotacao_dolar)

    #print("O valor em reais (R$) é:", valor_real)

#if __name__ == "__main__":
    #main()

#print("\n")











  






