#!/usr/bin/env python 

import pygame

class Gun(pygame.sprite.Sprite):


    gun_1 = pygame.image.load('images/lazer_green.png')
    gun_2 = pygame.image.load('images/lazer_red.png')
    gun_imgs = {1:gun_1, 2:gun_2}
    move_speed = 300


    def __init__(self, gun, power, is_enemy, position, direction, *groups):
        super(Gun, self).__init__(*groups)
        self.image = self.__get_image_for_gun(gun)
        self.rect = pygame.rect.Rect(position, self.image.get_size())
        self.direction = direction
        self.power = power
        self.gun_life = 3
        self.is_enemy_bullet = is_enemy


    def __get_image_for_gun(self, gun):
        return self.gun_imgs.get(gun)


    def __movement(self, dt):
        self.rect.y += self.move_speed * dt * self.direction


    def __gun_life_controller(self, dt):
        self.gun_life -= dt
        if self.gun_life < 0:
            self.kill()
            return


    def __collide_controller(self, game):
        for cell in pygame.sprite.spritecollide(self, game.enemies, False):
            if not self.is_enemy_bullet and self.direction == -1:
                self.kill()
                cell.health -= self.power
                if cell.health <= 0:
                    cell.kill()
        if pygame.sprite.collide_circle(self, game.gamer) and self.is_enemy_bullet:
            self.kill()
            game.gamer.health -= self.power
            if game.gamer.health <= 0:
                game.gamer.kill()


    def update(self, tick, game):
        self.__movement(tick)
        self.__gun_life_controller(tick)
        self.__collide_controller(game)
