#!/usr/bin/env python

import pygame

class Game:

    def main(self, screen):
        print('Game started...')
        
        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    Game().main(screen)    
