from subprocess import call
import subprocess
import os
import shutil
from pprint import pprint
import inquirer
import stat
from pathlib import Path



automationPath = "C:\\Users\\Brian Gomes\\OneDrive - SkillStorm\\Desktop\\python-projects\\automateOh-myPosh"

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    # print(completed.stdout)  # Print the output
    # print(completed.stderr) 
    return completed

if __name__ == '__main__':
# Is the error an access error?
    run("Set-ExecutionPolicy Bypass -Scope Process -Force")

    def on_rm_error( func, path, exc_info):
        os.chmod( path, stat.S_IWRITE )
        os.unlink( path )
    dirPath = f"{automationPath}\\oh-my-posh"
    if not dirPath:
        shutil.rmtree( dirPath, onerror = on_rm_error )
        for i in os.listdir(dirPath):
            if i.endswith('git'):
                print(i)
                tmp = os.path.join(dirPath, i)
            #     # We want to unhide the .git folder before unlinking it.
                while True:
                    call(['attrib', '-H', tmp])
                    break
                shutil.rmtree(tmp, onerror=on_rm_error)
        

    else:
        downloadThemes = "git clone https://github.com/JanDeDobbeleer/oh-my-posh.git"
        downloadingThemes = run(downloadThemes)



    installOhMyPosh = "Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://ohmyposh.dev/install.ps1'))"
    install = run(installOhMyPosh)

    def copytree(src, dst):
        src_path = Path(src)
        dst_path = Path(dst)

        if not src_path.exists():
            print(f"Source path {src_path} does not exist.")
            return

        if not dst_path.exists():
            os.makedirs(dst_path)

        for item in src_path.iterdir():
            if item.is_dir():
                copytree(item, dst_path / item.name)
            else:
                shutil.copy2(item, dst_path / item.name)

    srcPath = f"{automationPath}\\oh-my-posh\\themes"
    copytree(srcPath, Path(automationPath) / 'themes')



