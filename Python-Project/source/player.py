#!/usr/bin/env python

import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, location, gun, gun_level, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('images/player.png')
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.radius = 24


    def move(self, tick):
        img_left = pygame.image.load('images/player_left.png')
        img_right = pygame.image.load('images/player_right.png')
        img_original = pygame.image.load('images/player.png')
        step = 300 * tick
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
            

    def colliusion_detection(self, game, last):
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


    def shoot(self, gun, events):
        for event in events: 
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                print("Boom boom")
        # gun.shoot()
        

    def update(self, tick, game):
        last_position = self.rect.copy()
        self.move(tick)
        self.shoot(1, game.events)
        self.colliusion_detection(game, last_position)
