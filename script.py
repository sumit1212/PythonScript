import csv
import psycopg2

conn_string = "dbname= 'PROJECTDEMO_11' user= 'sumit' password='sumit@123'"

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

reader = csv.reader(open('student_import.csv','rb'))

for row in reader:
    print(row[0],row[1])

    statement = "INSERT INTO op_category (name ,code) VALUES (%s,%s) RETURNING id"
    data = (str(row[0]),str(row[1]))
    cursor.execute(statement,data)
conn.commit()


    

