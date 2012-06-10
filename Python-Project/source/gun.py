#!/usr/bin/env python 

import pygame

class Gun(pygame.sprite.Sprite):
    gun_1 = pygame.image.load('images/lazer_green.png')
    gun_2 = pygame.image.load('images/lazer_red.png')
    gun_imgs = {1:gun_1, 2:gun_2}

    def __init__(self, gun, level, is_enemy, position, direction, *groups):
        super(Gun, self).__init__(*groups)
        self.image = self.get_image_for_level(gun)
        self.rect = pygame.rect.Rect(position, self.image.get_size())
        self.direction = direction
        self.power = self.get_power_by_gun_level(gun, level)
        self.gun_life = 3
        self.is_enemy_bullet = is_enemy


    def get_image_for_level(self, gun):
        return self.gun_imgs.get(gun)

    def get_power_by_gun_level(self, gun, level):
        return 100 # TODO make real dmg calculation    
    
    def movement(self, dt):
        self.rect.y += 300 * dt * self.direction

    def gun_life_controller(self, dt):
        self.gun_life -= dt
        if self.gun_life < 0:
            self.kill()
            return

    def collide_controller(self, game):
        for cell in pygame.sprite.spritecollide(self, game.enemies, not self.is_enemy_bullet):
            if not self.is_enemy_bullet and self.direction == -1:
                self.kill()
        if pygame.sprite.collide_circle(self, game.gamer) and self.is_enemy_bullet:
            self.kill()
            game.gamer.kill()

    def update(self, tick, game):
        self.movement(tick)
        self.gun_life_controller(tick)
        self.collide_controller(game)
