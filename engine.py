# === GHOST ENGINE v0.4 ===
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

# --- Stage 4: Function to generate a random post ---
def generate_post(sentences, questions, hashtags, emojis):
    """Generates a single, randomized post string."""
    
    # Start with a mandatory sentence
    if not sentences:
        return "Error: No sentences provided. Cannot generate a post."
    
    post_parts = [random.choice(sentences)]

    # Add other parts based on probability
    if questions and random.random() < 0.5: # 50% chance to add a question
        post_parts.append(random.choice(questions))
        
    if hashtags and random.random() < 0.4: # 40% chance to add a hashtag
        post_parts.append(random.choice(hashtags))
        
    if emojis and random.random() < 0.7: # 70% chance to add an emoji
        post_parts.append(random.choice(emojis))

    # Shuffle the parts to make the order random, then join them with spaces
    random.shuffle(post_parts)
    return " ".join(post_parts)

# --- Stage 3: Main Execution Block ---
def main():
    """The main function where the script's logic resides."""
    print("--- Ghost Engine Initializing ---")

    # Load all content from our text files into memory
    sentences = read_file_lines('sentences.txt')
    questions = read_file_lines('questions.txt')
    hashtags = read_file_lines('hashtags.txt')
    emojis = read_file_lines('emojis.txt')

    print(f"Successfully loaded {len(sentences)} sentences.")
    print(f"Successfully loaded {len(questions)} questions.")
    print(f"Successfully loaded {len(hashtags)} hashtags.")
    print(f"Successfully loaded {len(emojis)} emojis.")

    # Let's generate a test post to see if it works
    print("\n--- Generating a Test Post ---")
    test_post = generate_post(sentences, questions, hashtags, emojis)
    print(test_post)
    print("----------------------------\n")

    print("--- Ghost Engine Initialization Complete ---")


# This standard Python construct ensures that the main() function is called
# only when the script is executed directly.
if __name__ == "__main__":
    main()

# --- End of Stage 3 ---
