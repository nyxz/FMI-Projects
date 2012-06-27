#!/usr/bin/env python

import pygame
import random
import sounds


class Bonus(pygame.sprite.Sprite):

    DOWN = 1
    SPEED = 120
    GIFTS = ('p100', 'p200', 'p300', 'gun', 'shield', 'heal')
    RADIUS = 15

    p100_img = pygame.image.load('images/gifts/p100.png')
    p200_img = pygame.image.load('images/gifts/p200.png')
    p300_img = pygame.image.load('images/gifts/p300.png')
    shield_img = pygame.image.load('images/gifts/shield.png')
    heal_img = pygame.image.load('images/gifts/heal.png')
    gun_img = pygame.image.load('images/gifts/gun.png')

    images = {'p100': p100_img, 'p200': p200_img, 'p300': p300_img,
            'shield': shield_img, 'heal': heal_img, 'gun': gun_img}

    def __init__(self, type, position, *groups):
        """Initialize bonus

        The player's bonus could be additional points,
        +50 shield, +health and weapon damage bonus.

        """
        super(Bonus, self).__init__(*groups)
        self.type = type
        self.image = self.images.get(self.type)
        self.rect = pygame.rect.Rect(position, self.image.get_size())
        self.direction = self.DOWN
        self.speed = self.SPEED
        self.radius = self.RADIUS

    def __movement(self, tick):
        self.rect.y += tick * self.speed * self.direction

    def __collide_controller(self, game):
        """If bonus collide with player reward the player."""
        for gamer in game.players.sprites():
            if pygame.sprite.collide_circle(self, gamer):
                self.__reward_player(game)
                self.kill()

    def __reward_player(self, game):
        """Rewar the player with the bonus taken.

        If bonus is points (100/200/300) add them to the score.
        If bonus is weapon then add 400 point to score and add DPS.
        If health or shield add points and raise the health/shield.

        """
        if self.type == self.GIFTS[0]:
            game.gamer.score += 100
            sounds.Sound('points').play()
            return
        if self.type == self.GIFTS[1]:
            game.gamer.score += 200
            sounds.Sound('points').play()
            return
        if self.type == self.GIFTS[2]:
            game.gamer.score += 300
            sounds.Sound('points').play()
            return
        if self.type == self.GIFTS[3]:
            game.gamer.score += 400
            if game.gamer.gun_level < 3:
                game.gamer.gun_level += 1
            else:
                dmg_min = game.gamer.gun_powers[0] + 5
                dmg_max = game.gamer.gun_powers[1] + 5
                game.gamer.gun_powers = (dmg_min, dmg_max)
            sounds.Sound('weapon').play()
            return
        if self.type == self.GIFTS[4]:
            game.gamer.score += 450
            game.gamer.shield = min(100, game.gamer.shield + 50)
            sounds.Sound('shield').play()
            return
        if self.type == self.GIFTS[5]:
            game.gamer.score += 500
            health = random.randint(25, 50)
            game.gamer.health = min(100, game.gamer.health + health)
            sounds.Sound('heal').play()
            return

    def update(self, tick, game):
        self.__movement(tick)
        self.__collide_controller(game)
