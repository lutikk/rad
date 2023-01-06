'Для авто настройки хоста' 
'Пусть будет'
import os

pro = input("Кол-во ядер кмд nproc")

os.system('sudo apt update')

os.system('sudo apt install git')
os.system('sudo apt install zsh')
os.system('sudo apt-get update')
os.system('sudo apt-get install -y language-pack-ru')
os.system('sudo apt-get install -y language-pack-gnome-ru')
os.system('sudo apt-get install -y libreoffice-l10n-ru')
os.system('sudo apt-get install -y hyphen-ru mythes-ru hunspell-ru')

os.system('sudo apt install powerline fonts-powerline')
os.system('sudo apt-get update && sudo apt-get upgrade ')
os.system('sudo apt-get install -y sh git vim curl')
os.system('sudo apt-get install -y git')
os.system('sudo apt-get install -y curl')
os.system('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')

os.system('sudo apt-get update -y')
os.system('sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y')
os.system('wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tar.xz')
os.system('tar xf Python-3.8.5.tar.xz')
os.chdir(f'{os.getcwd()}/Python-3.8.5')
os.system('./configure')
os.system(f'make -j {pro} && sudo make altinstall')