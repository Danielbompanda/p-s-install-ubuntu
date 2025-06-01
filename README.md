🛠️ Script Interativo de Pós-Instalação para Ubuntu e Derivados

Este é um script open source escrito em Python 3, que automatiza a configuração pós-instalação do Ubuntu e distribuições derivadas. Com uma interface interativa baseada em whiptail (python3-dialog), ele permite selecionar facilmente categorias de programas, instalar codecs, drivers adicionais e até buscar pacotes manualmente.

✅ Compatível com:

Ubuntu (20.04 ou superior)

Linux Mint

Pop!_OS

Zorin OS

Elementary OS
e outras distribuições baseadas no Ubuntu.



---

🔧 Funcionalidades

Atualização completa do sistema (apt-get update, upgrade, autoremove)

Instalação por categorias:

🛠️ Sistema: GParted, Timeshift, BleachBit, etc.

🎥 Multimídia: VLC, GIMP, OBS Studio, etc.

🌐 Internet: Firefox, FileZilla, Telegram, etc.

📋 Escritório: LibreOffice, Okular, Calibre, etc.

💻 Desenvolvimento: Git, VS Code, Python, Docker, etc.

🧰 Utilitários: Neofetch, Htop, Tweaks, etc.

🎮 Jogos: Steam, Lutris, Wine, etc.


Instalação de codecs multimídia e fontes proprietárias

Instalação de drivers adicionais com ubuntu-drivers autoinstall

Busca manual de pacotes por nome com verificação automática

Geração de log de instalação (instalador.log)

Verificação automática das dependências Python e do sistema



---

📦 Requisitos

Ubuntu ou derivado (20.04+)

Acesso root (sudo)

Python 3 instalado


> O script verifica automaticamente se pip, dialog e python3-dialog estão presentes, instalando-os se necessário.




---

⚙️ Como usar

Clone o repositório:

git clone https://github.com/Danielbompanda/p-s-install-ubuntu.git
cd p-s-install-ubuntu

Torne o script executável:

chmod +x instalar.py

Execute com permissões adequadas:

./instalar.py


---

🧪 Observações

Todos os pacotes são instalados via apt-get (sem Snap ou Flatpak).

O script pode ser facilmente personalizado editando o dicionário CATEGORIAS.

O suporte a Steam adiciona a arquitetura de 32 bits automaticamente.

O ubuntu-drivers funciona apenas em sistemas compatíveis (Ubuntu, Mint, Pop!_OS, etc.).



---

📄 Licença

Distribuído sob a GNU General Public License v3.0.
Veja o arquivo LICENSE para mais detalhes.
