from pygame import Rect, draw, init
from pygame.font import Font
from pygame.surface import Surface
from settings import *
init()

class Button:
    def __init__(self, screen: Surface, x: int, y: int, text: str):
        self.screen = screen
        self.x, self.y = x, y
        self.global_rect = Rect(x, y, CELL_SIZE * 2, CELL_SIZE // 2)
        self.rect = Rect(0, 0, CELL_SIZE * 2, CELL_SIZE // 2)

        self.font = Font(None, 25)
        self.text_surface = self.font.render(text, True, BLACK)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.rect.center

        self.surface = Surface((CELL_SIZE * 2, CELL_SIZE // 2))

        self.was_press = False
    
    def update(self):
        self.draw()

    def draw(self):
        self.surface.fill(WHITE)
        draw.rect(self.surface, BLACK, self.rect, width=3)
        self.surface.blit(self.text_surface, self.text_rect)
        self.screen.blit(self.surface, (self.x, self.y))

    def check_press(self, mouse_pos):
        self.was_press = self.global_rect.collidepoint(mouse_pos)
        return self.was_press