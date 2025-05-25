🛠️ Script de Instalação e Configuração Pós-Instalação para Ubuntu e Derivados

Este script automatiza o processo de atualização do sistema, instalação de programas essenciais, codecs multimídia e drivers adicionais em distribuições baseadas no Ubuntu, como:

    Ubuntu

    Linux Mint

    Pop!_OS

    Zorin OS

    Elementary OS

    entre outras.

✅ O que o script faz:

    Atualiza a lista de pacotes (apt update)

    Atualiza todos os pacotes do sistema (apt upgrade, dist-upgrade, autoremove)

    Instala uma seleção de programas úteis para o dia a dia:

        Produtividade: LibreOffice, GIMP, Thunderbird

        Multimídia: VLC, OBS Studio, SimpleScreenRecorder

        Sistema: GParted, Timeshift, BleachBit, Synaptic, GUFW, Gnome Disk Utility

        Compressão: File Roller, p7zip, unrar

        Rede: FileZilla, Remmina, Transmission

        Terminal: Vim, Htop, Neofetch, Net-tools, Git, Curl

    Instala codecs multimídia e fontes proprietárias (pacote ubuntu-restricted-extras)

    Instala drivers adicionais automaticamente (ex: drivers NVIDIA) com ubuntu-drivers autoinstall

💡 Requisitos:

    Distribuição baseada em Ubuntu (20.04 ou superior)

    Acesso root ou permissões sudo

⚙️ Como usar:

    Clone este repositório ou baixe o script:

git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

Torne o script executável:

chmod +x instalar_completo.sh

Execute:

    ./instalar_completo.sh

🧪 Observações:

    O script instala apenas pacotes via apt, não usa Flatpak ou Snap. Você pode personalizá-lo conforme suas preferências.

    O ubuntu-drivers só funciona em sistemas com suporte oficial a ele, como Ubuntu, Mint, Pop!_OS, etc.

    Timeshift pode precisar de um PPA em algumas distros (como Ubuntu 24.04+), mas ainda está disponível na maioria dos repositórios.

📌 Licença

Este projeto está licenciado sob a Open Source Code.
