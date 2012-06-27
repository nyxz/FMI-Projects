#!/usr/bin/python

import enemy
import unittest
import pygame


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.enemy = enemy.Enemy((100, 100), 1, pygame.sprite.Group())

    def test_enemy_has_image(self):
        self.assertNotEqual(None, self.enemy.image)

    def test_enemy_has_level(self):
        self.assertNotEqual(None, self.enemy.level)

    def test_enemy_has_rect(self):
        self.assertNotEqual(None, self.enemy.rect)

    def test_enemy_has_health(self):
        self.assertNotEqual(None, self.enemy.health)

    def test_enemy_has_damage_level(self):
        self.assertNotEqual(None, self.enemy.dmg_level)

    def test_enemy_has_radius(self):
        self.assertNotEqual(None, self.enemy.radius)

    def test_enemy_has_role(self):
        self.assertNotEqual(None, self.enemy.is_boss)

    def test_enemy_is_not_boss(self):
        self.assertEqual(False, self.enemy.is_boss)

    def test_enemy_has_images(self):
        self.assertNotEqual(None, self.enemy.images)

    def test_enemy_has_images_for_all_enemy_levels(self):
        self.assertNotEqual(None, self.enemy.image_1)
        self.assertNotEqual(None, self.enemy.image_2)
        self.assertNotEqual(None, self.enemy.image_3)
        self.assertNotEqual(None, self.enemy.image_4)
        self.assertNotEqual(None, self.enemy.image_5)

    def test_enemy_has_health_levels(self):
        self.assertNotEqual(None, self.enemy.health_level)

    def test_enemy_has_gun_min_and_max_speed(self):
        self.assertNotEqual(None, self.enemy.gun_min_speed)
        self.assertNotEqual(None, self.enemy.gun_max_speeds)

    def test_enemy_has_cooldown_range(self):
        self.assertNotEqual(None, self.enemy.gun_cooldown_range)
        self.assertNotEqual(None, self.enemy.boss_gun_cooldown_range)

    def test_enemy_has_red_bullets(self):
        self.assertEqual('red', self.enemy.gun_type)

    def test_enemy_has_gun_direction_down(self):
        self.assertEqual(1, self.enemy.gun_direction)

    def test_enemy_has_direction_right(self):
        self.assertEqual(1, self.enemy.direction)

    def test_enemy_has_initial_gun_cooldown(self):
        self.assertNotEqual(None, self.enemy.gun_cooldown)

    def test_enemy_has_gun_bullets_rate(self):
        self.assertNotEqual(None, self.enemy.gun_bullets_rate)

    def test_enemy_has_speed(self):
        self.assertNotEqual(None, self.enemy.BOSS_SPEED)
        self.assertNotEqual(None, self.enemy.REGULAR_SPEED)

    def test_x_movement(self):
        last_x = self.enemy.rect.x
        self.enemy._movement(10)
        new_x = self.enemy.rect.x
        self.assertNotEqual(last_x, new_x)

    def test_y_movement(self):
        last_y = self.enemy.rect.y
        self.enemy._movement(10)
        new_y = self.enemy.rect.y
        self.assertEqual(last_y, new_y)

    def test_enemy_get_move_speed(self):
        self.assertNotEqual(self.enemy._get_move_speed,
                self.enemy.REGULAR_SPEED)

    def test_enemy_gun_damage_is_in_right_bounds(self):
        self.assertTrue(
                self.enemy.gun_dmg_by_level() >= self.enemy.dmg_level[0])
        self.assertTrue(
                self.enemy.gun_dmg_by_level() <= self.enemy.dmg_level[1])

if __name__ == '__main__':
    unittest.main()
