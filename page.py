import mysql.connector
import cursor

def dbHandle():
    conn = mysql.connector.connect(

        host="localhost",

        user="root",

        password="123456",

        charset = "utf8",

        use_unicode = False,

        database="mydatabase",

       auth_plugin="my_validate_password"
    )
    return conn
def pagination(pageNumber, pageSize):
    dbObject = dbHandle()
    mycursor = dbObject.cursor()
    firstRecord = (pageNumber -1)* pageSize
    maxRecord = pageSize
    mycursor.execute("SELECT * FROM questions LIMIT "+str(firstRecord) +","+str(maxRecord))
    result = mycursor.fetchall()
    for question in result:
        print(question)
try:
    print("Nhap so thu tu trang: ")
    a = int(input())
    print("Nhap so record tu trang: ")
    b = int(input())
    pagination(a,b)
except BaseException as e:
    print("The error is here >>>>>>>>>>", e,"<<<<<<<<<<The error is here")
