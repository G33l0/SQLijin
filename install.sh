#!/bin/bash

# SQLijin v2.1 Auto-Installer
# Maker: https://t.me/x0x0h33l0

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${RED}"
cat << "EOF"
   __ __  _    _  _ _       
  / _// _ \/ /   ()() ()_ 
  \_ \/ / / / /   / / / / / / _ \
 _/ / // / /__/ / / / / / / / /
/_/\_\\_/////// // 
                                   
EOF
echo -e "${NC}"

echo -e "${CYAN}[*] Initializing SQLijin v2.1 Installation...${NC}"

# Step 1: Update system packages
echo -e "${CYAN}[*] Updating system repositories...${NC}"
sudo apt update -y && sudo apt upgrade -y

# Step 2: Install Python3 and Pip if not present
echo -e "${CYAN}[*] Checking for Python3 and Pip...${NC}"
sudo apt install -y python3 python3-pip git

# Step 3: Install tool dependencies
echo -e "${CYAN}[*] Installing Elite CLI dependencies...${NC}"
pip3 install -r requirements.txt --break-system-packages 2>/dev/null || pip3 install -r requirements.txt

# Step 4: Finalize permissions
echo -e "${CYAN}[*] Setting execution permissions...${NC}"
chmod +x SQLijin.py

echo -e "${GREEN}[+] Setup complete!${NC}"
echo -e "${CYAN}[*] To launch the tool, run: ${NC}${RED}python3 SQLijin.py${NC}"