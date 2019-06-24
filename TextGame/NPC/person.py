import time


class Person:
    max_mood_time = 0
    money = 0
    experience = 0

    def __init__(self, type_product):
        self.type_product = type_product

    def define_type_product(self):
        if self.type_product == 'Sideboard':
            return 'взглянуть на стол с драгоценностями'
        elif self.type_product == 'Cupboard':
            return 'примерить вещи'
