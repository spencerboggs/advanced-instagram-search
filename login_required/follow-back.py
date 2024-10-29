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
    exit()

target_user = input("Enter the username of the person whose followers you want to check: ")

try:
    profile = instaloader.Profile.from_username(L.context, target_user)

    following = set(followee.username for followee in profile.get_followees())
    print(f"Number of accounts {target_user} follows: {len(following)}")

    followers = set(follower.username for follower in profile.get_followers())
    print(f"Number of followers for {target_user}: {len(followers)}")

    non_follow_back = following - followers
    if non_follow_back:
        print(f"Accounts that {target_user} follows but who do not follow them back:")
        for non_follower in non_follow_back:
            print(f" - {non_follower}")
    else:
        print(f"All accounts that {target_user} follows also follow them back.")

except LoginRequiredException:
    print("Login required to access profile information.")
except InstaloaderException as e:
    print(f"An error occurred: {e}")
