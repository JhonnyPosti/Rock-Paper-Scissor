import random
import PySimpleGUI as sg

decisions = {
    '0' : 'Rock',
    '1' : 'Paper',
    '2' : 'Scissor'
}

def robotplay():
    robotchoice = random.choice(list(decisions))
    return robotchoice

def main():
    radio_buttons = ['Rock', 'Paper', 'Scissor']
    layout = [
        [sg.Text('Selecione uma jogada')],
        [sg.Radio(text, 1) for text in radio_buttons],
        [sg.Button('Read')]
    ]

    window = sg.Window('Rock Paper & Scissor', layout)

    while True:
        event, values = window.Read()
        robotchoice = robotplay()
        if event is None:
            break
        print(event, values)
        print(robotchoice)

if __name__ == "__main__":
    main()