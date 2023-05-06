# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0

for i in range(1, 101):
    if i < 24:
        print(i)
        contador += 1



print(contador)