import os
import PySimpleGUI as sg

automationPath = "C:\\Users\\Brian Gomes\\OneDrive - SkillStorm\\Desktop\\python-projects\\automateOh-myPosh"
choices = []

themeNames = os.listdir(f"{automationPath}\\themes")
for theme in themeNames:
    choices.append(theme)

print(choices)

def make_window():
    # Set theme based on previously saved
    layout = [
        sg.Text("Select your theme")
    ]
    
