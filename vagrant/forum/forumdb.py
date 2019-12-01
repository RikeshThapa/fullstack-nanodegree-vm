# "Database code" for the DB Forum.

import datetime
import psycopg2


DBNAME = "forum"

#POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
    db = psycopg2.connect(database = DBNAME)
    c = db.cursor()
    c.execute("SELECT content, time FROM posts order by time desc;")
    return c.fetchall()
    """Return all posts from the 'database', most recent first."""
    db.close()

def add_post(content):
    db = psycopg2.connect(database = DBNAME)
    c = db.cursor()
    c.execute("insert into posts values ('%s')" % content)
    db.commit()
    db.close()
