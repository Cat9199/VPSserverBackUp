#!/bin/bash

# Log file
LOG_FILE="/root/SiteCode/git_auto_commit.log"

# Change directory to your Git repository
cd /root/SiteCode

# Add timestamp to log
echo "Script executed at $(date +'%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"

# Add all changes
git add .

# Commit changes with a timestamped message
git commit -m "Automatic backup $(date +'%Y-%m-%d %H:%M:%S')"

# Push changes to remote repository
git push >> "$LOG_FILE" 2>&1  # Redirect both stdout and stderr to log file
