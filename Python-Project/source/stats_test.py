#!/usr/bin/python

import unittest
from stats import Stats
from game import Game
import pygame


class TestStats(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 700),
                pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.game = Game(self.screen)
        self.stats = Stats(self.game)

    def test_stats_have_game(self):
        self.assertNotEqual(None, self.stats.game)

    def test_stats_have_screen(self):
        self.assertNotEqual(None, self.stats.screen)

    def test_stats_have_player(self):
        self.assertNotEqual(None, self.stats.player)

    def test_stats_have_overflow_color(self):
        self.assertNotEqual(None, self.stats.overflow_color)

    def test_stats_have_health_color(self):
        self.assertNotEqual(None, self.stats.health_color)

    def test_stats_have_empty_dict_initially(self):
        self.assertEqual(0, self.stats.stats.__len__())

    def test_stats_have_positions(self):
        self.assertNotEqual(None, self.stats.p_health_pos)
        self.assertNotEqual(None, self.stats.p_shield_pos)
        self.assertNotEqual(None, self.stats.p_score_pos)
        self.assertNotEqual(None, self.stats.level_pos)
        self.assertNotEqual(None, self.stats.gun_over_pos)
        self.assertNotEqual(None, self.stats.enemy_down_pos)
        self.assertNotEqual(None, self.stats.gun_lvl_pos)
        self.assertNotEqual(None, self.stats.dmg_lvl_pos)
        self.assertNotEqual(None, self.stats.e_dmg_lvl_pos)
        self.assertNotEqual(None, self.stats.e_health_pos)

    def test_stats_have_colors(self):
        self.assertNotEqual(None, self.stats.color)
        self.assertNotEqual(None, self.stats.color_red)
        self.assertNotEqual(None, self.stats.color_green)
        self.assertNotEqual(None, self.stats.color_orange)
        self.assertNotEqual(None, self.stats.color_yellow)

    def test_stats_have_texts_after_loading_stats(self):
        self.stats.load_stats()
        self.assertNotEqual(None, self.stats.stats.get('health'))
        self.assertNotEqual(None, self.stats.stats.get('shield'))
        self.assertNotEqual(None, self.stats.stats.get('score'))
        self.assertNotEqual(None, self.stats.stats.get('overflow'))
        self.assertNotEqual(None, self.stats.stats.get('kills'))
        self.assertNotEqual(None, self.stats.stats.get('gun'))
        self.assertNotEqual(None, self.stats.stats.get('dmg'))
        self.assertNotEqual(None, self.stats.stats.get('e_dmg'))
        self.assertNotEqual(None, self.stats.stats.get('e_health'))
        self.assertNotEqual(None, self.stats.stats.get('level'))

    def test_stats_have_congratz(self):
        self.stats.congratz()
        self.assertNotEqual(None, self.stats.stats.get('congratz'))

    def test_stats_have_lose(self):
        self.stats.lose()
        self.assertNotEqual(None, self.stats.stats.get('lose'))
        self.assertNotEqual(None, self.stats.game)

if __name__ == '__main__':
    unittest.main()
