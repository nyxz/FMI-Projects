#!/usr/bin/python

import unittest
from . source.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player((0, 0), None)


    def testPlayerHasImage(self):
       self.assertNotEqual(self.player.image, None,\
               'Player does not have image') 


if __name__ == '__main__':
    unittest.main()
