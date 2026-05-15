import PySimpleGUI as sg


def make_title_screen():
    return [
        [sg.Text("LightningTail's Game Library")],
        [sg.Button("Start", key="start")],
        [sg.Button("Credits", key="credits")],
        [sg.Button("Exit", key="exit")],
    ]


def make_credits_screen():
    return [
        [sg.Text("Credits")],
        [sg.Text("Game Library by LightningTail")],
        [sg.Text("Games included:")],
        [sg.Text("- Hangman")],
        [sg.Text("- Wordle")],
        [sg.Text("- Rock Paper Scissors")],
        [sg.Button("Back", key="back"), sg.Button("Exit", key="exit")],
    ]


def make_window(screen, location=None):
    if screen == "credits":
        layout = make_credits_screen()
    else:
        layout = make_title_screen()

    return sg.Window(
        "LightningTail's Game Library", layout, location=location, finalize=True
    )


def get_window_location(window):
    window.TKroot.update_idletasks()
    return (window.TKroot.winfo_x(), window.TKroot.winfo_y())


def switch_screen(window, screen):
    location = get_window_location(window)
    window.close()
    return make_window(screen, location)


current_screen = "title"
window = make_window(current_screen)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "exit":
        break
    elif event == "credits":
        current_screen = "credits"
        window = switch_screen(window, current_screen)
    elif event == "back":
        current_screen = "title"
        window = switch_screen(window, current_screen)

window.close()

# https://docs.pysimplegui.com/en/latest/documentation/module/elements/button/
