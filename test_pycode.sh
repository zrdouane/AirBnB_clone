#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'
YOUR_NAME="Zakaria rdouane and Abdessamad EL FADILI"

file=$(find . -name "*.py")
for file in $file; do
    echo -e "Checking style for ${GREEN}$file${NC}"
    pycodestyle "$file"
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Style check passed${NC}"
    else
        echo -e "${RED}Style check failed${NC}"
    fi
done
echo -e "Script executed by: ${YELLOW}$YOUR_NAME${NC}"