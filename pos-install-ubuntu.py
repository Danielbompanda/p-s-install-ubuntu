#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil

# Verifica se um pacote Python está instalado
def pacote_python_instalado(nome):
    try:
        __import__(nome)
        return True
    except ImportError:
        return False

# Instala pacotes pip se necessário
def instalar_pacote_pip(pacote):
    print(f"Instalando dependência Python: {pacote}...")
    subprocess.run([sys.executable, "-m", "pip", "install", pacote], check=True)

# Verifica e instala dependências do sistema
def verificar_dependencias_sistema():
    if shutil.which("python3") is None:
        print("Erro: Python3 não está instalado.")
        sys.exit(1)

    if shutil.which("pip3") is None:
        print("Instalando pip...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "python3-pip"], check=True)

    if shutil.which("dialog") is None:
        print("Instalando o utilitário dialog...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "dialog"], check=True)

# Verifica e instala o python3-dialog
def instalar_dialog():
    verificar_dependencias_sistema()

    if not pacote_python_instalado("dialog"):
        instalar_pacote_pip("python3-dialog")

    try:
        from dialog import Dialog
        return Dialog(dialog="dialog", compat="whiptail")
    except ImportError:
        print("Erro: Não foi possível importar 'dialog' após instalação.")
        sys.exit(1)

d = instalar_dialog()
d.set_background_title("Instalador de Programas por Categoria")

CATEGORIAS = {
    "🛠️ Sistema": {
        "gparted": "Editor de partições",
        "gnome-disk-utility": "Utilitário de discos",
        "baobab": "Analisador de espaço",
        "bleachbit": "Limpador de sistema",
        "gufw": "Firewall gráfico",
        "timeshift": "Backup do sistema",
        "hardinfo": "Informações de hardware",
        "lm-sensors": "Sensores de temperatura",
        "ncdu": "Análise de uso de disco via terminal",
        "tldr": "Manual simplificado para comandos",
        "grub-customizer": "Personalizar o GRUB",
        "ufw": "Firewall Uncomplicated",
        "smartmontools": "Monitoramento de discos",
        "numlockx": "Ativar Num Lock no login"
    },
    "🎥 Multimídia": {
        "vlc": "Reprodutor de mídia",
        "gimp": "Editor de imagens",
        "kdenlive": "Editor de vídeo",
        "audacity": "Editor de áudio",
        "obs-studio": "Streaming e gravação",
        "simplescreenrecorder": "Gravação de tela",
        "ffmpeg": "Manipulador de mídia",
        "flameshot": "Captura de tela com anotações",
        "cheese": "Câmera/webcam",
        "handbrake": "Conversor de vídeo",
        "openshot": "Editor de vídeo simples",
        "pitivi": "Editor de vídeo básico",
        "pavucontrol": "Controle de áudio",
        "clementine": "Player de música",
        "rhythmbox": "Organizador de músicas",
        "brasero": "Gravação de CDs/DVDs"
    },
    "🌐 Internet": {
        "firefox": "Navegador Mozilla",
        "chromium-browser": "Navegador Chromium",
        "brave-browser": "Navegador Brave",
        "thunderbird": "Cliente de e-mail",
        "filezilla": "Cliente FTP",
        "remmina": "Acesso remoto",
        "transmission": "Cliente torrent",
        "telegram-desktop": "Telegram",
        "teams": "Microsoft Teams",
        "zoom": "Zoom Meetings",
        "qbittorrent": "Cliente torrent alternativo",
        "hexchat": "Cliente IRC",
        "deluge": "Outro cliente torrent",
        "lynx": "Navegador de terminal",
        "weechat": "Chat IRC em terminal"
    },
    "📋 Escritório": {
        "libreoffice": "Suite de escritório",
        "okular": "Visualizador de PDF",
        "evince": "Visualizador de documentos",
        "foliate": "Leitor de eBooks",
        "calibre": "Gerenciador de eBooks",
        "gnumeric": "Planilhas leves",
        "scribus": "Diagramação profissional",
        "zathura": "Visualizador de PDF leve",
        "onlyoffice-desktopeditors": "Suite alternativa"
    },
    "💻 Desenvolvimento": {
        "git": "Controle de versão",
        "vim": "Editor de texto",
        "geany": "IDE leve",
        "code": "Visual Studio Code",
        "build-essential": "Compiladores e ferramentas",
        "python3-pip": "Gerenciador de pacotes Python",
        "cmake": "Sistema de build",
        "nodejs": "Ambiente Node.js",
        "npm": "Gerenciador do Node.js",
        "openjdk-17-jdk": "Java Development Kit",
        "php": "Linguagem PHP",
        "sqlitebrowser": "Editor SQLite",
        "mysql-client": "Cliente MySQL",
        "postgresql": "Banco PostgreSQL",
        "docker.io": "Contêineres Docker",
        "flatpak": "Gerenciador de apps universal",
        "snapd": "Gerenciador Snap"
    },
    "🧰 Utilitários": {
        "neofetch": "Info do sistema",
        "htop": "Monitor do sistema",
        "curl": "Transferência HTTP",
        "wget": "Download via terminal",
        "net-tools": "Ferramentas de rede",
        "gnome-tweaks": "Ajustes GNOME",
        "p7zip-full": "Compactador 7z",
        "unrar": "Descompactar RAR",
        "file-roller": "Gerenciador de arquivos compactados",
        "xclip": "Copiar via terminal",
        "xsel": "Manipulação da área de transferência",
        "dconf-editor": "Editor de configurações avançadas",
        "stacer": "Otimizador de sistema",
        "preload": "Melhor desempenho de apps",
        "indicator-multiload": "Monitor do sistema na bandeja"
    },
    "🎮 Jogos (Steam, Lutris e Wine)": {
        "steam": "Plataforma Steam",
        "lutris": "Gerenciador de jogos",
        "wine": "Executar programas do Windows",
        "winetricks": "Ajustes e dependências do Wine",
        "playonlinux": "Interface para Wine",
        "gamemode": "Melhor desempenho para jogos",
        "glxinfo": "Informações da GPU (mesa-utils)",
        "vulkan-tools": "Ferramentas Vulkan"
    }
}

selecionados = []
log_file = open("instalador.log", "w")

def instalar_pacotes(lista):
    subprocess.run(["sudo", "apt-get", "update", "-y"], stdout=log_file, stderr=log_file)
    subprocess.run(["sudo", "apt-get", "upgrade", "-y"], stdout=log_file, stderr=log_file)
    for pkg in lista:
        d.gauge_start(text=f"Instalando {pkg}...", percent=0)
        log_file.write(f"Instalando {pkg}\n")
        subprocess.run(["sudo", "apt-get", "install", "-y", pkg], stdout=log_file, stderr=log_file)
        d.gauge_update(100)
    subprocess.run(["sudo", "apt-get", "install", "-y", "ubuntu-restricted-extras"], stdout=log_file, stderr=log_file)
    subprocess.run(["sudo", "ubuntu-drivers", "autoinstall"], stdout=log_file, stderr=log_file)

# Lista temporária para pacotes buscados na busca manual
busca_pacotes = []

while True:
    code, categoria = d.menu(
        "Escolha uma categoria para instalar programas:",
        choices=[(key, f"{len(value)} programas") for key, value in CATEGORIAS.items()] +
                [("🔍 Buscar pacote", "Procurar e adicionar um pacote específico"),
                 ("Finalizar", "Prosseguir para instalação")],
        width=70,
        height=20,
        menu_height=12
    )

    if code != d.OK:
        break

    if categoria == "Finalizar":
        break
    elif categoria == "🔍 Buscar pacote":
        while True:
            code, pacote = d.inputbox("Digite o nome do pacote que deseja buscar (deixe vazio para finalizar):")
            if code != d.OK or not pacote.strip():
                # Sai da busca manual se o usuário cancelar ou não digitar nada
                break

            resultado = subprocess.run(["apt-get", "show", pacote], capture_output=True, text=True)
            if resultado.returncode == 0:
                if pacote not in busca_pacotes:
                    busca_pacotes.append(pacote)
                d.msgbox(f"Pacote '{pacote}' encontrado e adicionado na lista de busca.")
            else:
                d.msgbox("Pacote não encontrado.")

        # Após terminar a busca, permite selecionar múltiplos pacotes buscados para instalação
        if busca_pacotes:
            choices = [(p, p, True) for p in busca_pacotes]
            code, pacotes = d.checklist(
                "Selecione os pacotes buscados para instalar:",
                choices=choices,
                width=70,
                height=20,
                list_height=10
            )
            if code == d.OK:
                selecionados.extend(pacotes)
            busca_pacotes = []
        continue

    programas = CATEGORIAS[categoria]
    checklist = [(pkg, desc, False) for pkg, desc in programas.items()]

    code, pacotes = d.checklist(
        f"Selecione os programas da categoria {categoria}:",
        choices=checklist,
        width=70,
        height=25,
        list_height=15
    )

    if code == d.OK:
        selecionados.extend(pacotes)

selecionados = list(set(selecionados))

if "steam" in selecionados:
    d.infobox("Habilitando suporte a 32 bits necessário para Steam...")
    subprocess.run(["sudo", "dpkg", "--add-architecture", "i386"], check=True)
    subprocess.run(["sudo", "apt-get", "update", "-y"], stdout=log_file, stderr=log_file)

if selecionados:
    instalar_pacotes(selecionados)
    d.msgbox("✅ Instalação concluída com sucesso!", width=50)
else:
    d.msgbox("Nenhum programa foi selecionado.", width=50)

log_file.close()
