from NPC.person import *


class SimpleBuyer(Person):

    def __init__(self, type_product):
        super().__init__(type_product)
        Person.money = 45
        Person.experience = 10
        Person.max_mood_time = 25

    def go_shop(self):
        return 'Обычный покупатель заходит в  магазин. Он хочет ' + str(self.define_type_product())
