

import os
import random
import subprocess

from github import Github

from github import Auth

auth = Auth.Token(subprocess.run(["gh", "auth", "token"], stdout=subprocess.PIPE, encoding="utf-8").stdout.strip())
github = Github(auth=auth)

repository = 'sbrunner/test-github-app'
event_type = 'published'

published = {
    'items': [
        {
            "name": "test"
        }
    ]
}
id_ = random.randint(1, 100000)  # nosec # noqa: S311
published["id"] = id_

github_repo = github.get_repo(repository)
github_repo.create_repository_dispatch(event_type, published)  # type: ignore[arg-type]
