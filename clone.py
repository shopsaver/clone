import requests
import os

def clone_github_org_repos():
    # Prompt the user for the GitHub organization name
    org_name = input("Enter the GitHub organization name: ")

    # Make the URL to the input GitHub organization's repository page
    org_url = f"https://api.github.com/orgs/{org_name}/repos?per_page=200"

    # Send a GET request to the GitHub API
    response = requests.get(org_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        repos = response.json()

        # Clone all the repositories
        for repo in repos:
            repo_url = repo['html_url'] + '.git'
            os.system(f"git clone {repo_url}")
        print("Cloning completed.")
    else:
        print(f"Failed to fetch repositories for organization '{org_name}'")

if __name__ == "__main__":
    clone_github_org_repos()
