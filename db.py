"""The database library for simple blog.
"""
import web

db = web.database(dbn="sqlite", db="blog.db")

def get_posts():
    return db.select("post", order="created desc")

def get_post(slug):
    return db.where("post", slug=slug).first()

def new_post(slug, title, body):
    db.insert("post", slug=slug, title=title, body=body)


