"""Simple blog using web.py"""
import web
import db

urls = (
   "/", "index",
   "/(.*)", "post"
)
render = web.template.render("templates")

app = web.application(urls, globals())

class index:
    def GET(self):
        posts = db.get_posts()
        return render.index(posts)

class post:
    def GET(self, slug):
        p = db.get_post(slug)
        return render.post(p)

if __name__ == "__main__":
    app.run()
