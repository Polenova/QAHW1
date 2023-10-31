class User ():

    first_name = ""
    last_name = ""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def user_name (self):
        print(self.first_name)

    def user_last_name (self):
        print(self.last_name)

    def user_full_name (self):
        print("user: ", self.first_name, " ", self.last_name)