#!/usr/bin/env python

import pygame


class Sound(pygame.mixer.Sound):

    shield = 'sounds/on_shield.wav'
    heal = 'sounds/on_heal.wav'
    hit = 'sounds/on_hit.wav'
    death = 'sounds/on_explosion.wav'
    points = 'sounds/on_points.wav'
    shot = 'sounds/on_shot.wav'
    weapon = 'sounds/on_weapon.wav'
    overflow = 'sounds/on_overflow.wav'
    shield_hit = 'sounds/on_shield_hit.wav'
    e_hit = 'sounds/on_e_hit.wav'

    sounds = {'shield': shield, 'heal':heal, 'hit':hit, 'death':death,\
            'points':points, 'shot':shot, 'weapon':weapon,\
            'overflow':overflow, 'shield_hit':shield_hit, 'e_hit':e_hit}

    def __init__(self, type):
        self.type = type
        self.path = self.sounds.get(self.type) 
        super(Sound, self).__init__(self.path)
