#!/usr/bin/env python

import pygame


class Explosion(pygame.sprite.Sprite):

    expl_frames = [\
            pygame.image.load('images/explosion/Explode1.png'),
            pygame.image.load('images/explosion/Explode2.png'),
            pygame.image.load('images/explosion/Explode3.png'),
            pygame.image.load('images/explosion/Explode4.png'),
            pygame.image.load('images/explosion/Explode5.png'),
            pygame.image.load('images/explosion/Explode6.png'),
            pygame.image.load('images/explosion/Explode7.png'),
            pygame.image.load('images/explosion/Explode8.png'),
            pygame.image.load('images/explosion/Explode9.png'),
            pygame.image.load('images/explosion/Explode10.png'),
            pygame.image.load('images/explosion/Explode11.png'),
            pygame.image.load('images/explosion/Explode12.png'),
            pygame.image.load('images/explosion/Explode13.png'),
            pygame.image.load('images/explosion/Explode14.png'),
            pygame.image.load('images/explosion/Explode15.png'),
            pygame.image.load('images/explosion/Explode16.png'),
            pygame.image.load('images/explosion/Explode17.png')
            ]

    def __init__(self, position, game, *groups):
        """Initialize the explosion effect."""
        super(Explosion, self).__init__(*groups)
        self.idx = 0
        self.image = self.expl_frames[self.idx]
        self.rect = pygame.rect.Rect(position, self.image.get_size())
        self.game = game

    def __evolution(self, tick):
        """Go through all explosion frames."""
        if self.idx > self.expl_frames.__len__() - 1:
            self.kill()
        else:
            self.image = self.expl_frames[self.idx]
            self.idx += 1

    def update(self, tick, game):
        self.__evolution(tick)
