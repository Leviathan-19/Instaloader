import instaloader
from models.post_model import Post
from config.settings import USERNAME, PASSWORD, MAX_POSTS

class InstagramService:

    def __init__(self):
        self.loader = instaloader.Instaloader()

    def login(self):
        self.loader.login(USERNAME, PASSWORD)

    def get_posts(self, username):
        profile = instaloader.Profile.from_username(self.loader.context, username)

        posts_data = []
        count = 0

        for post in profile.get_posts():
            if count >= MAX_POSTS:
                break

            post_data = Post(
                username=username,
                url=f"https://www.instagram.com/p/{post.shortcode}/",
                likes=post.likes,
                comments=post.comments,
                caption=post.caption
            )

            posts_data.append(post_data)
            count += 1

        return posts_data