#!/usr/bin/python

import unittest
import pygame
from player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.group = pygame.sprite.Group()
        self.player = Player((0, 0), self.group)

    def test_player_has_image(self):
        self.assertNotEqual(self.player.image, None,\
               'Player does not have image')

    def test_player_has_rect(self):
        self.assertNotEqual(self.player.rect, None,\
                'Player does not have rect')

    def test_player_has_radius(self):
        self.assertNotEqual(self.player.radius, None,\
                'Player does not have radius')

    def test_player_has_no_gun_cooldown(self):
        self.assertEqual(self.player.gun_cooldown, 0,\
                'Player has gun cooldown at the begining')

    def test_player_has_gun_cooldown_delay(self):
        self.assertNotEqual(self.player.gun_cooldown_delay, None,\
                'Player does not have gun delay')

    def test_player_has_gun_cooldown_delay_not_zero(self):
        self.assertNotEqual(self.player.gun_cooldown_delay, 0,\
                'Player does not have gun delay zero')

    def test_player_has_health(self):
        self.assertNotEqual(self.player.health, None,\
                'Player health is not set')

    def test_player_has_shield(self):
        self.assertNotEqual(self.player.shield, None,\
                'Player shield is not set')

    def test_player_has_initial_gun_overflow_zero(self):
        self.assertEqual(0, self.player.gun_overflow)

    def test_player_has_gun_overflow_max(self):
        self.assertNotEqual(self.player.gun_overflow_max, None)

    def test_player_has_gun_overflow_step(self):
        self.assertNotEqual(self.player.gun_overflow_step, None)

    def test_player_has_gun_overflow_step_back(self):
        self.assertNotEqual(self.player.gun_overflow_step_back, None)

    def test_player_has_green_gun_type(self):
        self.assertEqual(self.player.gun_type, 'green')

    def test_player_has_initial_gun_level_one(self):
        self.assertEqual(self.player.gun_level, 1)

    def test_player_has_gun_powers(self):
        self.assertNotEqual(self.player.gun_powers, None)

    def test_player_has_bullets_speed(self):
        self.assertNotEqual(self.player.gun_speed, None)

    def test_player_can_initialy_shoot(self):
        self.assertEqual(self.player.can_shoot, True)

    def test_player_has_move_speed(self):
        self.assertNotEqual(self.player.move_speed, None)

    def test_player_has_zero_kills(self):
        self.assertEqual(self.player.kills, 0)

    def test_player_has_zero_score(self):
        self.assertEqual(self.player.score, 0)

    def test_get_gun_position(self):
        position = self.player._get_gun_position(1)
        self.assertEquals(position, self.player.rect.midtop)

    def test_get_gun_power(self):
        self.assertTrue(
                self.player._get_gun_power() >= self.player.gun_powers[0])
        self.assertTrue(
                self.player._get_gun_power() <= self.player.gun_powers[1])

if __name__ == '__main__':
    unittest.main()
