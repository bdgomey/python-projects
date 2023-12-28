import PySimpleGUI as sg
import os
import subprocess
from pathlib import PurePath
import re


class OhMyPoshGui:

    def __init__(self):
        self.window_title = "Oh My Posh Theme Changer"
        self.temp_folder = f"{os.path.expanduser('~')}\\AppData\\Local\\Temp"
        self.theme_dir = f"{self.temp_folder}\\themes"
        self.ps_profile_result = subprocess.run(["powershell", "-Command", "echo $PROFILE"], capture_output=True)
        self.old_ps_script_path = self.ps_profile_result.stdout.decode().strip()
        self.psScriptPath = re.sub(r"WindowsPowerShell", "PowerShell", self.old_ps_script_path)
        self.resize_ratio = 2

    def oh_my_posh_gui(self):
        window_title = self.window_title
        ps_script_path = self.psScriptPath
        theme_dir = self.theme_dir
        resize_ratio = self.resize_ratio

        menu_def = [["File", ["Command1", "Command2", "Command3"]],
                    ["Menu", ["Settings", "About", "Exit"]]]

        layout = [[sg.Menu(menu_def, tearoff=True, font="Arial", )],
                  [sg.Titlebar(window_title)],
                  [sg.Button("Import posh-git"), sg.Button("Import Terminal Icons")],
                  [sg.Text('Select your Posh Type', font='Arial')],
                  [sg.InputText(key='-FILE_PATH-'),
                   sg.FilesBrowse(initial_folder=theme_dir, file_types=[("JSON Files", "*.json")]),],
                  [sg.Button("Check Theme", key="-THEME-"), sg.Button("Submit"), sg.Exit()]
                  ]
        # Create the Window
        window = sg.Window('File Loader', layout, finalize=True)
        window.write_event_value("-INIT-", "")
        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, "Exit"):
                exit(0)

            if event == "Import posh-git":
                with open(ps_script_path, "r") as file:
                    lines = file.readlines()
                for line in lines:
                    if "Import-Module posh-git" in line:
                        print(line)
                        sg.popup("Posh Git already imported")
                        break
                else:
                    with open(ps_script_path, "a") as module:
                        module.write("\nImport-Module posh-git\n")
                        sg.popup("Imported Posh Git")

            if event == "Import Terminal Icons":
                with open(ps_script_path, "r") as file:
                    lines = file.readlines()
                for line in lines:
                    if "Import-Module -Name Terminal-Icons" in line:
                        sg.popup("Terminal Icons already imported")
                        break
                else:
                    with open(ps_script_path, "a") as file:
                        file.write("\nImport-Module -Name Terminal-Icons\n")
                        sg.popup("Imported Terminal Icons")
                        file.close()

            if event == "About":
                window.disappear()
                sg.popup(window_title, "Version: 1.0.0", "Installs and Configures Oh My Posh Themes and Oh My Posh Git",
                         grab_anywhere=True)

            if event == "-THEME-":
                image_path = f"{PurePath("../images")}"
                images = os.listdir(image_path)
                file_path = values['-FILE_PATH-']
                file_parts = file_path.split("/")
                files = file_parts[len(file_parts) - 1]
                file_list = files.split(".omp.json")
                file_name = file_list[0]
                for image in images:
                    image_parts = image.split(".png")
                    image_name = image_parts[0]
                    if image_name == file_name:
                        layout = [
                            [sg.Titlebar("Oh My Posh Themes")],
                            [sg.Text("Please Select")],
                            [sg.Image("../images/" + image_name + ".png", key="-IMAGE-")],

                        ]
                        window = sg.Window('Posh Themes', layout, finalize=True)
                        while True:
                            event, values = window.read()

                            if event in (sg.WIN_CLOSED, "Exit"):
                                exit(0)


            if event == "Submit":
                if os.path.exists(values['-FILE_PATH-']):
                    posh_init = f"oh-my-posh --init --shell pwsh --config '{values["-FILE_PATH-"]}' | Invoke-Expression"
                    with open(ps_script_path, "r") as file:
                        lines = file.readlines()

                    # Replace the line in memory
                    line_found = False
                    for i, line in enumerate(lines):
                        if "oh-my-posh --init --shell" in line:
                            lines[i] = f"{posh_init}\n"
                            line_found = True
                            break

                    # If the line was not found, append it to the end of the file
                    if not line_found:
                        lines.append(f"{posh_init}\n")

                    # Write all lines back to the file
                    with open(ps_script_path, "w") as file:
                        file.writelines(lines)
                    sg.popup("Your Theme has been added!")
                    window.close()

            if event == "EXIT":
                exit(0)
            if event in ("Command1", "Command2", "Command3"):
                sg.popup_error("Feature not enabled yet")


if __name__ == '__main__':
    gui = OhMyPoshGui()
    gui.oh_my_posh_gui()