from salon.salon import *
from salon.equipment import *
from itertools import groupby


class Cupboard(Equipment):
    numb_jewelry = {}

    def __init__(self, types_jewelry):
        super().__init__(types_jewelry)
        Equipment.__approach_time = 0.6
        self.numb_jewelry = self.__sort_jewelry()

    def __sort_jewelry(self):
        numb = []
        for i in range(self.count_jewelry()):
            numb.append(len(self.types_jewelry[i]))
        no_dif_numb = [el for el, _ in groupby(numb)]
        numb_jewelry = {key: [] for key in sorted(no_dif_numb)}
        for i in range(self.count_jewelry()):
            numb_jewelry[numb[i]].append(self.types_jewelry[i])
        return numb_jewelry

    def __generate_jewelry(self):
        keys_jewelry = list(self.numb_jewelry.keys())
        count_jewelry = len(keys_jewelry)
        interval_a = 1
        interval_b = count_jewelry / self.level if count_jewelry / self.level > 1 else 1
        number_random = random.randint(interval_a, interval_b) - 1
        random_list_jewelry = self.numb_jewelry.get(keys_jewelry[number_random])
        return random_list_jewelry[random.randint(1, len(random_list_jewelry)) - 1]

    def play(self, person):
        random_jewelry = self.__generate_jewelry()
        random_concat_word = sorted(list(random_jewelry), key=lambda a: random.random())
        start_play_time = time.time()
        while True:
            if (time.time() - start_play_time) >= person.max_mood_time:
                return False
            try:
                print('Составьте слово из букв:')
                for i in random_concat_word:
                    print(i, end=" ")
                print('\r')
                word = str(input()).replace(' ', '')
                if word == random_jewelry:
                    print('Верно! ', end="")
                    return True
                else:
                    print('Неверно!')
                time.sleep(0.4)
            except ValueError:
                print('Вы ввели не слово')
                time.sleep(0.4)

    def type_and_level(self):
        return 'Шкаф с одеждой ' + str(self.level) + ' уровня'
