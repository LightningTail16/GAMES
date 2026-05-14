import PySimpleGUI as sg

def makeTitleScreen():
    return [
        [sg.Text("LightningTail's Game Library")],
        [sg.Button("Start", key="start")],
        [sg.Button("Credits", key="credits")],
        [sg.Button("Exit", key="exit")],
    ]

def makeCreditsScreen():
    return [
        [sg.Text("Credits")],
        [sg.Text("Hangman: "), sg.Text(" Program from Hyperskill")],
        [sg.Text("Wordle: "), sg.Text(" Program from me")],
        [sg.Text("Words by fogleman's scrabble word list")],
        [sg.Text("Rock Paper Scissors: "), sg.Text(" Program originally from Garrett Symes")],
        [sg.Button("Back", key="back")],
    ]

def makeGameScreen():
    return [
        [sg.Text("Play Game")],
        [sg.Button("Hangman", key="hangman")],
        [sg.Button("back", key="back")],
    ]

def makeWindow(screen):
    if screen == "credits":
        layout = makeCreditsScreen()
    elif screen == "start":
        layout = makeGameScreen()
    else:
        layout = makeTitleScreen()

    return sg.Window("LightningTail's Game Library", layout)

currentScreen = "title"
window = makeWindow(currentScreen)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "exit":
        break
    elif event == "credits":
        window.close()
        currentScreen = "credits"
        window = makeWindow(currentScreen)
    elif event == "back":
        window.close()
        currentScreen = "title"
        window = makeWindow(currentScreen)
    elif event == "start":
        window.close()
        currentScreen = "start"
        window = makeWindow(currentScreen)

window.close()

# https://docs.pysimplegui.com/en/latest/documentation/module/elements/button/