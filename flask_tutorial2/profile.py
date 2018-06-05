
from database import Database

class Profile():

    def __init__(self, user_id):
        self.id = None
        self.user_id = user_id
        self.name = None
        self.surname = None
        self.age = None
        self.set_user_data()

    def set_user_data(self):
        db = Database()
        db.cursor.execute("SELECT * FROM profiles WHERE user_id=\"%s\"" % self.user_id)
        user = db.cursor.fetchone()
        self.id, self.user_id, self.name, self.surname, self.age = user
    
    def update_user_data(self):
        #TODO
        pass

    def print_user_data(self):
        print(self.__dict__)