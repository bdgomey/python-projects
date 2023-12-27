from ohMyPoshAutomation import OhMyPoshAutomation
from ohMyPoshGui import OhMyPoshGui


automator = OhMyPoshAutomation()
automator.install()
automator.copy_themes(
    src=f"{automator.poshDir}\\themes",
    dest=f"{automator.tempFolder}\\themes",
    git_url=automator.git_url
)

gui = OhMyPoshGui()
gui.oh_my_posh_gui()

