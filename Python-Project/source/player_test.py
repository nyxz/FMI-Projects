#!/usr/bin/python

import unittest
import pygame
from player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.group = pygame.sprite.Group()
        self.player = Player((0, 0), self.group)

    def testPlayerHasImage(self):
        self.assertNotEqual(self.player.image, None,\
               'Player does not have image')

    def testPlayerHasRect(self):
        self.assertNotEqual(self.player.rect, None,\
                'Player does not have rect')

    def testPlayerHasRadius(self):
        self.assertNotEqual(self.player.radius, None,\
                'Player does not have radius')

    def testPlayerHasNoGunCooldown(self):
        self.assertEqual(self.player.gun_cooldown, 0,\
                'Player has gun cooldown at the begining')

    def testPlayerHasGunCooldownDelay(self):
        self.assertNotEqual(self.player.gun_cooldown_delay, None,\
                'Player does not have gun delay')

    def testPlayerHasGunCooldownDelayNotZero(self):
        self.assertNotEqual(self.player.gun_cooldown_delay, 0,\
                'Player does not have gun delay zero')

    def testPlayerHasHealth(self):
        self.assertNotEqual(self.player.health, None,\
                'Player health is not set')

    def testPlayerHasShield(self):
        self.assertNotEqual(self.player.shield, None,\
                'Player shield is not set')

if __name__ == '__main__':
    unittest.main()
