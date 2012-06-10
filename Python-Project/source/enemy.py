#!/usr/bin/env python 

import pygame

class Enemy(pygame.sprite.Sprite):
    image_1 = pygame.image.load('images/enemy_1.png')
    image_2 = pygame.image.load('images/enemy_2.png')
    image_3 = pygame.image.load('images/enemy_3.png')

    def __init__(self, location, level, *groups):
        super(Enemy, self).__init__(*groups)
        self.image = self.get_image_for_level(level)
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.radius = 24
        self.direction = 1

    def get_image_for_level(self, level):
        if level == 1:
            return self.image_1
        if level == 2:
            return self.image_2
        if level > 2:
            return self.image_3


    def update(self, tick, game):
        last_position = self.rect.copy()
        self.movement(tick)
        self.calusion_detection(game, last_position)


    def calusion_detection(self, game, last):
        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell_rect = cell.rect
            if last.right <= cell_rect.left and new.right > cell_rect.left and cell_rect.left > 0:
                self.direction = -1
            if last.left >= cell_rect.right and new.left < cell_rect.right and cell_rect.right < 798:
                self.direction = 1


    def movement(self, tick):
        self.rect.x += self.direction * 100 * tick
