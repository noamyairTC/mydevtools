import os

if os.system('hh') == 0:
    exit()

# Install bash history tool
os.system("add-apt-repository -y ppa:ultradvorka/ppa")
os.system("apt-get update")
os.system("apt-get install hh")
os.system('sudo -u "hh --show-configuration >> ~/.bashrc"')

