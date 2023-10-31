from address import Address

class Mailing ():
    to_address = Address
    from_address = Address
    cost = 1111
    track = "track"

    def __init__(self, track, cost):
        self.track = track
        self.cost = cost
        
    def addAddressTo(self, to_address):
        self.to_address = to_address

    def getAddressTo (self):
        return self.to_address

    def addAddressFrom(self, from_address):
        self.from_address = from_address

    def getAddressFrom (self):
        return self.from_address

    def say_track (self):
        print("track: ", self.track)

    def say_price (self):
        print (self.cost, " r.")


