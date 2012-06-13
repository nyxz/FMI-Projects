#!/usr/bin/env python

import pygame
import random

class Bonus(pygame.sprite.Sprite):

    DOWN = 1
    SPEED = 180
    GIFTS = ('p100', 'p200', 'p300', 'gun', 'shield', 'heal')
    RADIUS = 15

    p100_img = pygame.image.load('images/gifts/p100.gif')
    p200_img = pygame.image.load('images/gifts/p200.gif')
    p300_img = pygame.image.load('images/gifts/p300.gif')
    shield_img = pygame.image.load('images/gifts/shield.png')
    heal_img = pygame.image.load('images/gifts/heal.png')
    gun_img = pygame.image.load('images/gifts/gun.png')

    images = {'p100':p100_img, 'p200':p200_img, 'p300':p300_img, 
            'shield':shield_img, 'heal':heal_img, 'gun':gun_img}

    def __init__(self, type, position, *groups):
        super(Bonus, self).__init__(*groups)
        self.type = type
        self.image = self.images.get(self.type)
        self.rect = pygame.rect.Rect(position, self.image.get_size())
        self.direction = self.DOWN
        self.speed = self.SPEED
        self.radius = self.RADIUS

    def __movement__(self, tick):
        self.rect.y += tick * self.speed * self.direction


    def __collide_controller__(self, game):
        if pygame.sprite.collide_circle(self, game.gamer):
            self.kill
            self.__reward_player__(game)


    def __reward_player__(self, game):
        if self.type == self.GIFTS[0]:
            game.gamer.score += 100
            return
        if self.type == self.GIFTS[1]:
            game.gamer.score += 200
            return
        if self.type == self.GIFTS[2]:
            game.gamer.score += 300
            return
        if self.type == self.GIFTS[3]:
            if game.gamer.gun_level < 3:
                game.gamer.gun_level += 1
            return
        if self.type == self.GIFTS[4]:
            game.gamer.shield += 50
            return
        if self.type == self.GIFTS[5]:
            health = random.randint(25, 50)
            game.gamer.health += health 
            return


    def update(self, tick, game):
        self.__movement__(tick)
        self.__collide_controller__(game)
