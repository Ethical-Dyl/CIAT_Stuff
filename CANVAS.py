import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CANVAS_DOMAIN = os.getenv("CANVAS_DOMAIN", "canvas.instructure.com")
ACCESS_TOKEN = os.getenv("CANVAS_ACCESS_TOKEN")
COURSE_ID = os.getenv("COURSE_ID")

if not ACCESS_TOKEN or not COURSE_ID:
    raise Exception("Missing ACCESS_TOKEN or COURSE_ID in .env file")

url = f"https://{CANVAS_DOMAIN}/api/v1/courses/{COURSE_ID}/assignments"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    assignments = response.json()
    print(f"Found {len(assignments)} assignments in course {COURSE_ID}:")
    for i, assignment in enumerate(assignments, 1):
        print(f"{i}. {assignment['name']} (ID: {assignment['id']}) | Due: {assignment['due_at']}")
else:
    print(f"Failed to fetch assignments: {response.status_code}")
    print(response.text)
