import os

def main(followers_file, following_file):
    followers_file = os.path.join(os.path.dirname(__file__), followers_file)
    following_file = os.path.join(os.path.dirname(__file__), following_file)

    with open(followers_file, "r", encoding="utf-8", errors="ignore") as f:
        followers = f.read().splitlines()

    with open(following_file, "r", encoding="utf-8", errors="ignore") as f:
        following = f.read().splitlines()

    followers.sort()
    following.sort()

    not_following_back = [user for user in following if user not in followers]

    output_file = os.path.join(os.path.dirname(__file__), "not_following_back.txt")

    with open(output_file, "w", errors="ignore") as f:
        for user in not_following_back:
            f.write(user + "\n")

    # print(f"\033[94mDone! Results saved to not_following_back.txt\033[0m")
