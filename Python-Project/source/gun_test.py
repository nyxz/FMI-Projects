#!/usr/bin/python

import unittest
import gun
import pygame


class TestGun(unittest.TestCase):

    def setUp(self):
        groups = pygame.sprite.Group()
        self.gun = gun.Gun('green', 100, 100, False, (500, 400), 1, groups)

    def test_gun_has_movespeed(self):
        self.assertNotEqual(None, self.gun.move_speed)

    def test_gun_has_image(self):
        self.assertNotEqual(None, self.gun.image)

    def test_gun_has_rect(self):
        self.assertNotEqual(None, self.gun.rect)

    def test_gun_has_direction(self):
        self.assertNotEqual(None, self.gun.direction)

    def test_gun_has_power(self):
        self.assertNotEqual(None, self.gun.power)

    def test_gun_has_life(self):
        self.assertNotEqual(None, self.gun.gun_life)

    def test_gun_bullet_is_from_enemy(self):
        self.assertEqual(False, self.gun.is_enemy_bullet)

    def test_gun_has_images(self):
        self.assertNotEqual(None, self.gun.gun_1)
        self.assertNotEqual(None, self.gun.gun_2)
        self.assertNotEqual(None, self.gun.gun_imgs)

    def test_gun_movement_x(self):
        old_x = self.gun.rect.x
        self.gun._movement(10)
        new_x = self.gun.rect.x
        self.assertEqual(old_x, new_x)

    def test_gun_movement_y(self):
        old_y = self.gun.rect.y
        self.gun._movement(10)
        new_y = self.gun.rect.y
        self.assertNotEqual(old_y, new_y)

if __name__ == '__main__':
    unittest.main()
