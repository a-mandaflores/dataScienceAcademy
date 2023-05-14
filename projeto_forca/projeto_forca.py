import random  
from os import system, name

def limpa_tela():

    #Windows
    if name == 'nt':
       _ = system('cls')
    
    # Mac ou outros
    else:
       _ = system('clear')


#função
def game():
   
   limpa_tela()
   
   print('\nBem vindo(a) ao jogo da forca!')
   print('Adivinhe a palavra abaixo: \n')

   #lista de palavra para o jogo
   palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

   #Escolhe randomicamente uma palavra
   palavra = random.choice(palavras)

   #list comprehension
   letras_descobertas = ['_' for letra in palavra]

   chances = 6

   letras_erradas = []

   while chances > 0:
      
        print(' '.join(letras_descobertas))
        print('\nChances restantes:', chances)
        print('Letras erradas:', ' '.join(letras_erradas))

        tentativa = input('Digite uma letra: ').lower()

        if tentativa in palavra:
         index = 0

         for letra in palavra:
            if tentativa == letra:
               letras_descobertas[index] = letra
            index += 1
        else:
         chances -= 1
         letras_erradas.append(tentativa)


        #Condicional
        if '_' not in letras_descobertas:
            print('Você venceu, a palavra era: ', palavra)
            break
        
    #condicional
   if "_" in letras_descobertas:
        print('Voce perdeu, a palavra era: ', palavra)
        


print(game())