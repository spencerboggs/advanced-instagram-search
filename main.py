import instaloader

L = instaloader.Instaloader()

username = input("Enter username: ")
keyword = input("Enter search term: ")
print("-" * 50)

profile = instaloader.Profile.from_username(L.context, username)

for post in profile.get_posts():
    caption = post.caption if post.caption else ""
    if keyword.lower() in caption.lower():
        print(f"Keyword found in post: {post.shortcode}")
        print(f"Caption: {caption}")
        print(f"Post URL: https://www.instagram.com/p/{post.shortcode}/")
        print("-" * 50)
