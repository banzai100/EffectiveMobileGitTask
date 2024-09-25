# GitHub Repository Manager via GitHub API

This Python script interacts with the GitHub API to create, check, and delete repositories. It also includes automated
tests using `pytest`.

## Features

- Create a new public GitHub repository.
- Check if a repository already exists.
- Delete a repository.
- Automated testing using `pytest`.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` for managing environment variables
- `pytest` for testing

To install the required packages, run:

```bash
pip install -r requirements.txt
```

Environment Variables

Create a .env file in the root of your project with the following variables:

GITHUB_TOKEN=your_github_token

GITHUB_USERNAME=your_github_username

REPO_NAME=your_repo_name

Usage

The script interacts with the GitHub API using your personal access token. Make sure your token has the appropriate
permissions to create, check, and delete repositories.

To run the tests, execute:

```bash
pytest
```

Logging

Logs and errors during the GitHub API interactions are handled within the test assertions.
