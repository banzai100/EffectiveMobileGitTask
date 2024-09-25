import requests
import json
import os
from dotenv import load_dotenv
import pytest

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = os.getenv("REPO_NAME")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

repo_data = {
    "name": REPO_NAME,
    "description": "This is a new public repository created via GitHub API",
    "private": False
}


def create_repo():
    if check_repo_exists(REPO_NAME):
        return None
    response = requests.post(
        'https://api.github.com/user/repos',
        headers=headers,
        data=json.dumps(repo_data)
    )
    return response


def check_repo_exists(repo_name):
    response = requests.get('https://api.github.com/user/repos', headers=headers)

    if response.status_code == 200:
        repos = response.json()
        repo_names = [repo['name'] for repo in repos]
        return repo_name in repo_names
    else:
        return False


def delete_repo(repo_name):
    delete_url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}'

    response = requests.delete(delete_url, headers=headers)
    return response


def test_create_repo():
    response = create_repo()
    if response is None:
        pytest.skip(f"Repository '{REPO_NAME}' already exists.")
    assert response.status_code == 201, "Failed to create repository"
    assert response.json()["name"] == REPO_NAME, "Repository name does not match"


def test_check_repo_exists():
    repo_exists = check_repo_exists(REPO_NAME)
    assert repo_exists, "Repository was not found"


def test_delete_repo():
    response = delete_repo(REPO_NAME)
    assert response.status_code == 204, "Failed to delete repository"
    repo_exists = check_repo_exists(REPO_NAME)
    assert not repo_exists, "Repository was found after deletion"
