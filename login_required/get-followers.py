import instaloader
from instaloader.exceptions import InstaloaderException, TwoFactorAuthRequiredException, LoginRequiredException

L = instaloader.Instaloader()

username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")

try:
    L.login(username, password)
    print("Login successful!")
except TwoFactorAuthRequiredException:
    two_factor_code = input("Enter the 2FA code: ")
    L.two_factor_login(two_factor_code)
    print("Logged in successfully with 2FA!")
except LoginRequiredException:
    print("Login is required to access profile information.")
    exit()
except InstaloaderException as e:
    print(f"Login failed: {e}")
    exit()

target_user = input("Enter the username of the target account: ")
file_name = f"{target_user}_followers.txt"

try:
    profile = instaloader.Profile.from_username(L.context, target_user)

    followers = profile.get_followers()
    print(f"Followers of {target_user}:")
    with open(file_name, 'w') as file:
        for follower in followers:
            print(follower.username)
            file.write(follower.username + '\n')

    """ with open(file_name, 'w') as file:
        for follower in profile.get_followers():
            file.write(follower.username + '\n')

    print(f"List of followers has been saved to {file_name}.") """

except InstaloaderException as e:
    print(f"An error occurred: {e}")
