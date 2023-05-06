# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]

letrasA = [x for x in palavras if 'a' in x]

print(letrasA)