#!/usr/bin/env python 

import pygame
import gun
import random

class Enemy(pygame.sprite.Sprite):

    GIFTS = ('p100', 'p200', 'p300', 'gun', 'shield', 'heal')

    def __init__(self, location, game_level, *groups):
        
        self.image_1 = pygame.image.load('images/enemy_1.png')
        self.image_2 = pygame.image.load('images/enemy_2.png')
        self.image_3 = pygame.image.load('images/enemy_3.png')
        self.images = {1:self.image_1, 2:self.image_2, 3:self.image_3}
        self.health_level = {1:200, 2:250, 3:300}
        self.dmg_levels = ((25, 30), (30, 45), (45, 65))
        self.gun_min_speed = 150 
        self.gun_max_speeds = {1:300, 2:350, 3:400}
        self.move_speed = 100
        self.gun_cooldown_range = (1.0, 5.0)
        self.gun_type = 'red'
        self.gun_direction = 1
        self.bonus = self.__get_rand_bonus__()

        super(Enemy, self).__init__(*groups)
        self.level = game_level
        self.image = self.images.get(self.level)
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.radius = 22
        self.direction = 1
        self.gun_cooldown = 1 
        self.gun_bullets_rate = 800
        self.health = self.health_level.get(self.level)


    def __collide_controller(self, game, last):
        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell_rect = cell.rect
            if last.right <= cell_rect.left \
                    and new.right > cell_rect.left \
                    and cell_rect.left > 0:
                self.direction = -1
            if last.left >= cell_rect.right \
                    and new.left < cell_rect.right \
                    and cell_rect.right < 798:
                self.direction = 1


    def __movement(self, tick):
        self.rect.x += self.direction * self.move_speed * tick


    def __shoot(self, game, dt):
        rand = random.randint(1, 1000)
        if rand > self.gun_bullets_rate and not self.gun_cooldown:
            gun_dmg = self.__gun_dmg_by_level() 
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


    def __gun_dmg_by_level(self):
       dmg_level = self.dmg_levels[self.level - 1]
       rand = random.randint(dmg_level[0], dmg_level[1])
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
