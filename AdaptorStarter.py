from com.migration.data.ConnectionAdaptor import MysqlConnectionAdaptor


class  main():
    connection_obj = MysqlConnectionAdaptor()
    connection_obj.initConnectionToMysql()


