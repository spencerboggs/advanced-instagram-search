import os
import followers_vs_following
import user_strip
import link_check

followers_file = input("Enter the path to the followers file: ")
following_file = input("Enter the path to the following file: ")

followers_file = followers_file.strip()
following_file = following_file.strip()

user_strip.main(followers_file)
user_strip.main(following_file)

followers_file = f'{followers_file[:-4]}-stripped.txt'
following_file = f'{following_file[:-4]}-stripped.txt'

followers_vs_following.main(followers_file, following_file)

link_check.main()

followers_file = os.path.join(os.path.dirname(__file__), followers_file)
following_file = os.path.join(os.path.dirname(__file__), following_file)

os.remove(followers_file)
os.remove(following_file)
