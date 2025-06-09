import requests
import hashlib
import json
import time

# Configuration
MEDIUM_TOKEN = "YOUR_MEDIUM_INTEGRATION_TOKEN"
USER_ID = "YOUR_MEDIUM_USER_ID"
ARTICLE_FILE = "article.md"
TITLE = "The Pause: Where Time, Emotion, and Reality Collide"
TAGS = ["DigitalNexus", "neuroscience", "quantum", "AI", "legacyclass"]
PUBLISH_STATUS = "draft"

# Read article content
with open(ARTICLE_FILE, "r", encoding="utf-8") as f:
    article_content = f.read()

# Generate SHA-256 hash
hash_object = hashlib.sha256(article_content.encode('utf-8'))
article_hash = hash_object.hexdigest()

# Append hash and timestamp
timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
footer = f"\n\n---\n**Proof of Originality:**\n- SHA-256: `{article_hash}`\n- Timestamp: `{timestamp}`\n- Verified by: [ChatGPT & Pritul]\n"
final_content = article_content + footer

# Post to Medium
headers = {
    "Authorization": f"Bearer {MEDIUM_TOKEN}",
    "Content-Type": "application/json"
}
payload = {
    "title": TITLE,
    "contentFormat": "markdown",
    "content": final_content,
    "tags": TAGS,
    "publishStatus": PUBLISH_STATUS
}
url = f"https://api.medium.com/v1/users/{USER_ID}/posts"
response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 201:
    post_url = response.json()["data"]["url"]
    print(f"Draft posted: {post_url}")
else:
    print(f"Failed to post: {response.status_code}", response.json())
