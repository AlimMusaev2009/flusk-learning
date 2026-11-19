import pymysql

class Database:
    def __init__(self, host, user, password, database):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def get_user(self, username):
        sql = "SELECT * FROM users WHERE user_name = %s"
        self.cursor.execute(sql, (username,))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()