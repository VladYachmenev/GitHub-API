import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()


class GitHubApi:
    def __init__(self):
        self.header = {"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}
        self.user_name = os.getenv('USER_NAME')
        self.repos_name = {"name": f"{os.getenv('REPOS_NAME')}"}

    def create_repos(self):
        url = "https://api.github.com/user/repos"
        response = requests.post(url, json=self.repos_name, headers=self.header)
        return response.json()

    def check_repos(self):
        url = f" https://api.github.com/users/{self.user_name}/repos"
        response = requests.get(url, headers=self.header)
        return response

    def delete_repos(self):
        url = f"https://api.github.com/repos/{self.user_name}/{self.repos_name['name']}"
        response = requests.delete(url, headers=self.header)
        return response

    def check_del_repos(self):
        url = f" https://api.github.com/repos/{self.user_name}/{self.repos_name['name']}"
        response = requests.get(url, headers=self.header)
        return response


