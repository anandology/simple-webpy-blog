"""Simple blog using web.py"""
import web
import db

urls = (
        "/", "index"
    )

app = web.application(urls, globals())

class index:
    def GET(self):
        posts = db.get_posts()
        output = ""
        for p in posts:
            output += "<br>" + p.title
        return output

if __name__ == "__main__":
    app.run()
