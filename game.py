import random
import PySimpleGUI as sg


decisions = {
    '0' : 'Rock',
    '1' : 'Paper',
    '2' : 'Scissor'
}

first_collumn = [
    [
        sg.Text("Escolha sua opção"),
        sg.Button("Rock"),
        sg.Button("Paper"),
        sg.Button("Scissor")
    
    ]
]