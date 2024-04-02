import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''Класс для одного корабля чужих'''

    def __init__(self, ai_settings, screen):
        '''Создает одного чужого и задает его начальную позицию'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения чужого и получение прямоугольника
        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()
        # Назначение каждому новому пришельцу стартовой координаты в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной позиции пришельца
        self.x = float(self.rect.x)

    def bltime(self):
        '''Рисует сраного ксеноса в текущей позиции'''
        self.screen.blit(self.image, self.rect)
