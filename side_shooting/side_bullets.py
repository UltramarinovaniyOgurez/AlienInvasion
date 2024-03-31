import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Класс для управления пулями игрока'''
    def __init__(self,ai_settings,screen,ship):
        '''Создаем объект ПУЛЯ в текущей позиции корабля'''
        super(Bullet,self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #Создание пули в позиции 0,0 и назначение правильной позиции
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right
        #Позиция пули хранится в вещественном формате
        self.x = float(self.rect.x)
        #Цвет и скорость пули
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        '''Перемещение пули вправо по экрану'''
        #Обновление позиции пули в вещественном формате
        self.x += self.speed_factor
        self.rect.x = self.x


    def draw_bullet(self):
        '''Вывод пули на экран'''
        pygame.draw.rect(self.screen,self.color,self.rect)