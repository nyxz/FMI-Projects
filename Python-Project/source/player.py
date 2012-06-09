#!/usr/bin/env python

import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('images/player.png')
        self.rect = pygame.rect.Rect((50, 50), self.image.get_size())

    def move(self, tick):
        step = 300 * tick
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= step
        if key[pygame.K_RIGHT]:
            self.rect.x += step
        if key[pygame.K_UP]:
            self.rect.y -= step
        if key[pygame.K_DOWN]:
            self.rect.y += step

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

        

    def update(self, tick, game):
        last_position = self.rect.copy()
        self.move(tick)
        self.colliusion_detection(game, last_position)
