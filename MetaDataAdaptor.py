from com.migration.data.ConnectionAdaptor import 
    def getMetadataInfoFromMysql:
        cur = db.cursor()

        cur.execute('select * from instagram')
        for row in cur.fetchall():
            print(row)
        cur.close()