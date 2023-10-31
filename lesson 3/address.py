class Address ():
    
    mail_index = 111111
    city = "City"
    street = "Street"
    house = 234
    apartment = 1

    def __init__(self, mail_index, city, street, house, apartment):
        self.mail_index = mail_index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def say_address (self):
        print (self.mail_index, " ", self.city, " ", self.street, " ", self.house, " - ", self.apartment)


