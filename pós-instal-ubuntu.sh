#!/bin/bash

# Função para imprimir títulos em destaque
print_titulo() {
    echo -e "\n========== $1 ==========\n"
}

# Lista de programas úteis
PROGRAMAS=(
    libreoffice
    gimp
    vlc
    gparted
    file-roller
    p7zip-full
    unrar
    gnome-disk-utility
    baobab
    synaptic
    timeshift
    bleachbit
    gufw
    thunderbird
    transmission
    filezilla
    remmina
    obs-studio
    simplescreenrecorder
    neofetch
    net-tools
    curl
    git
    vim
    htop
)

print_titulo "Atualizando a lista de pacotes"
sudo apt update

print_titulo "Atualizando os pacotes existentes"
sudo apt upgrade -y
sudo apt dist-upgrade -y
sudo apt autoremove -y
sudo apt autoclean -y

print_titulo "Instalando programas úteis"
for programa in "${PROGRAMAS[@]}"; do
    echo "Instalando: $programa"
    sudo apt install -y "$programa"
done

print_titulo "Instalando codecs multimídia"
sudo apt install -y ubuntu-restricted-extras

print_titulo "Instalando drivers adicionais (se aplicável)"
sudo ubuntu-drivers autoinstall

print_titulo "Finalizado com sucesso!"

