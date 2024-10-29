import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException, LoginRequiredException, InstaloaderException

L = instaloader.Instaloader()

username = input("Enter your username: ")
password = input("Enter your password: ")

try:
    L.login(username, password)
except TwoFactorAuthRequiredException:
    two_factor_code = input("Enter the 2FA code: ")
    L.two_factor_login(two_factor_code)
    print("Logged in successfully with 2FA!")
except LoginRequiredException:
    print("Login is required to access profile information.")
except InstaloaderException as e:
    print(f"An error occurred: {e}")

target_user = input("Enter username: ")
keyword = input("Enter search term: ")
print("-" * 50)

try:
    profile = instaloader.Profile.from_username(L.context, target_user)

    for follower in profile.get_followers():
        bio = follower.biography if follower.biography else ""
        if keyword.lower() in bio.lower():
            print(f"Keyword found in follower: {follower.username}")
            print(f"Bio: {bio}")
            print(f"Profile URL: https://www.instagram.com/{follower.username}/")
            print("-" * 50)
except LoginRequiredException:
    print("Login required to access profile information.")
except InstaloaderException as e:
    print(f"An error occurred: {e}")
