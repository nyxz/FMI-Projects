#!/usr/bin/env python

import pygame
import player
import enemy

class Game:
    
    def main(self, screen):
        print('Game started...')
        
        background = pygame.image.load('images/bg_3.jpg')
        player_image = pygame.image.load('images/player.png')    

        clock = pygame.time.Clock()
        sprites = pygame.sprite.Group()

        self.enemies = self.load_enemies()
        sprites.add(self.enemies)

        self.gamer = player.Player((400,500), 'gun1', 1, sprites)
        sprites.add(self.gamer)

        self.walls = self.make_bounds()
        sprites.add(self.walls)

        game_running = True
        while game_running:
            tick = clock.tick(40)
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                #if event.type == pygame.KEYUP:
                #    self.gamer.image = player_image 
            

            sprites.update(tick / 1000., self)
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

    def load_enemies(self):
        enemies = pygame.sprite.Group()
        for y in range (60, 300, 90):
            for x in range (20, 700, 120):
                enemy_bot = enemy.Enemy((x, y), 1, enemies)
        return enemies


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600), pygame.HWSURFACE|pygame.DOUBLEBUF)
    Game().main(screen)    
