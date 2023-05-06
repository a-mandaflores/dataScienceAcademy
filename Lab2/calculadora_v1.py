# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!
import math

print("\n******************* Calculadora em Python *******************")


selecionar = int(input('Selecione a opção desejada \n\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n\n\nSelecione a opção desejada (1 - 2 - 3 - 4)'))

def soma(a, b):
    som = a + b
    return som

def subtracao(a, b):
    sub = a - b
    return sub

def divisao(a, b):
    div = a / b
    return div

def multiplicacao(a, b):
    mult = a * b
    return mult

if selecionar == 1:
    primeiro = float(input('Qual o primeiro numero: '))
    segundo = float(input('Qual o primeiro segundo: '))
    result = soma(primeiro, segundo)
    print(f'{primeiro} + {segundo} = {result}')
elif selecionar == 2:
    primeiro = float(input('Qual o primeiro numero: '))
    segundo = float(input('Qual o primeiro segundo: '))
    result = soma(primeiro, segundo)
    print(f'{primeiro} - {segundo} = {result}')

elif selecionar == 3:
    primeiro = float(input('Qual o primeiro numero: '))
    segundo = float(input('Qual o primeiro segundo: '))
    result = soma(primeiro, segundo)
    print(f'{primeiro} / {segundo} = {result}')

elif selecionar == 4: 
    primeiro = float(input('Qual o primeiro numero: '))
    segundo = float(input('Qual o primeiro segundo: '))
    result = soma(primeiro, segundo)
    print(f'{primeiro} * {segundo} = {result}')
else:
    print('Não existe essa opção.')


