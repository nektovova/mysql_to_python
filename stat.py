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

#считаем все строки
count_selected = mycursor.rowcount
print("total rows: ",count_selected)

#сколько start у бота spytwibot
mycursor.execute("SELECT * FROM Users where botname='spytwibot' and action='start'")
myresult = mycursor.fetchall()
count_selected = mycursor.rowcount
print("spytwibot start action: ",count_selected)

#сколько start у бота jpegerbot
mycursor.execute("SELECT * FROM Users where botname='jpegerbot' and action='start'")
myresult = mycursor.fetchall()
count_selected = mycursor.rowcount
print("jpegerbot start action: ",count_selected)




