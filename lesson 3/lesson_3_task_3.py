from mailing import Mailing
from address import Address

new_address_to = Address (1234345, "Moskow", "Ilinka", 6, 7)
new_address_from = Address (1234345, "Moskow", "Ilinka", 34, 89)


new_track = Mailing ("666", 1000)
new_track.addAddressTo(new_address_to)
new_track.addAddressFrom(new_address_from)
new_track.say_track()
new_track.getAddressTo().say_address()
new_track.getAddressFrom().say_address()
new_track.say_price()
