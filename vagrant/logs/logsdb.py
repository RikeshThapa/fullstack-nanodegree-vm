# Database code for the DB Forum, full solution!

import psycopg2, bleach

DBNAME = "news"


def get_all_time_popular():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # which articles have been accessed the most?
    # return sorted list with most popular article on top
    '''
    Merge articles < logs on articles; path count ; sort in descending order
    '''
    c.execute("""SELECT path, count(path)
                 FROM log
                 WHERE path not in ('/')
                 GROUP BY path
                 ORDER BY count(path)
                 DESC limit 5;""")
    results = c.fetchall()
    db.close()
    return results

def author_ranking():
    # sum up all of the articles written by each author
    # which authors get the most page views
    # sorted list with the most popular author at the top
    # truncate the returned list
    '''
    merge logs to articles to author
    look at path of logs
    tally up how many times each book appears
    sum total of book appearance on matching author
    return top 20 of result
    '''
    return none

def error_dates():
    # on which days did more than 1% of requests lead to errors?
    # look through log column status column,
    # tally error codes by day
    # return days with errors
    '''
    Select * from logs
    group by days, into groups based on status codes [200 OK, 404 NOT FOUND]
    add new column "percentage" = status count/ total count for day
    return list of dates where percentage > 1%
    '''
    return none


def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("insert into posts values (%s)", (bleach.clean(content),))  # good
  db.commit()
  db.close()
