# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

DiasdaSemana = ['Segunda', 'Terça', 'Quart', 'Quinta', 'Sexta']

def diaSemana(i):
    if i == 'Domingo' or i == 'Sabado':
        print('Hoje é dia de descanço. ')
    elif i == 'Segunda' or i == 'Terça' or i == 'Quarta' or i == 'Quinta' or i == 'Sexta': 
        print('Você precisa trabalhar. ')
    else: print('Esse dia não existe')


diaEscolhido = input('Qual o dia é hoje? ')

diaSemana(diaEscolhido)
