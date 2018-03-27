#! /usr/bin/env python2.7

import psycopg2


def execute_query(query):
    # connect to news db
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    db.close()
    return rows


def print_result(rows, type):
    for row in rows:
        print "%s \t %s %s" % (row[0], row[1], type)

# popular three articles
query1 = ("select articles.title, views_stat.valid_view "
          "from articles, views_stat "
          "where views_stat.path like CONCAT('%', articles.slug) "
          "order by views_stat.valid_view DESC "
          "limit 3")
print "\t most popular three articles"
print_result(execute_query(query1), "views")

# most popular article authors
query2 = ("select authors.name, top_writers.sum "
          "from authors, top_writers "
          "where authors.id = top_writers.author "
          "order by top_writers.sum DESC")
print "\n\t most popular article authors"
print_result(execute_query(query2), "views")

# On which days did more than 1% of requests lead to errors
query3 = ("select time, percent from log_percent "
          "where percent > 1")
print "\n\t 1% requests errors "
print_result(execute_query(query3), "errors")
