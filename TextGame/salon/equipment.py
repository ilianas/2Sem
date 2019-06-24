import random
import time


class Equipment:
    level = 1
    approach_time = 0

    def __init__(self, types_jewelry):
        self.types_jewelry = types_jewelry

    def count_jewelry(self):
        return len(self.types_jewelry)

    def level_up(self):
        self.level += 1

    def type(self):
        return type(self).__name__

