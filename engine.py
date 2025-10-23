import os
import random
import datetime
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# --- 1. Configuration ---
# The BLOG_ID is stored in GitHub Secrets
BLOG_ID = os.environ.get('BLOG_ID')

# --- 2. Content Generation Functions ---
def read_file_lines(file_path):
    """Reads a file and returns a list of its lines, stripped of whitespace."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except FileNotFoundError:
        return []

def generate_post_content(sentences, questions, hashtags, emojis):
    """Generates a single, randomized post content (title and body)."""
    if not sentences:
        return None, "Error: No sentences provided. Cannot generate a post."
    
    # Generate a unique title from a random sentence
    title = random.choice(sentences)
    
    # Generate the body
    body_parts = [random.choice(sentences)]
    
    if questions and random.random() < 0.5:
        body_parts.append(random.choice(questions))
    if hashtags and random.random() < 0.4:
        body_parts.append("\n\n" + random.choice(hashtags))
    if emojis and random.random() < 0.7:
        body_parts.append(random.choice(emojis))
        
    random.shuffle(body_parts)
    body = " ".join(body_parts)
    
    # Add product link
    product_url = os.environ.get('PRODUCT_URL', 'https://www.YOUR-PRODUCT-LINK-HERE.com')
    body += f"\n\n<p>---</p><p>لمعرفة المزيد عن مشروعنا، تفضل بزيارة الرابط التالي:</p><p><a href='{product_url}'>اكتشف المزيد هنا!</a></p>"
    
    return title, body

# --- 3. Blogger API Functions ---
def get_blogger_service():
    """Authenticates and returns the Blogger API service object."""
    try:
        # Load credentials from GitHub Secret
        creds_json = os.environ.get('BLOGGER_TOKEN')
        if not creds_json:
            print("Error: BLOGGER_TOKEN secret not found.")
            return None

        # The token is stored as a JSON string
        token_data = json.loads(creds_json)
        
        # Create Credentials object
        credentials = Credentials.from_authorized_user_info(info=token_data)

        # Build the service
        service = build('blogger', 'v3', credentials=credentials)
        return service
    except Exception as e:
        print(f"Authentication Error: {e}")
        return None

def insert_post(service, title, content):
    """Inserts a new post into the blog."""
    if not service:
        return False
        
    post_body = {
        'kind': 'blogger#post',
        'blog': {'id': BLOG_ID},
        'title': title,
        'content': content,
        'labels': ['GhostEngine', 'AutoPost']
    }
    
    try:
        posts = service.posts()
        # Set isDraft=True to publish as a draft first, for safety
        request = posts.insert(blogId=BLOG_ID, body=post_body, isDraft=False)
        response = request.execute()
        print(f"Successfully published post with ID: {response.get('id')}")
        print(f"Post URL: {response.get('url')}")
        return True
    except HttpError as e:
        print(f"API Error: Failed to insert post.")
        print(f"Error details: {e}")
        return False
    except Exception as e:
        print(f"General Error during post insertion: {e}")
        return False


# --- 4. Main Execution Block ---
def main():
    print("--- Ghost Engine (Blogger Mode) Initializing ---")
    
    # 1. Check for critical configuration
    if not BLOG_ID:
        print("CRITICAL ERROR: BLOG_ID environment variable is missing. Cannot proceed.")
        return

    # 2. Load Content
    sentences = read_file_lines('sentences.txt')
    questions = read_file_lines('questions.txt')
    hashtags = read_file_lines('hashtags.txt')
    emojis = read_file_lines('emojis.txt')
    
    if not sentences:
        print("CRITICAL ERROR: Content files (sentences.txt) are empty. Cannot generate post.")
        return

    # 3. Generate Post
    title, content = generate_post_content(sentences, questions, hashtags, emojis)
    if not title:
        print(content) # Print the error message
        return

    # 4. Authenticate and Publish
    service = get_blogger_service()
    if service:
        print(f"Attempting to publish to Blog ID: {BLOG_ID}")
        insert_post(service, title, content)
    else:
        print("Failed to get Blogger service. Check authentication.")

    print("--- Ghost Engine Run Complete ---")


if __name__ == "__main__":
    main()
