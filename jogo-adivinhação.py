#importa modolo random
import random  

#menu do jogo
print("JOGO DA ADIVINHAÇÃO".center(30,"-"))
print('\n')
print(f'Fácil: numero de 1 a 10\nMédio: numero de 1 a 20\nDifícil: numero de 1 a 50\n')
print('Digite SAIR para encerrar o jogo!')
print("\n")

#começo do while escolhendo dificuldade
while True:
    dificuldade = input('Esolha uma Dificuldade: (1=Fácil, 2=Médio ou 3=Difícil)')
    if dificuldade.upper() == 'SAIR': #opção de encerrar o jogo
        print('Jogo Encerrado!')
        break 

    if dificuldade == '1':
        print('NUMERO ENTRE 1 E 10 SORTEADO!\n')
        num = random.randint(1,10) #escolhe o numero de acordo com a dificuldade
        acerto = False #cria variavel false pro segundo laço

    if dificuldade == '2':
        print('NUMERO ENTRE 1 E 20 SORTEADO!\n')
        num = random.randint(1,20)
        acerto = False

    if dificuldade == '3':
        print('NUMERO ENTRE 1 E 50 SORTEADO!\n')
        num = random.randint(1,50)
        acerto = False

#começa segundo laço
    while not acerto:
        num_user = int(input('Digite um numero e tente acertar:')) #pede numero ao jogador

        if num_user == num:
            print(f'PARABENS você acertou o numero! {num} Vamos para proxima rodada:\n')
            acerto = True #se o jogador acertar a varieval se torna verdadeira e volta pro laço da dificuldade

#da dica para o jogador
        elif num > num_user:
            print(f'O numero é maior que {num_user}')

        elif num < num_user:
            print(f'O numero é menor que {num_user}')

        continue