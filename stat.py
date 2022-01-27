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
spytwibot_cursor = mydb.cursor()
spytwibot_cursor.execute("SELECT from Users where botname='spytwibot' and action='start'")
spytwibot_cursor_result = spytwibot_cursor.fetchall()
print("spytwibot start action: ",spytwibot_cursor_result)




