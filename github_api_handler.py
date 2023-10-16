import requests
import base64

GITHUB_API_ENDPOINT = "https://api.github.com/search/repositories?q="

def search_github(term):
    response = requests.get(GITHUB_API_ENDPOINT + term)
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
    url = f"https://api.github.com/repos/{full_name}/readme"
    response = requests.get(url)
    if response.status_code == 200:
        readme_data = response.json()
        readme_content = base64.b64decode(readme_data['content']).decode('utf-8')
        return readme_content
    return "README not found"

# print(search_github("python"))