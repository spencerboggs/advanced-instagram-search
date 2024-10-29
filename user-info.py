import instaloader

# Initialize Instaloader instance
L = instaloader.Instaloader()

# Function to download profile information
def get_public_profile_info(username):
    try:
        # Load the profile
        profile = instaloader.Profile.from_username(L.context, username)
        
        # Display public profile information
        print(f"Username: {profile.username}")
        print(f"Full Name: {profile.full_name}")
        print(f"Biography: {profile.biography}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts: {profile.mediacount}")
        print(f"External URL: {profile.external_url}")
        
        get_pfp = input("Download profile picture? (y/N): ")
        if get_pfp.lower() == "y":
            L.download_profilepic(profile)
            print(f"Profile picture downloaded.")
        
        get_posts = input("Download all public posts? (y/N): ")
        if get_posts.lower() == "y":
            print(f"Downloading all public posts of {username}...")
            for post in profile.get_posts():
                L.download_post(post, target=f"{username}_posts")

    except instaloader.exceptions.ProfileNotExistsException:
        print("The profile does not exist or is private.")

user = input("Enter username: ")
get_public_profile_info(user)
