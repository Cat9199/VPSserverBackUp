#!/usr/bin/env python3

from flask import Flask
import subprocess
from datetime import datetime
import time
import os

app = Flask(__name__)

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

    # Write log entry
    with open('git_auto_commit.log', 'a') as log_file:
        log_file.write(f'{timestamp}: Git auto commit executed\n')

@app.route('/')
def index():
    return 'Git auto commit script is running in the background.'

if __name__ == "__main__":
    while True:
        git_auto_commit()
        # Sleep for 2 hours (2 * 60 * 60 seconds)
        time.sleep(2 * 60 * 60)
