import pandas as pd

def export_to_excel(posts, filename="output.xlsx"):
    data = []

    for post in posts:
        data.append({
            "Usuario": post.username,
            "URL": post.url,
            "Likes": post.likes,
            "Comentarios": post.comments,
            "Texto": post.caption
        })

    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)