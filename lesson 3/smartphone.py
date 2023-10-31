class Smartphone ():

    phone_lable = "Lable"
    phone_index = 0
    phone_number = 123456789

    def __init__(self, phone_lable, phone_index, phone_number):
        self.phone_lable = phone_lable
        self.phone_index = phone_index
        self.phone_number = phone_number

    def about_phone (self):
        print(self.phone_lable, " ", self.phone_index, " ", self.phone_number)

    
    
