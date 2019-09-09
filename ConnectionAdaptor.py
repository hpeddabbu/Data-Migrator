# implementing connection adaptor
import pymysql

pymysql.install_as_MySQLdb()


class MysqlConnectionAdaptor:
    def initConnectionToMysql(self):
        print("Hi Welcome, Please Enter Valid credentials.")
        try:

            db = pymysql.connect(user=input("Please enter the Username:"),
                             password=input("Please enter the password:"),
                             host=input("Please enter the hostname:"),
                             db=input("Please enter the database:") )
            cur = db.cursor()

            cur.execute('select * from instagram')
            for row in cur.fetchall():
                print(row)
            cur.close()
            db.close()
        except:
            
            print("Failed!!please enter valid credentials")
            self.initConnectionToMysql()
            print("connection to database is sucssfull")




