import sqlalchemy
import psycopg2
from sqlalchemy import create_engine

db_string = "postgres://username:password@database-1.xxxxxxxxxxx.us-east-40.rds.amazonaws.com:5432/db231"

db = create_engine(db_string)

# Create

db.execute("CREATE TABLE  data1 (id text PRIMARY KEY,title text);")
db.execute("CREATE TABLE  data2 (id text PRIMARY KEY,director text ,FOREIGN KEY(id)REFERENCES data1(id));")
db.execute("CREATE TABLE  data3 (id text PRIMARY KEY,year text ,FOREIGN KEY(id)REFERENCES data2(id));")

db.execute("INSERT INTO data1 (id,title) VALUES ('a101','avengers')")
db.execute("INSERT INTO data2 (id,director) VALUES ('a101','rosso brothers')")
db.execute("INSERT INTO data3 (id,year) VALUES ('a101','2019')")
# Read
result_set = db.execute("SELECT * FROM data1 , data2 ,data3")
for r in result_set:
    print(r)

# Update
#db.execute("UPDATE data1 SET title='Some2016Film' WHERE year='2016'")

# Delete
#db.execute("DELETE FROM data2 WHERE year='2016'")