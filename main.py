import random

def maquina():
    tabuleiro_maquina = []

    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro_maquina.append(linha)

    quantidade_navios_maquina = 5
    navios_colocados = 0

    while navios_colocados < quantidade_navios_maquina:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)

        if tabuleiro_maquina[linha][coluna] == 0:
            tabuleiro_maquina[linha][coluna] = 1
            navios_colocados += 1

    return tabuleiro_maquina, quantidade_navios_maquina


def humano(posicoes):          
    tabuleiro_humano = []
    quantidade_navios_humano = 5

    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro_humano.append(linha)  

    for (x, y) in posicoes:           
        tabuleiro_humano[x][y] = 1

    return tabuleiro_humano, quantidade_navios_humano


def escolha_humano():
    posicoes = []

    for i in range(5):
        print(f"Navio {i + 1}")

        while True:
            x = input(f"Qual linha deseja colocar o navio {i + 1}? (1 a 10) ")
            y = input(f"Qual coluna deseja colocar o navio {i + 1}? (1 a 10) ")

            if not x.isdigit() or not y.isdigit():
                print("Digite apenas números!")
                continue

            x = int(x)
            y = int(y)

            if x-1 < 0 or x-1 > 9:
                print("Linha inválida! Digite entre 1 e 10.")
            elif y-1 < 0 or y-1 > 9:
                print("Coluna inválida! Digite entre 1 e 10.")
            elif (x-1, y-1) in posicoes:
                print("Posição já ocupada! Escolha outra.")
            else:
                posicoes.append((x-1, y-1))
                break  

        print('-' * 64)
    return posicoes            

def ataque_maquina(tabuleiro_humano, quantidade_navios_humano, tabuleiro_humano_marcado, posicoes_atacadas):
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)

        if (linha, coluna) not in posicoes_atacadas:  
            posicoes_atacadas.append((linha, coluna))
            break

    if tabuleiro_humano[linha][coluna] == 1:
        acerto_maquina = True
        tabuleiro_humano_marcado[linha][coluna] = '💥'
        quantidade_navios_humano -= 1
    else:
        tabuleiro_humano_marcado[linha][coluna] = '👎'
        acerto_maquina = False

    return tabuleiro_humano, tabuleiro_humano_marcado, quantidade_navios_humano, acerto_maquina, linha, coluna

def feedback_maquina(acerto_maquina,linha,coluna):

    if acerto_maquina == True:
        print()
        print(f"Computador escolheu a linha {linha}")
        print(f"Computador escolheu a coluna {coluna}")
        print("Computador acertou!")
    
    else:
        print(f"Computador escolheu a linha {linha}")
        print(f"Computador escolheu a coluna {coluna}")
        print("Computador errou!")





def ataque_humano(tabuleiro_maquina, tabuleiro_maquina_marcado, quantidade_navios_maquina):
    posicao_valida = True
    while posicao_valida == True:
        linha = input("Qual linha deseja atacar? ")
        coluna = input("Qual coluna deseja atacar? ")

        if not linha.isdigit() or not coluna.isdigit():
            print("Digite apenas números!")
            continue

        linha = int(linha)
        coluna = int(coluna)
        
        if linha > 10  or linha < 1 or coluna > 10 or coluna < 1:
            print('Coordenada inválida!')
        elif tabuleiro_maquina_marcado[linha-1][coluna-1] == '👎' or tabuleiro_maquina_marcado[linha-1][coluna-1] == '💥':
            print('Voce ja atacou essa posição!')
        else:
            posicao_valida = False
    if tabuleiro_maquina[linha-1][coluna-1] == 1:
        acerto_humano = True
        tabuleiro_maquina_marcado[linha-1][coluna-1] = '💥'
        quantidade_navios_maquina -= 1
    else:
        tabuleiro_maquina_marcado[linha-1][coluna-1] = '👎'
        acerto_humano = False

    return tabuleiro_maquina, tabuleiro_maquina_marcado, quantidade_navios_maquina,acerto_humano

 
