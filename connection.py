import pyodbc

class SQLTool:
    def __init__(self, server='localhost,1433', database='IMDB', username='SA', password='Passw0rd2018'):
        # Our variables to create a connection
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + '')
        self.cursor = self.conn.cursor()

    def query(self, sql_query):
        self.cursor.execute(sql_query)
