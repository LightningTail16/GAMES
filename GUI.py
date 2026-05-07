import PySimpleGUI as sg

titleScreen = [
    [
        sg.Text("LightningTail's Game Library")
    ],
    [
        sg.Button("Start", key="start")
    ],
    [
        sg.Button("Credits", key="credits")
    ],
    [
        sg.Button("Exit", key="exit")
    ],
]

creditsScreen = [
    [
        sg.Text("Credits"),
        sg.Text("Hangman")
    ]
]

layout = [titleScreen]

window = sg.Window("LightningTail's Game Library", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "exit":
        break
    elif event == "credits":
        layout = [creditsScreen]
        window["-OUT-"].update(creditsScreen)

window.close()

#https://docs.pysimplegui.com/en/latest/documentation/module/elements/button/