import random

import pygame
from pygame.sprite import Sprite
import os
from random import choice


class Star(Sprite):
    '''Класс для хранения звезд на фоне'''
    def __init__(self,ai_settings,screen):
        '''создает одну звезду'''
        super(Star,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения звезды и получение прямоугольника
        # Выбор случайной звезды
        way = 'images/stars'
        pictures = os.listdir(way)
        picture = f'{way}/{random.choice(pictures)}'
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def bltime(self):
        '''Рисует звезду в текущей позиции'''
        self.screen.blit(self.image, self.rect)




