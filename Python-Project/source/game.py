#!/usr/bin/env python

import pygame
import player

class Game:
    
    def main(self, screen):
        print('Game started...')
        
        background = pygame.image.load('images/bg_3.jpg')

        clock = pygame.time.Clock()
        sprites = pygame.sprite.Group()
        sprites.add(player.Player(sprites))
        self.walls = self.make_bounds()
        sprites.add(self.walls)

        game_running = True
        while game_running:
            tick = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            

            sprites.update(tick / 1000.0, self)
            screen.blit(background, (0,0))
            sprites.draw(screen)
            pygame.display.flip()


    def make_bounds(self):
        walls = pygame.sprite.Group()
        wall_image = pygame.image.load('images/wall.png')
        for x in range(0, 800, 1):
            for y in range(0, 600, 1):
                if x in (0, 800 - 1) or y in (0, 600 - 1):
                    wall = pygame.sprite.Sprite(walls)
                    wall.image = wall_image 
                    wall.rect = pygame.rect.Rect((x, y), wall_image.get_size())
        return walls


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600), pygame.HWSURFACE|pygame.DOUBLEBUF)
    Game().main(screen)    
