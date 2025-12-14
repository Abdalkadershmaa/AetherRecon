#!/bin/bash

# ==========================================
# BB Orchestrator Environment Installer
# ==========================================

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}[*] Starting BB Environment Setup...${NC}"
echo -e "${BLUE}[*] Note: This script assumes a Debian-based system (Kali, Ubuntu).${NC}"

# 1. System Updates & Essentials
# ------------------------------------------
echo -e "\n${YELLOW}[1/6] Updating System & Installing Essentials...${NC}"
sudo apt-get update -y
sudo apt-get install -y git curl wget unzip tar jq python3 python3-pip libpcap-dev build-essential

# 2. Install/Setup Go (Golang)
# ------------------------------------------
echo -e "\n${YELLOW}[2/6] Setting up Go Language...${NC}"
if ! command -v go &> /dev/null; then
    echo "    -> Go not found. Installing..."
    wget https://go.dev/dl/go1.21.0.linux-amd64.tar.gz -O go.tar.gz
    sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go.tar.gz
    rm go.tar.gz
    
    # Add to PATH (Temporary & Permanent)
    export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin
    echo 'export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin' >> ~/.bashrc
    echo 'export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin' >> ~/.zshrc
else
    echo -e "${GREEN}    -> Go is already installed.${NC}"
fi

# 3. Create Directory Structure
# ------------------------------------------
echo -e "\n${YELLOW}[3/6] Creating Directory Structure...${NC}"
BASE_DIR=$(pwd)
TOOLS_DIR="$BASE_DIR/tools"
WORDLIST_DIR="$BASE_DIR/wordlists"

mkdir -p "$TOOLS_DIR"
mkdir -p "$WORDLIST_DIR"
echo -e "${GREEN}    -> Tools Dir: $TOOLS_DIR${NC}"

# 4. Install Go Tools
# ------------------------------------------
echo -e "\n${YELLOW}[4/6] Installing Go Tools (Subfinder, Amass, etc.)...${NC}"

# Function to install go tool
install_go_tool() {
    package=$1
    name=$2
    echo -e "    -> Installing $name..."
    go install -v $package@latest
}

install_go_tool "github.com/projectdiscovery/subfinder/v2/cmd/subfinder" "Subfinder"
install_go_tool "github.com/owasp-amass/amass/v4/.../cmd/amass" "Amass"
install_go_tool "github.com/tomnomnom/assetfinder" "Assetfinder"
install_go_tool "github.com/gwen001/github-subdomains" "Github-Subdomains"
install_go_tool "github.com/projectdiscovery/dnsx/cmd/dnsx" "DNSx"
install_go_tool "github.com/projectdiscovery/httpx/cmd/httpx" "HTTPx"
install_go_tool "github.com/projectdiscovery/chaos-client/cmd/chaos" "Chaos"
install_go_tool "github.com/projectdiscovery/naabu/v2/cmd/naabu" "Naabu"
install_go_tool "github.com/projectdiscovery/nuclei/v2/cmd/nuclei" "Nuclei"
install_go_tool "github.com/michenriksen/aquatone" "Aquatone"

# 5. Install External/Python Tools (In 'tools' folder)
# ------------------------------------------
echo -e "\n${YELLOW}[5/6] Installing Python & External Tools...${NC}"

# Findomain (Binary install is faster/easier than Cargo)
echo -e "    -> Installing Findomain..."
wget https://github.com/Findomain/Findomain/releases/latest/download/findomain-linux.zip -O findomain.zip
unzip -o findomain.zip
chmod +x findomain
sudo mv findomain /usr/local/bin/
rm findomain.zip

# Sublist3r
echo -e "    -> Installing Sublist3r..."
if [ ! -d "$TOOLS_DIR/Sublist3r" ]; then
    git clone https://github.com/aboul3la/Sublist3r.git "$TOOLS_DIR/Sublist3r"
    pip3 install -r "$TOOLS_DIR/Sublist3r/requirements.txt"
fi

# Knockpy
echo -e "    -> Installing Knockpy..."
if [ ! -d "$TOOLS_DIR/Knockpy" ]; then
    git clone https://github.com/guelfoweb/knock.git "$TOOLS_DIR/Knockpy"
    # Note: Knockpy v6+ is installed via pip normally, but for the script path:
    cd "$TOOLS_DIR/Knockpy" && python3 setup.py install
    cd "$BASE_DIR"
fi

# Dnscan
echo -e "    -> Installing Dnscan..."
if [ ! -d "$TOOLS_DIR/dnscan" ]; then
    git clone https://github.com/rbsec/dnscan.git "$TOOLS_DIR/dnscan"
    pip3 install -r "$TOOLS_DIR/dnscan/requirements.txt"
fi

# Anubis
echo -e "    -> Installing Anubis..."
if [ ! -d "$TOOLS_DIR/Anubis" ]; then
    git clone https://github.com/jonnybanana/anubis.git "$TOOLS_DIR/Anubis"
    pip3 install -r "$TOOLS_DIR/Anubis/requirements.txt"
fi

# Crtndstry (Simulated/Placeholder as it's often a custom script)
# We will create the folder so the python script doesn't complain, 
# but usually, this tool is less common now.
mkdir -p "$TOOLS_DIR/crtndstry"

# 6. Download Wordlists
# ------------------------------------------
echo -e "\n${YELLOW}[6/6] Downloading Wordlists...${NC}"
if [ ! -f "$WORDLIST_DIR/dns.txt" ]; then
    echo "    -> Downloading generic DNS wordlist..."
    wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-110000.txt -O "$WORDLIST_DIR/dns.txt"
fi

if [ ! -f "$WORDLIST_DIR/resolvers.txt" ]; then
    echo "    -> Downloading Resolvers..."
    wget https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt -O "$WORDLIST_DIR/resolvers.txt"
fi

# ==========================================
# Final Check
# ==========================================
echo -e "\n${GREEN}[✔] Installation Complete!${NC}"
echo -e "${BLUE}Please run the following command to update your shell path:${NC}"
echo -e "    source ~/.bashrc  (or source ~/.zshrc)"
echo -e "\n${BLUE}Then run the orchestrator:${NC}"
echo -e "    python3 run_bb_professional.py target.com"
