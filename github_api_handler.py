import base64
import requests
import os
from dotenv import load_dotenv
load_dotenv()
GITHUB_API_ENDPOINT = "https://api.github.com"

# Get the access token from environment variables
access_token = os.environ.get("GITHUB_ACCESS_TOKEN")

# Set the headers for the API requests
headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github+json',
}

def get_user_repos():
    response = requests.get(f"{GITHUB_API_ENDPOINT}/user/repos", headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

def search_github(term):
    response = requests.get(f"{GITHUB_API_ENDPOINT}/search/repositories?q={term}", headers=headers)
    if response.status_code == 200:
        return response.json().get('items', [])[:10]
    return []

def extract_repo_details(repo):
    return {
        "title": repo["name"],
        "url": repo["html_url"],
        "readme": get_readme(repo["full_name"]),
        "language": repo["language"],
        "num_stars": repo["stargazers_count"],
        "author": repo["owner"]["login"]
    }

def get_readme(full_name):
    response = requests.get(f"{GITHUB_API_ENDPOINT}/repos/{full_name}/readme", headers=headers)
    if response.status_code == 200:
        readme_data = response.json()
        readme_content = base64.b64decode(readme_data['content']).decode('utf-8')
        return readme_content
    return "README not found"

