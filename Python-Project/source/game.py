#!/usr/bin/env python

import pygame
import player
import enemy

class Game:


    def __init__(self):
        self.score = 0
        self.accuracy = 100.0
        self.total = 0

        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()

        self.enemies = self.load_enemies()
        self.sprites.add(self.enemies)

        self.gamer = player.Player((400,500), 'gun1', 1, self.sprites)
        self.sprites.add(self.gamer)

        self.walls = self.make_bounds()
        self.sprites.add(self.walls)
       
        self.background = pygame.image.load('images/background2.png')
        self.status_img = pygame.image.load('images/stats.png')

    
    def main(self, screen):
        print('Game started...')

        game_running = True
        while game_running:
            tick = self.clock.tick(40)
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            self.sprites.update(tick / 1000., self)
            screen.blit(self.background, (0,0))
            self.sprites.draw(screen)
            screen.blit(self.status_img, (0,640))

            pygame.display.flip()


    def make_bounds(self):
        walls = pygame.sprite.Group()
        wall_image = pygame.image.load('images/wall.png')
        for x in range(2, 1000, 1):
            for y in range(2, 640, 1):
                if x in (2, 1000 - 2) or y in (2, 640 - 2):
                    wall = pygame.sprite.Sprite(walls)
                    wall.image = wall_image 
                    wall.rect = pygame.rect.Rect((x, y), wall_image.get_size())
        return walls

    def load_enemies(self):
        enemies = pygame.sprite.Group()
        for y in range (60, 300, 90):
            for x in range (20, 700, 120):
                enemy_bot = enemy.Enemy((x, y), 1, enemies)
        return enemies


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000,700), pygame.HWSURFACE|pygame.DOUBLEBUF)
    Game().main(screen)    
