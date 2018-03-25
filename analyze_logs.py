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
cur.close()
