from salon.sideboard import *
from salon.cupboard import *

price_sideboard = 250
price_cupboard = 200
price_upgrade_sideboard = 70
price_upgrade_cupboard = 75


class MoneyError(Exception):
    def __init__(self, text=''):
        self.txt = text


class Salon:

    equipments = []

    def __init__(self, money, experience):
        self.money = money
        self.experience = experience

    def up_money(self, money):
        self.money += money

    def up_experience(self, experience):
        self.experience += experience

    def count_equipments(self):
        return len(self.equipments)

    def count_money(self):
        return 'Вы имеете ' + str(self.money) + ' монет'

    def build_equipment(self, type_equipment, types_jewelry):
        try:
            if type_equipment == 1:
                if self.money < price_sideboard:
                    raise MoneyError()
                else:
                    self.money -= price_sideboard
                    equipment = Sideboard(types_jewelry)
                    self.equipments.append(equipment)
            elif type_equipment == 2:
                if self.money < price_cupboard:
                    raise MoneyError()
                else:
                    self.money -= price_cupboard
                    equipment = Cupboard(types_jewelry)
                    self.equipments.append(equipment)
        except MoneyError:
            print('Недостаточно средств для данного оборудования')
        else:
            print('Оборудование успешно куплено')
            time.sleep(0.4)

    def upgrade_equipment(self, numb_eq):
        try:
            equipment = self.equipments[numb_eq]
            if equipment.type() == 'Sideboard':
                if self.money < price_upgrade_sideboard:
                    raise MoneyError()
                else:
                    self.money -= price_upgrade_sideboard
                    equipment.level_up()
            elif equipment.type() == 'Cupboard':
                if self.money < price_upgrade_cupboard:
                    raise MoneyError()
                else:
                    self.money -= price_upgrade_cupboard
                    equipment.level_up()
        except MoneyError:
            print('Недостаточно средств для данного улучшения')
        else:
            print('Оборудование успешно улучшено')
            time.sleep(0.4)
