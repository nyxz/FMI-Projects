#!/usr/bin/env python 

import pygame
import bonus


class Gun(pygame.sprite.Sprite):


    def __init__(self, gun, power, speed, 
            is_enemy, position, direction, *groups):

        self.gun_1 = pygame.image.load('images/lazer_green.png')
        self.gun_2 = pygame.image.load('images/lazer_red.png')
        self.gun_imgs = {'green':self.gun_1, 'red':self.gun_2}
        self.move_speed = speed 

        super(Gun, self).__init__(*groups)
        self.image = self.__get_image_for_gun(gun)
        self.rect = pygame.rect.Rect(position, self.image.get_size())
        self.direction = direction
        self.power = power
        self.gun_life = 7
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
        for enemy in game.enemies.sprites():
            if pygame.sprite.collide_circle(self, enemy) \
                    and not self.is_enemy_bullet \
                    and self.direction == -1:
                self.kill()
                enemy.health -= self.power
                if enemy.health <= 0:
                    bonus.Bonus(enemy.bonus, enemy.rect.midtop, game.sprites)
                    enemy.kill()
                    game.gamer.score += game.game_level * 1000
                    game.gamer.kills += 1
        if pygame.sprite.collide_circle(self, game.gamer) \
                and self.is_enemy_bullet:
            self.kill()
            if game.gamer.shield > 0:
                game.gamer.shield -= self.power
                if game.gamer.shield < 0:
                    game.gamer.health += game.gamer.shield
                game.gamer.shield = max(0, game.gamer.shield)
            else:
                game.gamer.health -= self.power
                game.gamer.health = max(0, game.gamer.health)
                if game.gamer.health == 0:
                    game.gamer.kill()


    def update(self, tick, game):
        self.__movement(tick)
        self.__gun_life_controller(tick)
        self.__collide_controller(game)
