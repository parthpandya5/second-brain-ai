# Second Brain AI Project

This project automates the process of storing daily notes, committing them to a Git repository, and later processing them with a vector database for semantic search and other AI functionalities.

## Structure

- **daily_notes/**: Stores daily note files.
- **vector_db/**: Contains vector database code.
- **scripts/**: Utility scripts, including one to push your daily note.

## Usage

1. Create a daily note file in the `daily_notes/` folder named `Daily_Notes_YYYY-MM-DD.txt`.
2. Run the push script:
   ```bash
   python3 scripts/push_daily_note.py