def feedback_humano(acerto_humano):
    if acerto_humano == True:
        print()
        print("Parabéns! Você acertou!")
    
    else:
        print()
        print("Não foi dessa vez!")


def mostrador(tabuleiro_maquina_marcado, tabuleiro_humano_marcado, quantidade_navios_humano, quantidade_navios_maquina):
    print()
    print()
    print("Tabuleiro do computador")
    for linha in tabuleiro_maquina_marcado:
        print(linha)
    print('-' * 64)
    print(f"Embarcações restantes: {quantidade_navios_maquina}")

    print()
    print()
    print("Tabuleiro do Jogador")
    for linha in tabuleiro_humano_marcado:
        print(linha)
    print('-' * 64)
    print(f"Embarcações restantes: {quantidade_navios_humano}")
    print()
    print()


def incial():
    print('-' * 64)
    print("Bem vindo ao Batalha Naval!")
    print("Legenda: '👎' = Posição já atacada, '💥' = Embarcação abatida ")
    print()
    print()
    print("Tabuleiro do Computador")
    tabuleiro_maquina_marcado = []

    for i in range(10):
        linha = []
        for j in range(10):
            linha.append('🌊')
        tabuleiro_maquina_marcado.append(linha)

    for linha in tabuleiro_maquina_marcado:
            print(linha)
    
    print('-' * 64)
    print("Embarcações restantes: 5")

    print()
    print()
    print("Tabuleiro do Jogador")
    tabuleiro_humano_marcado = []

    for i in range(10):
        linha = []
        for j in range(10):
            linha.append('🌊')
        tabuleiro_humano_marcado.append(linha)

    for linha in tabuleiro_humano_marcado:
            print(linha)
    
    print('-' * 64)
    print("Embarcações restantes: 5")
    print()
    print()

    return tabuleiro_humano_marcado, tabuleiro_maquina_marcado 



def main():
    tabuleiro_humano_marcado, tabuleiro_maquina_marcado = incial()
    posiçoes = escolha_humano()
    tabuleiro_humano, quantidade_navios_humano = humano(posiçoes)
    tabuleiro_maquina, quantidade_navios_maquina = maquina()

    posicoes_atacadas_maquina = []

    while quantidade_navios_humano > 0 and quantidade_navios_maquina > 0:
        mostrador(tabuleiro_maquina_marcado, tabuleiro_humano_marcado, quantidade_navios_humano, quantidade_navios_maquina)
        
        tabuleiro_maquina, tabuleiro_maquina_marcado, quantidade_navios_maquina, acerto_humano = ataque_humano(tabuleiro_maquina, tabuleiro_maquina_marcado, quantidade_navios_maquina)
        feedback_humano(acerto_humano)
        mostrador(tabuleiro_maquina_marcado, tabuleiro_humano_marcado, quantidade_navios_humano, quantidade_navios_maquina)

        if quantidade_navios_maquina == 0:
            break

        verificaçao = input("Digite '1' para prosseguir: ")
        while not verificaçao.isdigit() or int(verificaçao) != 1:
            print("Digite um comando válido")
            verificaçao = input("Digite '1' para prosseguir: ")

        tabuleiro_humano, tabuleiro_humano_marcado, quantidade_navios_humano, acerto_maquina, linha, coluna = ataque_maquina(tabuleiro_humano, quantidade_navios_humano, tabuleiro_humano_marcado, posicoes_atacadas_maquina)
        feedback_maquina(acerto_maquina, linha, coluna)
        

    if quantidade_navios_maquina == 0:
        print("Parabéns! Você afundou todas as embarcações do inimigo!")
        print("Jogo desenvolvido por: Gabriel Sandrini, João Pedro Lima e Mateus Picinin.")
        print("Obrigada por jogar nosso jogo!")

    else:
        print("Computador venceu!")

main()