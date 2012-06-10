#!/usr/bin/env python

import pygame


class Stats:

    def __init__(self, game):
        self.player = game.gamer
        self.p_health_pos = (860, 640)
        self.color = (200, 200, 200)
        self.stats = dict() 

    def load_player_health(self):
        pygame.font.init()
        font = pygame.font.Font(None, 18)

        health_msg = "Health: {health}".format(health = self.player.health)
        health_txt = font.render(health_msg, 1, self.color)
        self.stats.__setitem__('health', (health_txt, self.p_health_pos))

        return self.stats


class DamageBar(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super(DamageBar, self).__init__(*groups)
        self.image = pygame.image.load()
