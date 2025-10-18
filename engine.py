# === GHOST ENGINE v0.3 ===
# This is the main script for our project.
# We will build it step by step.

# --- Stage 1: Importing necessary libraries ---
import os
import random
import datetime

# --- Stage 2: Function to read content files ---
def read_file_lines(file_path):
    """Reads a file and returns a list of its lines, stripped of whitespace."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except FileNotFoundError:
        print(f"Warning: File not found at {file_path}. Returning empty list.")
        return []

# --- Stage 3: Main Execution Block ---
def main():
    """The main function where the script's logic resides."""
    print("--- Ghost Engine Initializing ---")

    # Load all content from our text files into memory
    sentences = read_file_lines('sentences.txt')
    questions = read_file_lines('questions.txt')
    hashtags = read_file_lines('hashtags.txt')
    emojis = read_file_lines('emojis.txt')

    # For now, let's just print a confirmation to see if it worked.
    print(f"Successfully loaded {len(sentences)} sentences.")
    print(f"Successfully loaded {len(questions)} questions.")
    print(f"Successfully loaded {len(hashtags)} hashtags.")
    print(f"Successfully loaded {len(emojis)} emojis.")

    print("--- Ghost Engine Initialization Complete ---")


# This standard Python construct ensures that the main() function is called
# only when the script is executed directly.
if __name__ == "__main__":
    main()

# --- End of Stage 3 ---
