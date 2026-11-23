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

    def create_user(self, username, password):
        try:
            sql = "INSERT INTO users (user_name, user_password) VALUES (%s, %s)"
            self.cursor.execute(sql, (username, password))
            self.connection.commit()
            return True
        except pymysql.err.IntegrityError:
            return False

    def close(self):
        self.cursor.close()
        self.connection.close()
