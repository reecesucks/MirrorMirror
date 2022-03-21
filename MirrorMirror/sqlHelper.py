import mysql.connector


class sqlHelper:
  def __init__(self, host, user, password, database):
    self.host = host
    self.user = user
    self.password = password
    self.database = database

  def connect(self):
    mydb = mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.database
    )

  def insert(self, sql, values):
    self.connect()
    mycursor = mydb.cursor()
    mycursor.execute(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


  def get(self, sql):
    self.connect()
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

#mirrormirror
#admin
#XATRTota9b7L6yaA
#port 1433
mydb = mysql.connector.connect(
  host="mirror.cauzlu4kxune.us-east-1.rds.amazonaws.com",
  user="admin",
  password="XATRTota9b7L6yaA",
  database="mirrormirror"
)

