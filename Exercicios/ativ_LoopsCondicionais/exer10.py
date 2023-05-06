# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 

frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 

#fatiarFrase = [x for x in frasesplit(x)]
fatiar_Frase = frase.split()

contarquantasR = len([x for x in fatiar_Frase if 'n' in x])
print(contarquantasR)
