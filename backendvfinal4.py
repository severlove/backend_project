#!/usr/bin/env python3
import psycopg2


def top_3_articles():
    '''Print top 3 articles of all time'''
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """SELECT articles.title, count(articles.title) as num
               FROM articles,log
               WHERE articles.slug = SUBSTRING(log.path, 10)
               GROUP BY title
               ORDER BY num DESC
               LIMIT 3;"""
    c.execute(query)
    results = c.fetchall()
    db.close()
    print("\nTop 3 Articles:\n")
    for i in range(len(results)):
        print "\"" + results[i][0] + "\" - " + str(results[i][1]) + " views"


def popular_authors():
    '''Print the top authors'''
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """SELECT authors.name, count(articles.author) as num
               FROM articles, log, authors
               WHERE articles.slug = SUBSTRING(log.path, 10) and
               articles.author = authors.id
               GROUP BY authors.name
               ORDER BY num DESC"""
    c.execute(query)
    results = c.fetchall()
    db.close()
    print("\nPopular Authors:\n")
    for i in range(len(results)):
        print results[i][0] + " - " + str(results[i][1]) + " views"


def errors():
    '''Print the date where more than 1% of requests cause errors'''
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """SELECT Date, Total, Error,
               (Error::float*100)/Total::float as Percent
               FROM (
               SELECT to_char(time::timestamp::date, 'Month DD, YYYY') as Date,
               count(status) as Total, sum(case when not status =
               '200 OK' then 1 else 0 end) as Error
               FROM log
               GROUP BY time::timestamp::date) as result
               WHERE(Error::float*100)/Total::float > 1.0;"""
    c.execute(query)
    results = c.fetchall()
    db.close()
    print("\nDays where more than 1% of requests lead to errors:\n")
    for i in range(len(results)):
        print(str(results[i][0]) +
              " - " + str(round(results[i][3], 1)) + "% errors")
    print("\n")


if __name__ == '__main__':
    top_3_articles()
    popular_authors()
    errors()
