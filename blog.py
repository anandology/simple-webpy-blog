"""Simple blog using web.py"""
import web
import db

urls = (
   "/", "index"
)
render = web.template.render("templates")

app = web.application(urls, globals())

class index:
    def GET(self):
        posts = db.get_posts()
        return render.index(posts)

if __name__ == "__main__":
    app.run()
