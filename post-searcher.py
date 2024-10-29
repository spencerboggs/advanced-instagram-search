import instaloader

L = instaloader.Instaloader()

usernames = input("Enter usernames (separated by spaces): ").split()
keyword = input("Enter search term: ")
print("-" * 50)

with open("posts.txt", "w") as file:
    file.write(f"Search term: {keyword}\n")
    for username in usernames:
        profile = instaloader.Profile.from_username(L.context, username)
        file.write(f"\nAccount: {username}\n")
        for post in profile.get_posts():
            caption = post.caption if post.caption else ""
            if keyword.lower() in caption.lower():
                file.write(f"Post URL: https://www.instagram.com/p/{post.shortcode}/\n")
                print(f"Keyword found in {username}'s post: {post.shortcode}")
