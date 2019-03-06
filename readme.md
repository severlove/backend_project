# OVERVIEW

This program analyzes the data in several tables within the newsdata file to answer three questions including 1)The most popular articles 2) the most popular authors and 3) the days where 1% of the requsts lead to errors.

### PREPARE YOUR SOFTWARE AND DATA:

1) Install Virtual Box and Vagrant
2) Bring the Virtual Machine oniine with command **"vagrant up"**
3) Log into it with command **"vagrant ssh"**
4) Download the file newsdata.sql and unzip "_https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip_"
5) Load data cd into vagrant directory and use the command **"psql-d news -f newdata.sql"**
6) Connect to the database via **"psql -d news"**
7) Explore data _**"(\dt, \dtable, and select)"**_

### Execute Program
run program _backendvfinal.py_

### Example of Output

Top 3 Articles:

Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views


Popular Authors:

Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views


Days where more than 1% of requests lead to errors:

July      17, 2016 - 2.3% errors





