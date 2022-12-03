from github import Github
import config

# Authenticate yourself
g = Github(config.USER, config.TOKEN)

# Find your repository and path of README.md
repo = g.get_user().get_repo("advent-2022")
file = repo.get_contents("README.md")

# The new contents of your README.md
content = file.content

# Update README.md
repo.update_file("README.md", "badge update", content, file.sha)
