import random
from settings import *

class LevelMap:
    def __init__(self):
        self.map = []
        self.dict = {}
        self.bad_points = [
            round(COLUMNS / 2),
            round(ROWS * COLUMNS / 2) - COLUMNS // 2 + 1,
            round(ROWS * COLUMNS / 2) + round(COLUMNS / 2),
            ROWS * COLUMNS - COLUMNS // 2
        ]
        print(self.bad_points)
        self.generate_map()
    
    def generate_map(self):
        self.map = ['#' for i in range(ROWS * COLUMNS)]
        self.dict = {
            "enemies_cnt": [random.randint(1, 3), 'E'],
            "h_potion_cnt": [random.randint(0, 1), 'H'],
            "s_potion_cnt": [random.randint(0, 1), 'P'],
            "spikes_cnt": [random.randint(1, 3), 'S'],
            "walls_cnt": [random.randint(1, 10), 'W'],
            "chests_cnt": [random.randint(0, 1), 'C']
        }
        for key in self.dict.keys():
            count, char = self.dict[key]
            for i in range(count):
                self.set_value(char)
    
    def set_value(self, value):
        index = random.randint(0, len(self.map) - 1)
        while (self.map[index] != '#') or ((index + 1) in self.bad_points):
            index = random.randint(0, len(self.map) - 1)
        self.map[index] = value
    
    def __call__(self, index: int) -> list:
        return self.map[index]

    def __str__(self):
        map = ', '.join(self.map)
        return f'[{map}]'
