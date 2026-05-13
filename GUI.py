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
        sg.Text("Credits")
    ],
    [
        sg.Text("Hangman")
    ],
    [
        sg.Button("Back", key="back")
    ],
]

layout = [
    [
        sg.Column(titleScreen, key="titleScreen", visible=True),
        sg.Column(creditsScreen, key="credits", visible=False),
    ]
]

window = sg.Window("LightningTail's Game Library", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "exit":
        break
    elif event == "credits":
        window["titleScreen"].update(visible=False)
        window["credits"].update(visible=True)
    elif event == "back":
        window["credits"].update(visible=False)
        window["titleScreen"].update(visible=True)

window.close()

#https://docs.pysimplegui.com/en/latest/documentation/module/elements/button/