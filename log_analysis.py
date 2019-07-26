#!/usr/bin/env python3
# Log Analysis project Solution


import psycopg2
import re

DBNAME = "news"

query1 = """SELECT title, views FROM articles_logs LIMIT 3"""

query2 = """SELECT authors.name, sum(views) AS views FROM authors,
               articles_logs WHERE authors.id = articles_logs.author
               GROUP BY authors.name ORDER BY views desc"""

query3 = """SELECT to_char(log_total.day,'Month DD, YYYY'),
             round(err_count*100/total_count::decimal,2) AS error_percent
             FROM log_error,log_total WHERE log_error.day = log_total.day
             AND err_count*100 > total_count"""


def execute_query(query):

    db = None
    posts = None
    try:
        # Try connecting to database
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        # Execute the query
        c.execute(query)
        posts = c.fetchall()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # Close database connection if open
        if db is not None:
            db.close()
    return posts


def popular_articles(query):

    """ 1. What are the most popular three articles of all time? """
    posts = execute_query(query1)
    print("\nFollowing are the most popular three articles of all time\n")
    for article, views in posts:
        print('"{}" -- {} views\n'.format(article, views))


def popular_authors(query):

    """ 2. Who are the most popular article authors of all time? """
    posts = execute_query(query2)
    print("\nFollowing are the most popular article authors of all time\n")
    for author, views in posts:
        print('"{}" -- {} views\n'.format(author, views))


def error_percent(query):

    """ 3. On which days did more than 1% of requests lead to errors? """
    posts = execute_query(query3)
    print("\nDays where more than 1% of requests lead to errors\n")
    for day, percent in posts:
        print('{}--{}% errors\n'.format(re.sub(r"\s+", " ", day), percent))


if __name__ == '__main__':
    popular_articles(query1)
    popular_authors(query2)
    error_percent(query3)
