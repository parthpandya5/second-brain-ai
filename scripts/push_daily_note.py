from cgitb import text
import os
import glob
import subprocess
from datetime import datetime
from sys import stderr, stdout
from unittest import result

#specifying director for them notes namean
NOTES_DIR = os.path.join(os.getcwd(), 'daily_notes')
today = datetime.now().strftime('%Y-%m-%d')
pattern = f"Daily_Notes_{today}*.txt"  # e.g., Daily_Notes_2025-03-01.txt

def find_daily_note():
    search_path = os.path.join(NOTES_DIR, pattern)
    files = glob.glob(search_path)
    return files[0] if files else None

def run_git_command(command):
    try:
        result = subprocess.run(command, check = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def commit_and_push(file_path):
    run_git_command(['git', 'add', file_path])
    commit_message = f"Add daily note for {today}"
    run_git_command(['git', 'commit', '-m', commit_message])
    run_git_command(['git', 'push'])

def main():
    note_file = find_daily_note()
    if note_file:
        print(f"Found daily note: {note_file}")
        commit_and_push(note_file)
    else:
        print(f"No daily note file matching pattern '{pattern}' found in {NOTES_DIR}.")

if __name__ == "__main__":
    main()