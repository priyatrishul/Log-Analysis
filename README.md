# Log Analysis

The purpose of this project is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program  which uses the psycopg2 module to connect to the database. This tool is used to get results for the following  queries.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors?

### Requirements

1. This project makes use of the virtual machine to run the program. Download and 
Install `VirtualBox` from [here](https://www.virtualbox.org/).
2. Download and Install `Vagrant` from [here](https://www.vagrantup.com/).
3. Download vagrant directory with VM configurations from [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).
4. Download the database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine. 

### Steps to run the program

1. cd into the vagrant directory. Start the virtual machine by running command `vagrant up`.
2. When [vagrant up] is finished running,you can run `vagrant ssh` to log in.
3. To load the data use the command `psql -d news -f newsdata.sql`.
4. Connect to the database news using `psql -d news`.
5. Create the views mentioned in the create view section.
6. Execute the program by running command `python3 log_analysis.py` to get the results.




### Create views 

```sh
CREATE VIEW articles_logs AS
SELECT articles.author,articles.title, count(log.path) AS views FROM articles,
log WHERE articles.slug = substring(log.path from 10) 
GROUP BY articles.author,articles.title ORDER BY views DESC;
```
```sh
CREATE VIEW log_error AS
SELECT time::DATE AS day, count(*) AS err_count FROM log WHERE status ='404 NOT FOUND' 
GROUP BY day ;
```

```sh
CREATE VIEW log_total AS
SELECT time::DATE AS day, count(*) AS total_count FROM log GROUP BY day;
```
