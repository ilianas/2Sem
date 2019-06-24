from NPC.person import *
from NPC.simple_buyer import *
from NPC.vip_buyer import *
from collections import deque
from salon.salon import *
from salon.sideboard import *
import os
import random


class ClientError(Exception):
    def __init__(self, text=''):
        self.txt = text


def scan_path():
    path = './'
    text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
    if len(text_files) == 0:
        raise FileNotFoundError()
    else:
        return text_files


def read_file(file):
    inf_file = open(file)
    inf = inf_file.readlines()
    q = []
    if len(inf) == 1 and inf[0] != '\n':
        q.append(inf[0].replace(' ', ''))
    else:
        for k in inf:
            if k.replace(' ', '') == '\n':
                continue
            else:
                q.append(k.replace(' ', '')[:-1])
        inf_file.close()
        if int(len(q)) == 0:
            raise SyntaxError()
    return q


salon = Salon(600, 0)


# salon.equipments = [Cupboard(read_file('test.txt')), Sideboard(read_file('test.txt'))]


def buy_equipment():
    try:
        print(
            "Выберите тип нового оборудования или 999 для выхода:\n1. Стол с драгоценностями(%d)\n2. Шкаф с одеждой(%d)"
            % (price_sideboard, price_cupboard))
        type_eq = int(input())
        if type_eq == 999:
            return
        elif (type_eq != 1) and (type_eq != 2):
            raise ValueError()
        print('Выберите файл с продукцией для данного оборудования:')
        files = scan_path()
        for i in range(len(files)):
            print("%d. %s" % (i, files[i]))
        numb_file = int(input())
        salon.build_equipment(type_eq, read_file(files[numb_file]))
    except ValueError:
        print('Вы ввели не цифру из списка')
        time.sleep(0.4)
    except FileNotFoundError:
        print('Ни один файл не найден. Пожалуйста создайте новый файл(.txt). Слова должны идти'
              ' в колонку без пробелов')
        time.sleep(3)
    except SyntaxError:
        print('Данный файл пуст. Пожалуйста создайте новый файл(.txt). Слова должны идти'
              ' в колонку без пробелов')
        time.sleep(3)


def buy_upgrade():
    try:
        if len(salon.equipments) == 0:
            print('У вас нет оборудования')
            time.sleep(0.4)
            return
        print('Выберите оборудование для улучшения или 999 для выхода.')
        print('Улучшая стол, карты будут частично открываться на старте')
        print('Улучшая шкаф с одеждой, вам с большей вероятностью попадутся легкие слова')
        for i in range(salon.count_equipments()):
            print("%d.%s(%d монет)" % (i, salon.equipments[i].type_and_level(),
                                       price_upgrade_sideboard
                                       if salon.equipments[i].type() == 'Sideboard'
                                       else price_upgrade_cupboard))

        numb_eq = int(input())
        if numb_eq == 999:
            return
        salon.upgrade_equipment(numb_eq)
    except ValueError:
        print('Вы ввели не цифру')
        time.sleep(0.4)
    except IndexError:
        print('Вы ввели не цифру из списка')
        time.sleep(0.4)


def shop():
    try:
        while True:
            print(salon.count_money())
            print('Введите:')
            print('1.Для покупки нового оборудования')
            print('2.Для улучшения имеющегося оборудования')
            print('или 999 для выхода в главное меню')
            variant = int(input())
            if variant == 999:
                return
            elif variant == 1:
                buy_equipment()
            elif variant == 2:
                buy_upgrade()
            else:
                raise ValueError()
    except ValueError:
        print('Вы ввели не цифру из списка')
        time.sleep(0.4)


def generate_queue(count_person):
    queue = deque()
    for i in range(count_person):
        type_person = random.randint(1, 4)
        type_product = random.randint(0, 1)
        if type_product == 0:
            type_product = 'Sideboard'
        elif type_product == 1:
            type_product = 'Cupboard'
        if type_person == 1:
            person = VipBuyer(type_product)
        else:
            person = SimpleBuyer(type_product)
        queue.append(person)
    return queue


time_level = 45


def start_day(count_person):
    print('Магазин открылся.')
    time.sleep(0.4)
    queue = generate_queue(count_person)
    time_open = time.time()
    while len(queue) != 0 and (time.time() - time_open) < time_level:
        try:
            person = queue.pop()
            print(person.go_shop())
            print('Выберите оборудование для клиента:')
            for i in range(salon.count_equipments()):
                print("%d.%s" % (i, salon.equipments[i].type_and_level()))
            numb_eq = int(input())
            equipment = salon.equipments[numb_eq]
            if equipment.type() != person.type_product:
                raise SyntaxError()
            result = equipment.play(person)
            if result:
                print("Вы заработали %d монет." % person.money)
                salon.up_experience(person.experience)
                salon.up_money(person.money)
            else:
                raise ClientError()
        except ValueError:
            print('Вы ввели не цифру из списка, клиенту пришлось уйти')
            time.sleep(0.4)
        except IndexError:
            print('Вы ввели не цифру из списка, клиенту пришлось уйти')
            time.sleep(0.4)
        except SyntaxError:
            print('Клиент не хотел данный тип услуг. Ему пришлось уйти')
            time.sleep(0.4)
        except ClientError:
            print('Клиент заждался и покинул очередь')
    print('Магазин закрылся.')
    time.sleep(0.4)


def main():
    print('Добро пожаловать в игру Свадебный салон!')
    time.sleep(2)
    print('Здесь вы можете обустраивать свой салон, покупая и улучшая оборудование')
    time.sleep(3)
    print('Чтобы это было возможно сделать, необходимо зарабатывать деньги, играя в мини-игры')
    time.sleep(3)
    print('Учтите, что у клиентов могут быть разные характеристики!')
    time.sleep(3)
    print('Приятной игры!')
    time.sleep(5)
    while True:
        try:
            print('Выберите один из вариантов или 999 для выхода из игры:')
            print('1. Улучшить и купить оборудование')
            print('2. Открыть магазин для клиентов')
            numb = int(input())
            if numb == 999:
                print('Пока')
                return
            if numb == 1:
                shop()
            elif numb == 2:
                if salon.count_equipments() == 0:
                    print('У вас нет ни одного оборудования. Пожалуйста посетите магазин.')
                    time.sleep(0.4)
                    continue
                print('Насколько загруженным должен быть рабочий день от 1 до 5(где 1-не очень, 5-ужастно))')
                variant = int(input())
                if (variant <= 0) or (variant > 5):
                    raise ValueError()
                else:
                    start_day(variant * 2)
        except ValueError:
            print('Вы ввели не цифру из списка')
            time.sleep(0.4)


main()
# salon.equipments[1].play(VipBuyer('Cupboard'))
