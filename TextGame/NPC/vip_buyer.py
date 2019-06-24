from NPC.person import *


class VipBuyer(Person):

    def __init__(self, type_product):
        super().__init__(type_product)
        Person.money = 60
        Person.experience = 15
        Person.max_mood_time = 20

    def go_shop(self):
        return 'Vip покупатель заходит в  магазин. Он хочет ' + str(self.define_type_product())
