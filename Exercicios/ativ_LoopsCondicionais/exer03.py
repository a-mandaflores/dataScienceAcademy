# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

tupla = (1, 2, 3, 4)
novaTuple = []
for i in tupla:
    calc = i * 2
    novaTuple.append(calc)

print(novaTuple)
