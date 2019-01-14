# Log Analysis Program

Author: May Wong
Email: msg2may@gmail.com

This program is to analyze the log of news articles data in PostgreSQL database.  

The program is written in Python3 code.  It connects to news database and queries the data from the tables named log, articles and authors, and from the view named errorview.

## Files/Folders require to run the program

  - newsdata.sql as provided from the course [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  - FSND-Virtual-Machine.zip Download the Virtual Machine Configuration file and unzip it. [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
  - newsanalysis_maywong.py file is the python3 code executable file for this program.

## Development Environment

   The development environment is configured and set up as described in course lecture using Virtual Machine and vagrant.

   The database is loaded using newsdata.sql

## Database

   This program uses a view named errorview as follow:

```
   create view errorview as
    select time::date, count(status) as errors
    from log where status != '200 OK'
    group by time::date
    order by time::date;
```

   This program requires to create the PostgreSQL database view errorview in database named news as described above.

## Program Design

   This program has fours functions.  

   The main function connects to news database and calls each of other three functions to query the data from the database, close the database and prints out the text data in console.

   Each of other three function takes cursor as input, query the data answering the questions in the assignment using one SQL statement and return the data.

## Directions

   - cd to your vagrant directory. For example: FSND-Virtual-Machine/vagrant
   - Run "vagrant up"
   - Run "vagrant ssh"
   - cd to "/vagrant"
   - cd to where "newsanalysis_maywong.py" file is located. In my case, I place this file under /vagrant/news directory.
   - Then run, "python newsanalysis_maywong.py"
   - The program will output the text data answering the questions in the assignment.
