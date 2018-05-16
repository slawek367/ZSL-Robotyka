import sqlite3


class Database:

    def __init__(self):
        self.conn = None
        self.connect()
        self.cursor = self.get_cursor()
        #self.add_account("fsfsf", "test", 'testmail')

    def connect(self):
        self.conn = sqlite3.connect('database1.db')

    def get_cursor(self):
        return self.conn.cursor()

    def add_account(self, username, password, email):
        if self.get_account(username) is not None and \
                username in self.get_account(username):
            return False
        self.cursor.execute("INSERT INTO users(username, password, email) VALUES(\"%s\", \"%s\", \"%s\")" % (username, password, email))
        self.conn.commit()
        return True

    def get_account(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=\"%s\"" % username)
        user = self.cursor.fetchone()
        return user

    def get_user_password(self, username):
        self.cursor.execute("SELECT password FROM users WHERE username=\"%s\"" % username)
        password = self.cursor.fetchone()
        return password

