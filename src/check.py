import asyncio
import logging
import os

from asgiref.sync import sync_to_async

from github import Github

REPOSITORY = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GITHUB_TOKEN"]
SHA = os.environ["GITHUB_SHA"]
EVENT = os.environ["GITHUB_EVENT_NAME"]
EVENT_PATH = os.environ["GITHUB_EVENT_PATH"]
MATCHWORDS = os.environ["INPUT_MATCHWORDS"].split(',')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    g = Github(TOKEN)
    repo = await sync_to_async(g.get_repo)(REPOSITORY)
    commit = await sync_to_async(repo.get_commit)(sha=SHA)
    subject = commit.commit.message.splitlines()[0]

    result = False
    for word in MATCHWORDS:
        if word in subject:
            result = True
    print(f"::set-output name=match::{str(result).lower()}")


if __name__ == "__main__":
    asyncio.run(main())
