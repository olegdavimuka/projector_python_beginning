import requests


def get_repository_info(repo_name: str) -> dict[str, str]:
    response = requests.get(f"https://api.github.com/repos/{repo_name}")

    if response.status_code != 200:
        return {"error": f"Failed to fetch repository details. Status code: {response.status_code}"}

    data = response.json()

    return {
        "Repository Name": data.get("name", "N/A"),
        "Owner": data.get("owner", {}).get("login", "N/A"),
        "Description": data.get("description", "N/A"),
        "License": data.get("license", {}).get("name", "No license") if data.get("license") else "No license",
        "Creation Date": data.get("created_at", "N/A"),
    }

def get_recent_commits(repo_name: str) -> list[dict[str, str]]:
    response = requests.get(f"https://api.github.com/repos/{repo_name}/commits", params={"per_page": 5})

    if response.status_code != 200:
        return [{"error": f"Failed to fetch commits. Status code: {response.status_code}"}]

    commits = response.json()

    commit_info = []
    for commit in commits:
        commit_info.append({
            "Commit Message": commit.get("commit", {}).get("message", "N/A"),
            "Author": commit.get("commit", {}).get("author", {}).get("name", "N/A"),
            "Date": commit.get("commit", {}).get("author", {}).get("date", "N/A"),
            "Commit URL": commit.get("html_url", "N/A"),
        })

    return commit_info