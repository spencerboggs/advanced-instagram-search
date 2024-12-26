import instaloader

# Initialize Instaloader instance
L = instaloader.Instaloader()

# Function to download profile information
def search_bio(username, search_term):
    try:
        # Load the profile
        profile = instaloader.Profile.from_username(L.context, username)
        
        # If the search term is in the bio, save the user to a txt file called bios.txt
        if search_term.lower() in profile.biography.lower():
            with open("bios.txt", "a") as f:
                f.write(f"--------------------\n")
                f.write(f"https://www.instagram.com/{profile.username}\n")
                f.write(f"Bio: {profile.biography}\n")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"The profile '{username}' does not exist or is private.")
    except Exception as e:
        print(f"An error occurred with '{username}': {e}")

# Input file with usernames
text_file = input("Enter a txt file: ")

# Input search term
search_term = input("Enter search term: ")

# Process each username from the text file
try:
    with open(text_file, "r", errors="ignore") as file:
        for user in file:
            # Strip trailing newline or whitespace from username
            username = user.strip()
            if username:  # Skip empty lines
                search_bio(username, search_term)
except FileNotFoundError:
    print(f"Error: File '{text_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
