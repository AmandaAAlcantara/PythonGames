from random import randint
print('---------Jogo do Pokemon---------')
nomedojogador = input('Digite o nome do jogador: ')
while (nomedojogador == '') or (nomedojogador == ' '):
    print('Nome inválido.')
    nomedojogador = input('Digite o nome do jogador: ')

 
print('Olá',nomedojogador,', agora você deverá escolher o Pokemon que te acompanhará durante o jogo!')
print('Estes são os Pokemons disponíveis:')
print('<1> Bulbassauro')
print('<2> Charmander')
print('<3> Squirtle')
pokemonescolhido = (input('Qual será o Pokemon de sua escolha?: '))
while (pokemonescolhido != '3') and (pokemonescolhido != '2') and (pokemonescolhido != '1'):
    print('Número inválido, escolha não corresponde a um Pokemon disponível.')
    pokemonescolhido = input('Qual será o Pokemon de sua escolha? ')

sorteio = randint(1,3)

if ( pokemonescolhido == '3' and sorteio == 1):
    print('Squirtle lutou contra Bubassauro. Você perdeu a batalha, tente jogar novamente.')
elif ( pokemonescolhido == '1' and sorteio == 3):
    print('Bulbassauro lutou contra Squirtle. Você ganhou a batalha, parabéns!')
elif(pokemonescolhido == '1' and sorteio == 2): 
    print('Bulbassauro lutou contra Charmander. Você perdeu a batalha, tente jogar novamente.') 
elif (pokemonescolhido == '2' and sorteio == 1):
    print('Charmander lutou contra Bulbassauro. Você ganhou a batalha, parabéns!')
elif (pokemonescolhido == '2' and sorteio == 3): 
    print('Charmander lutou contra Squirtle. Você perdeu a batalha, tente jogar novamente.')
elif (pokemonescolhido == '3' and sorteio == 2):
    print('Squirtle lutou contra Charmander. Você ganhou esta batalha, parabéns!')
elif (pokemonescolhido == '1' and sorteio == 1):
    print('Bulbassauro lutou contra Bulbassauro. A batalha foi um empate.')
elif (pokemonescolhido == '2' and sorteio ==2):
    print('Charmander lutou contra Charmander. A batalha foi um empate.')
else:
    print('Squirtle lutou contra Squirtle. A batalha foi um empate.')
input('')

