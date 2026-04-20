##variables a capturar en los post
class Post:
    def __init__(self, username, url, likes, comments, caption):
        self.username = username
        self.url = url
        self.likes = likes
        self.comments = comments
        self.caption = caption