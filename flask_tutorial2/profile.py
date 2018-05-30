
from database import Database

class Profile():

    def __init__(self):
        self.id = None
        self.user_id = None
        self.name = None
        self.surname = None
        self.age = None

    def set_user_data(self, user_id):
        db = Database()
        db.cursor.execute("SELECT * FROM profiles WHERE user_id=\"%s\"" % user_id)
        user = db.cursor.fetchone()
        self.id, self.user_id, self.name, self.surname, self.age = user

    def print_user_data(self):
        print(self.__dict__)