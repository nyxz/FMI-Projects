#!/usr/bin/env python

import pygame
import gun
import random

class Player(pygame.sprite.Sprite):


    def __init__(self, location, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('images/player.png')
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.radius = 24
        self.gun_cooldown = 0
        self.gun_cooldown_delay = 0.4
        self.gun_direction = -1
        self.gun_type_green = 1
        self.gun_level = 1
        self.gun_powers = (25, 50)
        self.accuracy = 0
        self.score = 0
        self.total_score = 0
        self.health = 100
        self.move_speed = 300


    def __movement(self, tick):
        img_left = pygame.image.load('images/player_left.png')
        img_right = pygame.image.load('images/player_right.png')
        img_original = pygame.image.load('images/player.png')

        step = self.move_speed * tick

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.image = img_left
            self.rect.x -= step
        if key[pygame.K_RIGHT]:
            self.image = img_right
            self.rect.x += step
        if key[pygame.K_UP]:
            self.rect.y -= step
            if not (key[pygame.K_LEFT] or key[pygame.K_RIGHT]):
                self.image = img_original
        if key[pygame.K_DOWN]:
            self.rect.y += step
            if not (key[pygame.K_LEFT] or key[pygame.K_RIGHT]):
                self.image = img_original

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                self.image = img_original


    def __collide_controller(self, game, last):
        new = self.rect

        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell_rect = cell.rect
            if last.right <= cell_rect.left and new.right > cell_rect.left:
                new.right = cell_rect.left
            if last.left >= cell_rect.right and new.left < cell_rect.right:
                new.left = cell_rect.right
            if last.bottom <= cell_rect.top and new.bottom > cell_rect.top:
                new.bottom = cell_rect.top
            if last.top >= cell_rect.bottom and new.top < cell_rect.bottom:
                new.top = cell_rect.bottom

        for sprite in game.enemies.sprites():
            if pygame.sprite.collide_circle(self, sprite):
                sprite.kill()


    def __shoot(self, gun1, events, dt, game):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.gun_cooldown:
            gun_power = self.__get_gun_power()
            gun.Gun(self.gun_type_green, gun_power, False, self.rect.midtop, self.gun_direction, game.sprites)    
            self.gun_cooldown = self.gun_cooldown_delay
        self.gun_cooldown = max(0, self.gun_cooldown - dt)
        

    def __get_gun_power(self):
        rand = random.randint(self.gun_powers[0], self.gun_powers[1])
        return rand


    def update(self, tick, game):
        last_position = self.rect.copy()
        self.__movement(tick)
        self.__shoot(1, game.events, tick, game)
        self.__collide_controller(game, last_position)
