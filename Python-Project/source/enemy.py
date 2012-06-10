#!/usr/bin/env python 

import pygame
import gun
import random

class Enemy(pygame.sprite.Sprite):

    image_1 = pygame.image.load('images/enemy_1.png')
    image_2 = pygame.image.load('images/enemy_2.png')
    image_3 = pygame.image.load('images/enemy_3.png')
    images = {1:image_1, 2:image_2, 3:image_3}
    health_level = {1:100, 2:120, 3:150}
    dmg_levels = ((25, 30), (30, 45), (45, 65))
    move_speed = 100
    gun_type_red = 2
    gun_direction = 1

    def __init__(self, location, game_level, *groups):
        super(Enemy, self).__init__(*groups)
        self.level = game_level
        self.image = self.images.get(self.level)
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.radius = 24
        self.direction = 1
        self.gun_cooldown = 0
        self.health = self.health_level.get(self.level)


    def __collide_controller(self, game, last):
        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell_rect = cell.rect
            if last.right <= cell_rect.left and new.right > cell_rect.left and cell_rect.left > 0:
                self.direction = -1
            if last.left >= cell_rect.right and new.left < cell_rect.right and cell_rect.right < 798:
                self.direction = 1


    def __movement(self, tick):
        self.rect.x += self.direction * self.move_speed * tick


    def __shoot(self, game, dt):
        rand = random.randint(1, 1000)
        if rand > 985 and not self.gun_cooldown:
            gun_dmg = self.__gun_dmg_by_level() 
            gun.Gun(self.gun_type_red, gun_dmg, True, self.rect.midtop, self.gun_direction, game.sprites)
            self.gun_cooldown = 5
        self.gun_cooldown = max(0, self.gun_cooldown - dt)


    def __gun_dmg_by_level(self):
       dmg_level = self.dmg_levels[self.level - 1]
       rand = random.randint(dmg_level[0], dmg_level[1])
       return rand


    def update(self, tick, game):
        last_position = self.rect.copy()
        self.__movement(tick)
        self.__shoot(game, tick)
        self.__collide_controller(game, last_position)
