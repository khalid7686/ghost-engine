# === GHOST ENGINE v0.2 ===
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
            # We use a list comprehension to read lines and filter out empty ones.
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except FileNotFoundError:
        print(f"Warning: File not found at {file_path}. Returning empty list.")
        return []

# --- End of Stage 2 ---

# The rest of the code will be added here later.
