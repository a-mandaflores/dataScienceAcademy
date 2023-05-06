# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela

temp = int(input('Qual a temperatura no momento'))

temperatura = lambda x: x > 35

if temperatura(temp) == True:
    print('Temperatura alta da bixiga! ')
else: print('Ta suave')

