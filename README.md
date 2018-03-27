## log analysis
### overview
this project is a reporting tool that will use information from database.<br>
the database contains newspaper articles and server log for the site.<br>
the report mainly answer 3 questions.
###### 1. What are the most popular three articles of all time?
###### 2. Who are the most popular article authors of all time?
###### 3. On which days did more than 1% of requests lead to errors?

### database description
database contains 3 tables.<br>
- **authors** table includes information about the authors of articles. <br>

| column | type   |
|------  | :-----:|
|name    | text   |
|bio     | text   |
|id      | integer| 

- **articles** table includes the articles themselves.<br>

|column | type                     |
|------ | :-----------------------:|
 author | integer                  | 
 title  | text                     | 
 slug   | text                     | 
 lead   | text                     | 
 body   | text                     | 
 time   | timestamp with time zone |
 id     | integer                  |

- **log** table includes one entry for each time a user has accessed the site.<br>

|column | type                     |
|------ | :-----------------------:|
path   | text                      | 
 ip     | inet                     | 
 method | text                     | 
 status | text                     | 
 time   | timestamp with time zone |
 id     | integer                  |

### How to run
firstly need to install [postgresql](https://www.postgresql.org/) and [pyrhon 2.7](https://www.python.org/download/releases/2.7/) 

1. [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
2. unzip file after downloading
3. create news database ``` CREATE DATABASE news; ```
4. cd to the folder that is contain unziped file
5. load the data with this command ```psql -d news -f newsdata.sql ```

6. ### creating views
6.1 use ``` psql -d news ``` to connect to news database
6.2 create **views_stat** view
``` create view views_stat as  ```

7. cd to the project folder
8. run ``` python analyze_logs.py ```





























