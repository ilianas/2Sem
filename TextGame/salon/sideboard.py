from salon.salon import *
from salon.equipment import *


class Sideboard(Equipment):

    def __init__(self, types_jewelry):
        super().__init__(types_jewelry)
        Equipment.__approach_time = 0.8

    def play(self, person):
        random_jewelry = self.__generate_jewelry()
        count_open_numb = 0
        start_play_time = time.time()
        while True:
            try:
                if (time.time() - start_play_time) >= person.max_mood_time:
                    return False
                print('Введите пару цифр из списка(через enter):')
                for i in list(random_jewelry.keys()):
                    if i < (self.level - 1 - count_open_numb):
                        print("%d.%s" % (i, random_jewelry.get(i)), end=" ")
                    else:
                        print(i, end=" ")
                print('\r')
                num_1 = int(input())
                num_2 = int(input())
                if (list(random_jewelry.keys()).count(num_1) == 0) or (list(random_jewelry.keys()).count(num_2) == 0):
                    raise ValueError()
                jewelry_1 = random_jewelry.get(num_1)
                jewelry_2 = random_jewelry.get(num_2)
                print(jewelry_1)
                time.sleep(0.4)
                print(jewelry_2)
                time.sleep(0.4)
                if jewelry_1 == jewelry_2:
                    random_jewelry.pop(num_1)
                    random_jewelry.pop(num_2)
                    count_open_numb += 1
                    print('Верно! ')
                else:
                    print('Неверно!')
                time.sleep(0.4)
                if len(list(random_jewelry.keys())) == 0:
                    print('Успех', end="")
                    return True
            except ValueError:
                print('Вы ввели не цифру из списка')
                time.sleep(0.4)

    def __generate_jewelry(self):
        d = {a: self.types_jewelry[int(a / 2)] for a in range(self.count_jewelry() * 2)}
        values = list(d.values())
        random.shuffle(values)
        return dict(zip(d.keys(), values))

    def type_and_level(self):
        return 'Стол с драгоценностями ' + str(self.level) + ' уровня'
