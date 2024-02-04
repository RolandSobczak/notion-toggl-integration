from os import getenv
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path("../.env")
load_dotenv(dotenv_path)

TOGGL_API_KEY = getenv("TOGGL_API_KEY")
NOTION_API_KEY = getenv("NOTION_API_KEY")
