import psycopg2


# connect to news db
db = psycopg2.connect("dbname=news")
cur = db.cursor()

# popular three articles
cur.execute("select articles.title, views_stat.valid_view "
            "from articles, views_stat "
            "where views_stat.path like CONCAT('%', articles.slug) "
            "order by views_stat.valid_view DESC "
            "limit 3")

rows = cur.fetchall()
print "\t most popular three articles"
for row in rows:
    print "%s \t %s views" %(row[0], row[1])
#cur.close()

# most popular article authors
cur.execute("select authors.name, top_writers.sum "
            "from authors, top_writers "
            "where authors.id = top_writers.author "
            "order by top_writers.sum DESC")

rows = cur.fetchall()
print "\n\t most popular article authors"
for row in rows:
    print "%s \t %s views" %(row[0], row[1])
cur.close()