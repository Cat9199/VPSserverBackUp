#!/bin/bash

# Color codes for formatting output
HEADER_COLOR='\033[1;32m'     # Bright Green
INFO_COLOR='\033[1;33m'       # Bright Yellow
SUCCESS_COLOR='\033[1;36m'    # Bright Cyan
ERROR_COLOR='\033[1;31m'      # Bright Red
NC='\033[0m'                  # No Color

# Function to print a loader
print_loader() {
    local pid=$1
    local delay=0.1
    local spinstr='/-\|'
    while ps -p $pid > /dev/null; do
        printf "${INFO_COLOR}[${spinstr:0:1}]${NC}"
        local temp=${spinstr#?}
        spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b"
    done
}

# Function to install dependencies if requirements.txt exists
install_dependencies() {
    if [ -f "requirements.txt" ]; then
        echo -e "${INFO_COLOR}Installing dependencies from requirements.txt${NC}"
        pip install -r requirements.txt &>/dev/null
        if [ $? -eq 0 ]; then
            echo -e "${SUCCESS_COLOR}Dependencies installed successfully${NC}"
        else
            echo -e "${ERROR_COLOR}Failed to install dependencies${NC}"
            exit 1
        fi
    fi
}

# Print top company information
echo -e "${HEADER_COLOR}======================================================${NC}"
echo -e "${HEADER_COLOR}           e3lanoTopia Corporation                   ${NC}"
echo -e "${HEADER_COLOR}        Developed by Abdelrahman Nasr               ${NC}"
echo -e "${HEADER_COLOR}        GitHub: ${INFO_COLOR}https://github.com/Cat9199${NC}"
echo -e "${HEADER_COLOR}======================================================${NC}"
echo -e "${HEADER_COLOR}RunScholerSyncServers - Version 1.0 (March 2024)${NC}"
echo -e "${HEADER_COLOR}======================================================${NC}"
echo -e "${HEADER_COLOR}Time: $(date)${NC}"
echo -e "${HEADER_COLOR}======================================================${NC}"

# Reload nginx
echo -e "${INFO_COLOR}Reloading Nginx...${NC}"
sudo systemctl reload nginx
if [ $? -eq 0 ]; then
    echo -e "${SUCCESS_COLOR}Nginx reloaded successfully${NC}"
else
    echo -e "${ERROR_COLOR}Failed to reload Nginx${NC}"
    exit 1
fi

# Read JSON file
allSiteJson="allSite.json"
sites=$(jq -c '.sites[]' "$allSiteJson")

# Loop through each site and start Flask app
for site in $sites; do
    path=$(echo "$site" | jq -r '.path')
    workers=$(echo "$site" | jq -r '.workers')
    host=$(echo "$site" | jq -r '.host')
    port=$(echo "$site" | jq -r '.port')

    # Kill gunicorn processes based on the port
    echo -e "${INFO_COLOR}Killing Gunicorn processes for port $port...${NC}"
    sudo pkill -f "gunicorn.*:$port" &>/dev/null
    if [ $? -eq 0 ]; then
        echo -e "${SUCCESS_COLOR}Gunicorn processes for port $port killed successfully${NC}"
    else
        echo -e "${ERROR_COLOR}Failed to kill Gunicorn processes for port $port${NC}"
        exit 1
    fi

    # Change directory to app path
    cd "$path" || { echo -e "${ERROR_COLOR}Error: Directory $path not found${NC}"; exit 1; }

    # Install dependencies if requirements.txt exists
    install_dependencies

    # Start Flask app using Gunicorn
    echo -e "${INFO_COLOR}Starting Flask app in directory: $path on $host:$port...${NC}"
    gunicorn -w "$workers" -b "$host:$port" app:app --daemon &>/dev/null &
    gunicorn_pid=$!

    # Print loader while starting the app
    echo -ne "${INFO_COLOR}Waiting for Flask app to start..."
    print_loader $gunicorn_pid

    # Check if Flask app started successfully
    if [ $? -eq 0 ]; then
        echo -e "${SUCCESS_COLOR}Flask app started successfully${NC}"
    else
        echo -e "${ERROR_COLOR}Failed to start Flask app${NC}"
    fi
done

# Print total Flask apps started
echo -e "${HEADER_COLOR}======================================================${NC}"
echo -e "${HEADER_COLOR}           Total Flask Apps Started: ${#sites[@]}          ${NC}"
echo -e "${HEADER_COLOR}======================================================${NC}"
