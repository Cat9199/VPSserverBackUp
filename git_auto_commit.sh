#!/bin/bash

# Change directory to your Git repository
cd /root/SiteCode

# Add all changes
git add .

# Commit changes with a timestamped message
git commit -m "Automatic backup $(date +'%Y-%m-%d %H:%M:%S')"

# Push changes to remote repository
git push
