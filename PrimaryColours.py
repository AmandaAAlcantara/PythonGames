print('Escolha duas cores primarias para descobrir a cor formada pela mistura das duas.')


cor_primaria1= ('vermelho')
cor_primaria2  = ('amarelo')
cor_primaria3 = ('azul')


cor_primaria_escolhida1 =  input('Insira a primeira cor primária escolhida: ')
cor_primaria_escolhida2 = input('Insira a segunda cor primária escolhida: ')


if cor_primaria1 == cor_primaria_escolhida1  and cor_primaria3 == cor_primaria_escolhida2:
    print('A cor secundária obtida será: Roxo')      
elif cor_primaria1 == cor_primaria_escolhida1 and cor_primaria2 == cor_primaria_escolhida2:
    print('A cor secundária obtida será: Laranja')
elif cor_primaria2 == cor_primaria_escolhida1 and cor_primaria3 == cor_primaria_escolhida2:
    print('A cor secundária obtida será: Verde') 
else: 
    print('Erro, digite uma cor primária')

    