from pathlib import Path
from database import conn


# 1 Obter os dados
cursor = conn.cursor()
fields = ("id", "title", "content", "author")
results = cursor.execute("SELECT * FROM post;")

# for result in results:
#     print(dict(zip(fields, result)))

posts = [dict(zip(fields, post)) for post in results]

print(posts)


# 2 criar a pagina de destino do site
site_dir = Path("site")
site_dir.mkdir(exist_ok=True)


# 3 criar uma função para gerar a url com slug
def get_post_url(post):
    slug = post['title'].lower().replace(" ", "-")
    return f"{slug}.html"


# 4 renderizar a pagina index.html
index_template = Path("list.template.html").read_text()
index_page = site_dir / Path("index.html")
post_list = [
    f"<li> <a href='{get_post_url(post)}'> {post['title']} </a></li>"
    for post in posts
]
index_page.write_text(
    index_template.format(post_list="\n".join(post_list))
)


# 5 Renderizar as paginas do blog

for post in posts:
    post_template = Path("post.template.html").read_text()
    post_page = site_dir /  Path(get_post_url(post))
    post_page.write_text(post_template.format(post=post))


print("Site generated !!!")

conn.close()
