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

    sounds = {'shield': shield, 'heal': heal, 'hit': hit, 'death': death,\
            'points': points, 'shot': shot, 'weapon': weapon,\
            'overflow': overflow, 'shield_hit': shield_hit, 'e_hit': e_hit}

    def __init__(self, type):
        """Initialize the sound effects

        Sound could be played:
            - when bonus shield is taken;
            - when bonus health is taken;
            - when enemy bullet hits player;
            - when enemy or player die;
            - when bonus point are taken (R2-D2)
            - when player is shooting;
            - when bonus weapon is taken;
            - when player gun overflows;
            - when player is hit and has shield;
            - when player is hit and does not have shield.

        """
        self.type = type
        self.path = self.sounds.get(self.type)
        super(Sound, self).__init__(self.path)
