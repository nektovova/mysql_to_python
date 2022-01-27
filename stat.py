import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="bots_users"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

count_selected = mycursor.rowcount
print("total rows: "count_selected)
