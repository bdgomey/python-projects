from ohMyPoshAutomation import OhMyPoshAutomation
from ohMyPoshGui import OhMyPoshGui
import PySimpleGUI as sg

layout = [
    [sg.Text("If you have yet to install Oh My Posh and Git Posh, Please press the button below!")],
    [sg.Button("Install OhMyPosh", key="-INSTALL-"),
     sg.Button("Git Posh Theme Selector", key="-SELECTOR-"),
     sg.Exit()]
]

window = sg.Window('File Loader', layout, finalize=True)
window.write_event_value("-INIT-", "")
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        exit(0)

    if event == "-INSTALL-":
        automator = OhMyPoshAutomation()
        automator.install()
        automator.copy_themes(
            src=f"{automator.poshDir}\\themes",
            dest=f"{automator.tempFolder}\\themes",
            git_url=automator.git_url
        )

    if event == "-SELECTOR-":
        gui = OhMyPoshGui()
        gui.oh_my_posh_gui()

