from subprocess import call
import subprocess
import os
import shutil
from pathlib import Path


class OhMyPoshAutomation:

    def __init__(self):
        self.power_shell_path = f"{os.path.expanduser('~')}"
        self.tempFolder = f"{os.path.expanduser('~')}\\AppData\\Local\\Temp"
        self.poshDir = f"{self.tempFolder}\\posh"
        self.git_url = 'https://github.com/JanDeDobbeleer/oh-my-posh.git'

    @staticmethod
    def run(cmd):
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        return completed

    def install(self):
        self.run("Set-ExecutionPolicy Bypass -Scope Process -Force")
        self.run("install-module posh-git -Scope CurrentUser -Force")
        if not self.run("oh-my-posh"):
            self.run("""
            Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression 
            ((New-Object System.Net.WebClient).DownloadString('https://ohmyposh.dev/install.ps1'))
            """)

    def copy_themes(self, src, dest, git_url):
        src_path = Path(src)
        dest_path = Path(dest)
        self.git_url = git_url
        if not os.path.exists(Path(self.tempFolder) / "oh-my-posh"):
            self.run(f"git clone {git_url}")
        if not os.path.exists(dest_path):
            os.mkdir(dest_path)
        for item in src_path.iterdir():
            if item.is_dir():
                self.copy_themes(item, dest_path / item.name, self.git_url)
            else:
                shutil.copy2(item, dest_path / item.name)


if __name__ == '__main__':
    automator = OhMyPoshAutomation()
    automator.install()
    automator.copy_themes()
