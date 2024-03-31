import sys

import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''Обработка нажатия клавиш'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings,screen,ship,bullets):
    '''Выпускает пулю, если максимум пуль не достигнут'''
    # Если количество пуль на экране меньше 3
    if len(bullets) < ai_settings.bullets_allowed:
        # Создаем пулю и включаем её в список пуль
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    '''Обработка отпускания клавиш'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings,screen,ship,bullets):
    '''Обрабатывает нажатия клавиш и события мыши'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings,screen,ship,bullets):
    '''Обновляет изображения на экране и отображает новый экран'''
    # При каждом проходе цикла перерисовывается экран
    # Заполнение экрана фоновым цветом
    screen.fill(ai_settings.bg_color)
    # Вывод на экран всех пуль из группы bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Вывод корабля в текущей позиции
    ship.bltime()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(bullets):
    '''Обновляет позиции пуль и уничтожает старые пули'''
    bullets.update()
    #Удаление пуль за краем экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)