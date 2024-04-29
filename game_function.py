import sys
# import random
from time import sleep
import pygame
from bullet import Bullet
# from side_shooting.side_bullets import Bullet
from alien import Alien

from star import Star


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''Обработка столкновений корабля и пришельцев'''
    # Уменьшаем лимит кораблей
    stats.ships_left -= 1
    # Очищаем список пуль и пришельцев
    aliens.empty()
    bullets.empty()
    # Создаем новый флот и новый корабль
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    # Пауза
    sleep(0.5)
    # Изменяем флаг активности игры при потере 3х кораблей
    if stats.ships_left == 0:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    print(stats.ships_left)
    print(stats.game_active)


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
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
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


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    '''Обрабатывает нажатия клавиш и события мыши'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            chek_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def chek_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    '''Запуск новой игры по нажатию кнопки Play'''
    button_cliked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_cliked and not stats.game_active:
        ai_settings.initialize_dinamic_settings()
        #Скрываем указатель мыши
        pygame.mouse.set_visible(False)
        # Сброс игровой статистики
        stats.reset_stats()
        stats.game_active = True
        # Очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats,sb, ship, aliens, bullets, play_button):
    '''Обновляет изображения на экране и отображает новый экран'''
    # При каждом проходе цикла перерисовывается экран

    # Заполнение экрана фоновым цветом
    # screen.fill(ai_settings.bg_color)

    # Поставим-ка фоном картинку
    screen.blit(ai_settings.background_image, (0, 0))
    # -----------------------------------------------------------------------------------------------------------------------
    # Здесь будет вывод всех звезд
    # for star in stars.sprites():
    #     star.bltime()
    # -----------------------------------------------------------------------------------------------------------------------
    #Вывод счета
    sb.show_score()
    # Вывод на экран всех пуль из группы bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Вывод корабля в текущей позиции
    ship.bltime()
    aliens.draw(screen)
    #Кнопка Play отображается только если игра неактивна
    if not stats.game_active:
        play_button.draw_button()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship,stats,sb, aliens, bullets):
    '''Обновляет позиции пуль и уничтожает старые пули'''
    bullets.update()
    # Удаление пуль за краем экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullets_alien_collisions(ai_settings, screen, ship,stats,sb, aliens, bullets)


def check_bullets_alien_collisions(ai_settings, screen, ship,stats,sb, aliens, bullets):
    # Обработка случаев столкновения пуль и пришельцев
    # При попадании удаляем пулю и пришельца
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points*len(aliens)
        sb.prep_score()
    # Добавляем возрождение флота
    if len(aliens) == 0:
        # Уничтожаем старые пули, создаем новый флот
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


# ------------------------------------------------------------------------------------------------------
# Для стрельбы вправо
# for bullet in bullets.copy():
#     if bullet.rect.right >= bullet.screen_rect.right:
#         bullets.remove(bullet)
# --------------------------------------------------------------------------------------------------------

def create_fleet(ai_settings, screen, ship, aliens):
    '''Функция для создания флота чужих'''
    # Создание пришельца и вычисление количества чужих кораблей в ряду
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_row = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Создание первого ряда
    for row_number in range(number_row):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    '''Вычисление количества пришельцев в ряду'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''Создает пришельца и размещает его в ряду'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    '''Определение количества рядов'''
    availiable_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(availiable_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''Проверка на достижение края и обновление позиций всех пришельцев во флоте'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Проверка коллизий корабль-пришелец
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    '''Реагирует на достижение флотом края экрана'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settigs, aliens):
    '''Опускает весь флот и меняет направление движения'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settigs.fleet_drop_speed
    ai_settigs.fleet_direction *= -1

# Блок, отвечающий за звезды-------------------------------------------------------------------------
# def create_stars(ai_settings,screen,stars):
#     '''Создает весь массив звезд'''
#     number_stars = random.randint(50,100)
#     for star_number in range(number_stars):
#         create_star(ai_settings,screen,stars)
#
# def create_star(ai_settings,screen,stars):
#     '''Создает звезду в случайной позиции'''
#     star = Star(ai_settings,screen)
#     star.rect.x = random.randint(0,ai_settings.screen_width)
#     star.rect.y = random.randint(0, ai_settings.screen_height)
#     stars.add(star)
# -----------------------------------------------------------------------------------------------------
