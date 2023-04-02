from settings import *
from pygame import display, event, time, mouse
from pygame import constants as py_cons
from src.modules.field import Field
from src.modules.buttons import Button
from pygame.image import save
from os import listdir

window = display.set_mode([WIDTH, HEIGHT])
display.set_caption('Генерация уровня')
clock = time.Clock()
field = Field(window, 16, 16)
refresh_button = Button(window, field.rect.w + 32, 16, 'Создать карту')
save_button = Button(window, field.rect.w + 32, 16 + CELL_SIZE // 2 + 16, 'Сохранить карту')

run = True


while run:
    for evt in event.get():
        if evt.type == py_cons.QUIT:
            run = False
        if evt.type == py_cons.MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()
            if refresh_button.check_press(mouse_pos):
                field.refresh_map()
            if save_button.check_press(mouse_pos):
                i = len(listdir('src/images/')) + 1
                save(window, f'src/images/Map{i}.png')
            field.check_press(mouse_pos)

    window.fill((255, 255, 255))
    refresh_button.update()
    save_button.update()
    field.update()
    clock.tick(FPS)
    display.update()