#!/usr/bin/env python

import pygame
import player
import enemy
import stats

class Game:


    def __init__(self, screen):

        self.player_pos = (400, 500)
        self.bg_img_pos = (0, 0)
        self.stat_img_pos = (0, 640)
        self.stat_bar_size = 60
        self.bound_size = 2
        self.border = 1
        self.clock_tick = 60
        self.enemy_y_range = range(40, 300, 90)
        self.enemy_x_range = range(20, 700, 120)
        
        self.screen_size = screen.get_size()
        self.game_level = 1

        self.background = pygame.image.load('images/background.png')
        self.status_img = pygame.image.load('images/stats.png')

        stats_img_pos = (0, self.screen_size[1] - self.stat_bar_size)

        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()

        self.enemies = self.__load_enemies()
        self.sprites.add(self.enemies)

        self.gamer = player.Player(self.player_pos, self.sprites)
        self.sprites.add(self.gamer)

        self.walls = self.__make_bounds()
        self.sprites.add(self.walls)


    def __make_bounds(self):
        walls = pygame.sprite.Group()
        wall_image = pygame.image.load('images/wall.png')
        height = self.screen_size[1] - self.stat_bar_size
        for x in range(self.bound_size, self.screen_size[0], self.border):
            for y in range(self.bound_size, height, self.border):
                if x in (
                        self.bound_size, \
                        self.screen_size[0] - self.bound_size) \
                or y in (self.bound_size, height - self.bound_size):
                    wall = pygame.sprite.Sprite(walls)
                    wall.image = wall_image 
                    wall.rect = pygame.rect.Rect((x, y), wall_image.get_size())
        return walls


    def __load_enemies(self):
        enemies = pygame.sprite.Group()
        for y in self.enemy_y_range:
            for x in self.enemy_x_range:
                enemy_bot = enemy.Enemy((x, y), self.game_level, enemies)
        return enemies


    def main(self):
        game_running = True
        while game_running:
            tick = self.clock.tick(self.clock_tick)
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN \
                and event.key == pygame.K_ESCAPE:
                    return

            self.stat_class = stats.Stats(self)
            has_enemies = self.stat_class.game_has_enemies()
            if not has_enemies:
                return
            
            self.stats = self.stat_class.load_player_health()
            health = self.stats.get('health')
            shield = self.stats.get('shield')
            score = self.stats.get('score')
            overflow = self.stats.get('overflow')
            kills = self.stats.get('kills')
            gun_lvl = self.stats.get('gun')

            self.sprites.update(tick / 1000., self)
            screen.blit(self.background, self.bg_img_pos)
            self.sprites.draw(screen)
            screen.blit(self.status_img, self.stat_img_pos)
            screen.blit(health[0], health[1])
            screen.blit(shield[0], shield[1])
            screen.blit(score[0], score[1])
            screen.blit(overflow[0], overflow[1])
            screen.blit(kills[0], kills[1])
            screen.blit(gun_lvl[0], gun_lvl[1])
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(
            (1000,700), 
            pygame.HWSURFACE|pygame.DOUBLEBUF
            )
    Game(screen).main()
