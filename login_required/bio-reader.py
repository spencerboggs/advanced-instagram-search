import instaloader
import os
from instaloader.exceptions import TwoFactorAuthRequiredException, LoginRequiredException, InstaloaderException

# Initialize Instaloader instance
L = instaloader.Instaloader()

# Prompt for login credentials
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")

# Attempt to log in
try:
    L.login(username, password)
    print("Login successful!")
except TwoFactorAuthRequiredException:
    two_factor_code = input("Enter the 2FA code: ")
    try:
        L.two_factor_login(two_factor_code)
        print("Logged in successfully with 2FA!")
    except InstaloaderException as e:
        print(f"2FA login failed: {e}")
        exit()
except LoginRequiredException:
    print("Login is required to access profile information.")
    exit()
except InstaloaderException as e:
    print(f"Login failed: {e}")
    exit()

# Input/output files
users_file = 'user_list.txt'  # File containing the list of usernames
output_file = 'users_with_keyword.txt'  # File to save users with the keyword
keyword = input("Enter the keyword to search in bios: ").lower()

def check_and_remove_user(target_user):
    try:
        # Load the profile of the target user
        profile = instaloader.Profile.from_username(L.context, target_user)

        # Check if the keyword is in the user's bio
        bio = profile.biography.lower() if profile.biography else ""
        if keyword in bio:
            # If keyword found, write the username and profile link to output file
            with open(output_file, 'a') as out_file:
                out_file.write(f"{profile.username}: https://www.instagram.com/{profile.username}/\n")
            print(f"Keyword found in {profile.username}'s bio. Added to {output_file}.")

        # Only remove the user if there was no error
        remove_processed_user(target_user)

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"User {target_user} does not exist.")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error processing {target_user}: {e}")

def remove_processed_user(target_user):
    # Read the current list of users from the file
    with open(users_file, 'r') as file:
        users = file.readlines()

    # Remove the processed user from the list
    users = [user.strip() for user in users if user.strip() != target_user]

    # Write the remaining users back to the file
    with open(users_file, 'w') as file:
        for user in users:
            file.write(user + '\n')


# Process each user from the list
if os.path.exists(users_file):
    with open(users_file, 'r') as file:
        users = file.readlines()

    # Iterate through each user in the list and check their bio
    for user in users:
        user = user.strip()  # Clean the username (remove newlines/spaces)
        if user:  # Skip empty lines
            check_and_remove_user(user)
else:
    print(f"File {users_file} does not exist.")
