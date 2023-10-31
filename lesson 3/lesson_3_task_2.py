from smartphone import Smartphone

catalog = [Smartphone("nokia", 3310, 77722277), Smartphone("motorola", 30, 77522277), Smartphone("iphone", 3, 77702277),Smartphone("xaomi", 31, 7772227), Smartphone("htc", 10, 77722277)]

for i in catalog:
    print(i.about_phone())