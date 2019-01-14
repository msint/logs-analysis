#!/usr/bin/env python3

# Author: May Wong
# Email: msg2may@gmail.com
# Full Stack Web Development Nano Degree Program

import psycopg2

DBNAME = "news"


def most_popular_articles(c):

    """Find the most popular three articles of all time."""
    sqlQuery = """select articles.title, count(log.path) as views\
                    from articles, log\
                    where log.status='200 OK' and\
                    log.path like '%' || articles.slug || '%'\
                    group by articles.title\
                    order by views desc\
                    limit 3"""
    c.execute(sqlQuery)
    most_popular_articles = c.fetchall()
    return most_popular_articles


def most_popular_authors(c):

    """Find the most popular article authors of all time."""
    sqlQuery = """select authors.name, count(log.path) as views\
                    from articles, log, authors\
                    where log.status=\'200 OK\' and\
                    log.path like '%' || articles.slug || '%' and\
                    articles.author = authors.id
                    group by authors.name\
                    order by views desc"""

    c.execute(sqlQuery)
    most_popular_article_authors = c.fetchall()
    return most_popular_article_authors


def error_days(c):

    """Find the days with more than 1% of requests lead to errors."""
    """This code made use of the view errorview."""
    """create view errorview as
         select time::date, count(status) as errors
         from log where status != '200 OK'
         group by time::date
         order by time::date;"""
    sqlQuery = """select to_char(log.time::date, 'Month DD, YYYY') as date, \
                    round(((errorview.errors*1.0\
                    /count(log.time::date)*1.0)*100.0)::numeric,1) as error\
                    from log, errorview\
                    where errorview.time = log.time::date\
                    group by log.time::date, errorview.errors\
                    having (errorview.errors*1.0/count(log.time::date)*1.0)\
                    *100.0 > 1.0"""
    c.execute(sqlQuery)
    days_of_error = c.fetchall()
    return days_of_error


def main():

    """Main program connects to PostgreSQl database and executes the query."""
    db = None
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()

        popular_articles = most_popular_articles(c)
        popular_authors = most_popular_authors(c)
        days_with_error = error_days(c)

        print("----------------------------------------")
        print("Most popular three articles of all time:")
        print("----------------------------------------")
        for article in popular_articles:
            ar, num = article
            print(ar + " - " + str(num) + " views")
        print("")

        print("-----------------------------------")
        print("Most popular authors of all time:")
        print("-----------------------------------")
        for author in popular_authors:
            au, numb = author
            print(au + " - " + str(numb) + " views")
        print("")

        print("-------------------------------------------------------")
        print("The days with more than 1% of requests lead to errors:")
        print("-------------------------------------------------------")
        for day in days_with_error:
            dateStr, percent = day
            print(dateStr + " - " + str(percent) + "% errors")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if db is not None:
            db.close()


main()
