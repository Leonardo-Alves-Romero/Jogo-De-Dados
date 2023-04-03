import random
import PySimpleGUI as sg

# Layout da janela do jogo
layout = [
    [sg.Text('Bem-vindo ao jogo de dados!')],
    [sg.Text('Pressione o botão "Jogar" para jogar os dados.')],
    [sg.Text('Total:___', size=(20, 1), font=('Helvetica', 20), justification='center', key='_TOTAL_')],
    [sg.Button("Jogar"), sg.Button("Sair")]
]

# Janela do jogo
window = sg.Window("Jogo de Dados", layout)

# Loop principal da interface gráfica
while True:
    event, values = window.read()

    # Se o jogador quiser jogar, inicia-se o jogo
    if event == "Jogar":
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        total = dado1 + dado2

        # Atualizando o total na interface gráfica 
        window['_TOTAL_'].update("Total: " + str(total))

        # Verificando se o jogador venceu
        if total == 7 or total == 11:
            sg.popup('Você venceu!')

        # Verificando se o jogador perdeu
        elif total == 2 or total == 12:
            sg.popup('Você perdeu!')
    
        # A partida continua
        else:
            pass
    # Se o jogador quiser sair, encerra-se o jogo
    elif event == "Sair" or event == sg.WIN_CLOSED:
        break

window.close()