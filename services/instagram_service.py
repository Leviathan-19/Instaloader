import instaloader
import http.cookiejar
from models.post_model import Post

class InstagramService:

    MAX_POSTS = 10  #numero de posts o publicaciones a exportar

    def __init__(self):
        self.loader = instaloader.Instaloader()

    def login_with_cookies(self, cookiefile="cookies.txt"):
        try:
            cj = http.cookiejar.MozillaCookieJar(cookiefile)
            cj.load(ignore_discard=True, ignore_expires=True)

            self.loader.context._session.cookies.update(cj)

            if self.loader.context.is_logged_in:
                print("Sesión iniciada con cookies")
            else:
                print("Cookies cargadas pero no autenticado")

        except Exception as e:
            print("Error cargando cookies:", e)

    def get_posts(self, username):
        try:
            profile = instaloader.Profile.from_username(self.loader.context, username)

            posts_data = []
            count = 0

            for post in profile.get_posts():
                if count >= self.MAX_POSTS:
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

        except Exception as e:
            print("Error obteniendo posts:", e)
            return []