from pygame import Rect, draw, transform, SRCALPHA
from pygame.surface import Surface
from src.modules.level_map import LevelMap
from settings import *

class Field:
    def __init__(self, screen: Surface, x: int, y: int):
        self.x, self.y = x, y
        w, h = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE
        self.rect = Rect(x, y, w, h)
        self.screen = screen
        
        self.coords = self.generate_coords()
        self.cells = []
        self.generate_cells()
        self.refresh_map()
    
    def update(self):
        self.draw()
    
    def check_press(self, mouse_pos):
        for cell in self.cells:
            cell.check_press(mouse_pos)

    def refresh_map(self):
        map = LevelMap()
        for i in range(len(self.cells)):
            self.cells[i].set_char(map(i))
    
    def generate_coords(self):
        steps_cols = self.rect.width // CELL_SIZE
        steps_rows = self.rect.height // CELL_SIZE
        return [[(self.x + i * CELL_SIZE, self.y + j * CELL_SIZE) for i in range(steps_rows)] for j in range(steps_cols)]

    def generate_cells(self):
        for row in self.coords:
            for point in row:
                self.cells.append(Cell(self.screen, point[0], point[1]))

    def draw(self):
        self.draw_cells()
        draw.rect(self.screen, BLACK, self.rect, width=3)
        self.draw_lines()
    
    def draw_cells(self):
        for cell in self.cells:
            cell.update()

    def draw_lines(self):
        steps_cols = self.rect.width // CELL_SIZE
        steps_rows = self.rect.height // CELL_SIZE
        for i in range(1, steps_rows):
            draw.line(self.screen, BLACK, (self.x, self.y + i*CELL_SIZE), (self.x + self.rect.w - 2, self.y + i*CELL_SIZE), width=3)
        for i in range(1, steps_cols):
            draw.line(self.screen, BLACK, (self.x + i*CELL_SIZE, self.y), (self.x + i*CELL_SIZE, self.y + self.rect.h - 2), width=3)


class Cell:
    def __init__(self, screen: Surface, x: int, y: int):
        self.x, self.y = x, y
        self.rect = Rect(x, y, CELL_SIZE, CELL_SIZE)
        self.surface = Surface((CELL_SIZE, CELL_SIZE), flags=SRCALPHA)
        self.screen = screen
        self.chars = ['#', 'S', 'E', 'H', 'P', 'W', 'C']
        self.char = '#'
        self.set_char('')

    def set_char(self, char):
        self.char = char
        if char == 'S':
            self.draw_function = self.draw_spike
        elif char == 'E':
            self.draw_function = self.draw_enemy
        elif char == 'H':
            self.draw_function = self.draw_heal_potion
        elif char == 'P':
            self.draw_function = self.draw_poison_potion
        elif char == 'W':
            self.draw_function = self.draw_wall
        elif char == 'C':
            self.draw_function = self.draw_chest
        else:
            self.draw_function = self.pass_draw
    
    def check_press(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            index = (self.chars.index(self.char) + 1) % len(self.chars)
            self.set_char(self.chars[index])

    def update(self):
        self.draw()

    def draw(self):
        self.surface.fill(WHITE)
        self.draw_function()
        self.screen.blit(self.surface, self.rect)
    
    def pass_draw(self):
        pass
    
    def draw_chest(self):
        self.surface.fill(GOLD)

    def draw_wall(self):
        self.surface.fill(BLACK)
    
    def draw_spike(self):
        draw.polygon(self.surface, GRAY, [
            [self.rect.w // 2, self.rect.h // 10],
            [self.rect.w // 5, self.rect.h // 1.2],
            [self.rect.w // 1.25, self.rect.h // 1.2],
        ])
    
    def draw_enemy(self):
        draw.circle(self.surface, RED,  [self.rect.w // 2, self.rect.h // 2], CELL_SIZE // 3)

    def draw_poison_potion(self):
        draw.ellipse(self.surface, GREEN, [
            self.rect.w // 4,
            self.rect.h // 10,
            self.rect.w // 4 + self.rect.w // 4,
            self.rect.h // 10 + self.rect.h // 1.4,
        ])

    def draw_heal_potion(self):
        draw.ellipse(self.surface, BROWN, [
            self.rect.w // 4,
            self.rect.h // 10,
            self.rect.w // 4 + self.rect.w // 4,
            self.rect.h // 10 + self.rect.h // 1.4,
        ])