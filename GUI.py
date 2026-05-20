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
        [sg.Button("Back", key="back")],
    ]

def makeWindow(screen, location=None, size=None):
    if screen == "credits":
        layout = makeCreditsScreen()
    elif screen == "start":
        layout = makeGameScreen()
    else:
        layout = makeTitleScreen()

    windowArguments = {
        "location": location,
        "resizable": True,
        "finalize": True,
    }

    if size is not None:
        windowArguments["size"] = size

    return sg.Window("LightningTail's Game Library", layout, **windowArguments)

def applyWindowMinimumSize(window):
    window.TKroot.update_idletasks()
    minimumWidth = window.TKroot.winfo_reqwidth()
    minimumHeight = window.TKroot.winfo_reqheight()
    window.TKroot.minsize(minimumWidth, minimumHeight)

def getWindowLocation(window):
    window.TKroot.update_idletasks()
    return (window.TKroot.winfo_x(), window.TKroot.winfo_y())

def switchScreen(window, screen):
    location = getWindowLocation(window)
    size = window.size
    window.close()
    return makeWindow(screen, location, size)

currentScreen = "title"
window = makeWindow(currentScreen)
applyWindowMinimumSize(window)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "exit":
        break
    elif event == "credits":
        currentScreen = "credits"
    elif event == "back":
        currentScreen = "title"
    elif event == "start":
        currentScreen = "start"
    window = switchScreen(window, currentScreen)
    applyWindowMinimumSize(window)

window.close()

# https://docs.pysimplegui.com/en/latest/documentation/module/elements/button/