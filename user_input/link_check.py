import os
import re
import requests

def main():
    file_name = os.path.join(os.path.dirname(__file__), "not_following_back.txt")

    with open(file_name, "r", encoding="utf-8", errors="ignore") as file:
        users = file.read().splitlines()

    pattern = re.compile(r"^[a-zA-Z0-9._]{1,}$")

    with open(file_name, "w", encoding="utf-8") as file:
        for user in users:
            if not pattern.match(user):
                print(f"Invalid username: {user}")
                continue

            url = f"https://www.instagram.com/{user}/"
            response = requests.get(url)

            if response.status_code == 200:
                print(f"\033[92m{user} exists!\033[0m")
                file.write(url + "\n")
            else:
                print(f"\033[91m{user} does not exist.\033[0m")

    print(f"Results saved to {file_name}")