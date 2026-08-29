from mastodon import Mastodon
from datetime import date
import os

# get today's word from file war-and-peace.txt
# starting the count from 2026-8-29.
word: str
with open("./war-and-peace.txt", "r") as file:
    day: int = (date.today() - date(2026, 8, 29)).days
    word = file.readlines()[day].replace("\n", "")

# post it on mastodon
mastodon: Mastodon = Mastodon(
        access_token = os.environ["API_SECRET"],
        api_base_url = "https://mastodon.social"
    )
mastodon.status_post(word)

