# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

frutas = ['Abacaxi', 'Morango', 'Amora', 'Uva', 'Pessego']

verificarFrutas = [x for x in frutas if 'Morango' in x]
print(verificarFrutas)