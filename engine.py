# === GHOST ENGINE v0.5 (Final Engine Code) ===
# This is the main script for our project.

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
        # This is not an error, it just means the file is empty or not created yet.
        return []

# --- Stage 4: Function to generate a random post ---
def generate_post(sentences, questions, hashtags, emojis):
    """Generates a single, randomized post string."""
    if not sentences:
        return "Error: No sentences provided. Cannot generate a post."
    
    post_parts = [random.choice(sentences)]

    if questions and random.random() < 0.5:
        post_parts.append(random.choice(questions))
    if hashtags and random.random() < 0.4:
        post_parts.append(random.choice(hashtags))
    if emojis and random.random() < 0.7:
        post_parts.append(random.choice(emojis))

    random.shuffle(post_parts)
    return " ".join(post_parts)

# --- Stage 5: Function to write content to a new file ---
def write_new_file(content):
    """Creates a new file with a timestamp and writes content to it."""
    # Generate a unique filename using the current UTC timestamp
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"updates/update_{timestamp}.md"
    
    # Ensure the 'updates' directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Write the content to the new file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully created new file: {filename}")
    return filename

# --- Stage 3: Main Execution Block ---
def main():
    """The main function where the script's logic resides."""
    print("--- Ghost Engine Initializing ---")

    # Load all content from our text files into memory
    sentences = read_file_lines('sentences.txt')
    questions = read_file_lines('questions.txt')
    hashtags = read_file_lines('hashtags.txt')
    emojis = read_file_lines('emojis.txt')

    # Generate a new post
    new_post_content = generate_post(sentences, questions, hashtags, emojis)
    
    # For now, we will just print it. In the final version, this will be written to a file.
    # We will add the file writing part after we set up the GitHub Action.
    # For now, let's add the product link to the post content.
    
    # IMPORTANT: We will get the product URL from GitHub Secrets later.
    # For now, we use a placeholder.
    product_url = os.environ.get('PRODUCT_URL', 'https://www.YOUR-PRODUCT-LINK-HERE.com')
    
    final_content = new_post_content + f"\n\n[Check it out!]({product_url})"

    # Write the final content to a new file
    write_new_file(final_content)

    print("--- Ghost Engine Run Complete ---")


# This standard Python construct ensures that the main() function is called
# only when the script is executed directly.
if __name__ == "__main__":
    main()
