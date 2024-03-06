palavrasecreta = ('desafio')
espaço = ['_','_','_','_','_','_','_']
letrasescolhidas = []
erros = 7
acertos = 0

print('-------Jogo da Forca-------')
print('Descubra a palavra secreta.')
print('Boa sorte!!!') 
print(' _ '*len(palavrasecreta))

while True:
    letra = str(input('Digite uma letra: '))
    while letra in letrasescolhidas:
        print('Essa letra já foi escolhida, tente outra letra')
        letra = str(input('Digite uma letra: '))
    letrasescolhidas.append(letra)
    print('Letras que já foram escolhidas {}'.format(letrasescolhidas))
    palavrasecreta == 'desafio'
    if letra in palavrasecreta:
        espaço[palavrasecreta.index(letra)] = (letra)
        print(espaço)
        acertos += 1
    else:
        print(espaço)
        erros -= 1
        if erros <= 0:
            print('Acabaram as tentativas, você perdeu. A palavra era: desafio.')
            break
    if acertos == 7:
        print('Parabén você descobriu a palavra secreta! A palavra era: desafio')
        break
print('Fim do Jogo da Forca!')
input(' ')

