#!/usr/bin/env python3

import subprocess
from datetime import datetime
import time
import os  # Add this import statement

def git_auto_commit():
    # Change directory to your Git repository
    repo_path = '/root/SiteCode'
    os.chdir(repo_path)

    # Add all changes
    subprocess.run(['git', 'add', '.'])

    # Commit changes with a timestamped message
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    commit_message = f'Automatic backup {timestamp}'
    subprocess.run(['git', 'commit', '-m', commit_message])

    # Push changes to remote repository
    subprocess.run(['git', 'push'])

if __name__ == "__main__":
    while True:
        git_auto_commit()
        time.sleep(60)  # Sleep for 60 seconds (1 minute)
