"""Simple blog using web.py"""
import web
import db

urls = (
   "/", "index",
   "/new", "newpost",
   "/(.*)", "post",
)
render = web.template.render("templates")

app = web.application(urls, globals())

class index:
    def GET(self):
        posts = db.get_posts()
        return render.site(render.index(posts))

class post:
    def GET(self, slug):
        p = db.get_post(slug)
        return render.site(render.post(p))

class newpost:
    def GET(self):
        p = web.storage(slug="", title="", body="")
        return render.site(render.edit(p))

    def POST(self):
        i = web.input(title="Untitled", body="")
        i.slug = self.generate_slug(i.title)
        db.new_post(i.slug, i.title, i.body)
        raise web.seeother("/" + i.slug)

    def generate_slug(self, title):
        slug = title.lower().replace(" ", "-")
        # TODO: if the slug is already present in database, generate new one
        return slug

if __name__ == "__main__":
    app.run()
