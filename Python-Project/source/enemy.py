#!/usr/bin/env python 

import pygame
import gun
import random

class Enemy(pygame.sprite.Sprite):

    GIFTS = ('p100', 'p200', 'p300', 'gun', 'shield', 'heal')
    image_1 = pygame.image.load('images/enemy_1.png')
    image_2 = pygame.image.load('images/enemy_2.png')
    image_3 = pygame.image.load('images/enemy_3.png')
    image_4 = pygame.image.load('images/enemy_4.png')
    images = {1:image_1, 2:image_2, 3:image_3, 4:image_4}
    health_level = {1:200, 2:250, 3:300, 4:350}
    dmg_levels = ((25, 30), (30, 45), (45, 65), (65, 90))
    gun_min_speed = 150 
    gun_max_speeds = {1:300, 2:350, 3:400, 4:450}
    move_speed = 100
    gun_cooldown_range = (1.0, 5.0)
    gun_type = 'red'
    gun_direction = 1
    direction = 1
    gun_cooldown = 4 
    gun_bullets_rate = 800


    def __init__(self, location, game_level, *groups):
        
        self.bonus = self.__get_rand_bonus__()
        super(Enemy, self).__init__(*groups)
        self.level = game_level
        self.image = self.images.get(self.level)
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.health = self.health_level.get(self.level)
        self.dmg_level = self.dmg_levels[0]
        self.radius = 22


    def __collide_controller(self, game, last):
        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell_rect = cell.rect
            if last.right <= cell_rect.left \
                    and new.right > cell_rect.left \
                    and cell_rect.left > 100 \
                    and self.direction == 1: 
                self.direction = -1
            if last.left >= cell_rect.right \
                    and new.left < cell_rect.right \
                    and cell_rect.right < 1000 \
                    and self.direction == -1: 
                self.direction = 1


    def __movement(self, tick):
        self.rect.x += self.direction * self.move_speed * tick


    def __shoot(self, game, dt):
        rand = random.randint(1, 1000)
        if rand > self.gun_bullets_rate and not self.gun_cooldown:
            gun_dmg = self.gun_dmg_by_level() 
            gun_speed = random.randint(
                    self.gun_min_speed, 
                    self.gun_max_speeds.get(self.level)
                    ) 
            gun.Gun(
                    self.gun_type, 
                    gun_dmg, 
                    gun_speed, 
                    True, 
                    self.rect.midtop, 
                    self.gun_direction, 
                    game.sprites
                    )
            self.gun_cooldown = random.uniform(
                    self.gun_cooldown_range[0], 
                    self.gun_cooldown_range[1]
                    ) 
        self.gun_cooldown = max(0, self.gun_cooldown - dt)


    def gun_dmg_by_level(self):
       self.dmg_level = self.dmg_levels[self.level - 1]
       rand = random.randint(self.dmg_level[0], self.dmg_level[1])
       return rand


    def __get_rand_bonus__(self):
        num = random.randint(0, 100)
        if num <= 30:
            return self.GIFTS[0]
        if num <= 55:
            return self.GIFTS[1]
        if num <= 75:
            return self.GIFTS[2]
        if num <= 85:
            return self.GIFTS[3]
        if num <= 95:
            return self.GIFTS[4]
        if num <= 100:
            return self.GIFTS[5]



    def update(self, tick, game):
        last_position = self.rect.copy()
        self.__movement(tick)
        self.__shoot(game, tick)
        self.__collide_controller(game, last_position)
