# Task Automation: Get the title of a fixed webpage.
# One-time setup in VS Code terminal: python -m pip install requests

import re
from html import unescape

try:
    import requests
except ImportError:
    print("The requests package is missing.")
    print("Install it by running: python -m pip install requests")
    raise SystemExit

URL = "https://example.com"

try:
    response = requests.get(URL, timeout=15)
    response.raise_for_status()
    match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)

    if match:
        title = unescape(match.group(1).strip())
        with open("webpage_title.txt", "w", encoding="utf-8") as file:
            file.write(f"URL: {URL}\nTitle: {title}\n")
        print("Webpage title:", title)
        print("Saved to webpage_title.txt")
    else:
        print("Could not find a title on this webpage.")
except requests.RequestException as error:
    print("Could not access the webpage:", error)
