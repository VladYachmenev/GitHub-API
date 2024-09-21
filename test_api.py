from github_api import GitHubApi


class TestGitHubApi:

    def test_api(self):
        api_git = GitHubApi()
        repos_created = api_git.create_repos()
        repos_check = api_git.check_repos()
        assert repos_created['name'] == repos_check.json()[0]['name']
        api_git.delete_repos()
        repos_check_del = api_git.check_del_repos()
        assert repos_check_del.status_code == 404
 