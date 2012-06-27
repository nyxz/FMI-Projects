#!/usr/bin/python

import unittest
import game
import pygame


class TestGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        screen = pygame.display.set_mode((1000, 700),
                pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.game = game.Game(screen)

    def test_has_screen(self):
        self.assertNotEqual(None, self.game.screen)

    def test_has_game_level(self):
        self.assertNotEqual(None, self.game.game_level)

    def test_has_background(self):
        self.assertNotEqual(None, self.game.background)

    def test_has_status_image(self):
        self.assertNotEqual(None, self.game.status_img)

    def test_has_enemies(self):
        self.assertNotEqual(None, self.game.enemies)

    def test_has_at_least_one_enemy(self):
        self.assertTrue(self.game.enemies.sprites().__len__() > 0)

    def test_has_player(self):
        self.assertNotEqual(None, self.game.players)

    def test_has_at_least_one_player(self):
        self.assertTrue(self.game.players.sprites().__len__() > 0)

    def test_has_walls(self):
        self.assertNotEqual(None, self.game.walls)

    def test_has_player_positions(self):
        self.assertNotEqual(None, self.game.player_pos)

    def test_has_background_image_position(self):
        self.assertNotEqual(None, self.game.bg_img_pos)

    def test_has_statistics_image_position(self):
        self.assertNotEqual(None, self.game.stat_img_pos)

if __name__ == '__main__':
    unittest.main()
