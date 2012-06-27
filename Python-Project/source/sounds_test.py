#!/usr/bin/python

import unittest
import sounds
import pygame


class TestSound(unittest.TestCase):

    def setUp(self):
        self.sound = sounds.Sound('e_hit')

    def test_sound_has_type(self):
        self.assertNotEqual(None, self.sound.type, 'Cannot load sound')

if __name__ == '__main__':
    unittest.main()
