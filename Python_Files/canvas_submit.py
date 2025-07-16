"""
This file is still in testing, please feel free to fork and make improvements.

API Documentation: https://canvas.instructure.com/doc/api/
Assignment Documentation: https://canvas.instructure.com/doc/api/assignments.html
File Documentation: https://canvas.instructure.com/doc/api/files.html
Submission Documentation: https://canvas.instructure.com/doc/api/submissions.html
"""

import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()
CANVAS_DOMAIN = os.getenv("CANVAS_DOMAIN")
ACCESS_TOKEN = os.getenv("CANVAS_ACCESS_TOKEN")
COURSE_ID = os.getenv("COURSE_ID")

headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

def parse_repo_input(repo_input):
    """
    This function allows you to enter in your repo standalone - or via full URL:
    My-Github/my_repo or https://github.com/My-Github/my_repo
    """
    m = re.search(r'github\.com[:/](?P<user>[^/]+)/(?P<repo>[^/]+)', repo_input)
    if m:
        return m.group('user'), m.group('repo')
    parts = repo_input.strip().split("/")
    if len(parts) == 2:
        return parts[0], parts[1]
    raise ValueError("Enter repo as 'user/repo' or full URL.")

def list_github_folder_files(user, repo, folder, branch="main"):
    url = f"https://api.github.com/repos/{user}/{repo}/contents/{folder}?ref={branch}"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception(f"Failed to list files in folder: {resp.text}")
    files = [f for f in resp.json() if f['type'] == 'file']
    return [f['download_url'] for f in files]

def download_from_github(download_url, local_path):
    r = requests.get(download_url)
    if r.status_code == 200:
        with open(local_path, "wb") as f:
            f.write(r.content)
        print(f"Downloaded {local_path}")
    else:
        raise Exception(f"Failed to download {download_url}")

def upload_file_to_canvas(local_file_path):
    """
    Upload files into canvas via the API.
    """
    url = f"https://{CANVAS_DOMAIN}/api/v1/courses/{COURSE_ID}/files"
    params = {
        "name": os.path.basename(local_file_path),
        "parent_folder_path": "/",
        "overwrite": True
    }
    r = requests.post(url, headers=headers, params=params)
    if r.status_code != 200:
        raise Exception(f"File upload start failed: {r.text}")
    upload_url = r.json()['upload_url']
    upload_params = r.json()['upload_params']

    with open(local_file_path, 'rb') as f:
        upload_files = {'file': f}
        r2 = requests.post(upload_url, data=upload_params, files=upload_files)
        if r2.status_code not in [200, 201, 302]:
            raise Exception(f"File data upload failed: {r2.text}")

        if 'id' in r2.json():
            file_id = r2.json()['id']
        else:
            confirm_url = r2.headers.get('Location')
            r3 = requests.get(confirm_url, headers=headers)
            file_id = r3.json()['id']
    print(f"Uploaded file {local_file_path}, file_id={file_id}")
    return file_id

def submit_assignment(assignment_id, file_ids):
    """
    Submit the uploaded files into canvas via the API.
    """
    url = f"https://{CANVAS_DOMAIN}/api/v1/courses/{COURSE_ID}/assignments/{assignment_id}/submissions"
    data = {
        "submission[submission_type]": "online_upload",
        "submission[file_ids][]": file_ids
    }
    r = requests.post(url, headers=headers, data=data)
    if r.status_code == 200:
        print("Submission successful!")
    else:
        print(f"Submission failed: {r.status_code}")
        print(r.text)

def main():
    """
    Main function, 
    """
    assignment_id = input("Enter the Canvas ASSIGNMENT_ID: ").strip()
    repo_url = input("Enter your GitHub repo or full URL): ").strip()
    folder_path = input("Enter the GitHub folder path (e.g. My_Stuff/python_files): ").strip()
    branch = input("Enter branch name (default: main): ").strip() or "main"
    user, repo = parse_repo_input(repo_url)
    download_urls = list_github_folder_files(user, repo, folder_path, branch)
    file_ids = []
    for download_url in download_urls:
        filename = os.path.basename(download_url)
        download_from_github(download_url, filename)
        file_id = upload_file_to_canvas(filename)
        file_ids.append(file_id)
    submit_assignment(assignment_id, file_ids)

if __name__ == "__main__":
    main()
