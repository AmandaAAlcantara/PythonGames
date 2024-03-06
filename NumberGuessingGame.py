from random import randint
print('Jogo de Adivinhação')
print('Escolha dois números inteiros e não negativos')

inicial = int(input('Digite o menor número possível para adivinhação: '))

if inicial < 0:
    print('Erro, digite somente números positivos')
else: 

    final = int(input('Digite o maior número possível para adivinhação: '))

    sorteio = randint (inicial, final+1)
    adivinhe = int(input('Adivinhe qual número foi gerado: '))

    print('Número gerado =',sorteio)
    if adivinhe == sorteio:
        print('Seu palpite estava correto')
    elif adivinhe > sorteio:
        print('Seu palpite foi muito alto')
    else:
        print('Seu palpite foi muito baixo')





