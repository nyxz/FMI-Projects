#!/usr/bin/env python

import pygame
import gun
import random


class Enemy(pygame.sprite.Sprite):

    GIFTS = ('p100', 'p200', 'p300', 'gun', 'shield', 'heal')
    image_1 = pygame.image.load('images/enemy_1.png')
    image_2 = pygame.image.load('images/enemy_2.png')
    image_3 = pygame.image.load('images/enemy_3.png')
    image_4 = pygame.image.load('images/enemy_4.png')
    image_5 = pygame.image.load('images/boss.png')
    images = {1: image_1, 2: image_2, 3: image_3, 4: image_4, 5: image_5}
    health_level = {1: 200, 2: 250, 3: 300, 4: 350, 5: 2000}
    dmg_levels = ((25, 30), (30, 45), (45, 65), (65, 90), (20, 200))
    gun_min_speed = 150
    gun_max_speeds = {1: 300, 2: 350, 3: 400, 4: 450, 5: 480}
    gun_cooldown_range = (1.0, 5.0)
    boss_gun_cooldown_range = (0.1, 1.0)
    gun_type = 'red'
    gun_direction = 1
    direction = 1
    gun_cooldown = 4
    gun_bullets_rate = 800
    BOSS_SPEED = 250
    REGULAR_SPEED = 100

    def __init__(self, location, game_level, *groups):
        """Initialize the enemy

        Every enemy has random bonus when killed.
        Enemies are different for different levels of the game.
        They differ in health, DPS, weapon power, weapon speed,
        image. Regular enemy speed is less than the boss speed.

        """
        self.bonus = self.__get_rand_bonus()
        super(Enemy, self).__init__(*groups)
        self.level = game_level
        self.image = self.images.get(self.level)
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.health = self.health_level.get(self.level)
        self.dmg_level = self.dmg_levels[self.level - 1]
        self.radius = 22
        self.is_boss = self.__get_role()
        self.move_speed = self._get_move_speed()

    def __collide_controller(self, game, last):
        """Check for collusions

        Check for collusions with walls.
        If collide with wall change the direction
        If collide with outside the wall - continue to move in same direction.

        """
        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell_rect = cell.rect
            if last.right <= cell_rect.left \
                    and new.right > cell_rect.left \
                    and cell_rect.left > 100 \
                    and self.direction == 1:
                self.direction = -1
            if last.left >= cell_rect.right \
                    and new.left < cell_rect.right \
                    and cell_rect.right < 1000 \
                    and self.direction == -1:
                self.direction = 1

    def _movement(self, tick):
        """Movement depends on speed and direction - left/right."""
        self.rect.x += self.direction * self.move_speed * tick

    def __shoot(self, game, dt):
        """Enemy shooting

        One bullet for regular enemy.
        Four bullets for boss.

        """
        if self.is_boss:
            self.__boss_shoot(game, dt)
        else:
            self.__regular_shoot(game, dt)

    def __regular_shoot(self, game, dt):
        """Creates the bullets for the regular enemy"""
        rand = random.randint(1, 1000)
        if rand > self.gun_bullets_rate and not self.gun_cooldown:
            gun_dmg = self.gun_dmg_by_level()
            gun_speed = random.randint(
                    self.gun_min_speed,
                    self.gun_max_speeds.get(self.level)
                    )
            gun.Gun(
                    self.gun_type,
                    gun_dmg,
                    gun_speed,
                    True,
                    self.rect.midtop,
                    self.gun_direction,
                    game.sprites
                    )
            self.gun_cooldown = random.uniform(
                    self.gun_cooldown_range[0],
                    self.gun_cooldown_range[1]
                    )
        self.gun_cooldown = max(0, self.gun_cooldown - dt)

    def __boss_shoot(self, game, dt):
        """Creates the bullets for the boss."""
        rand = random.randint(1, 1000)
        if rand > self.gun_bullets_rate and not self.gun_cooldown:
            gun_dmg = self.gun_dmg_by_level()
            gun_speed = random.randint(
                    self.gun_min_speed,
                    self.gun_max_speeds.get(self.level)
                    )
            count = 4
            while count > 0:
                gun.Gun(
                        self.gun_type,
                        gun_dmg,
                        gun_speed,
                        True,
                        self.__get_bullet_pos(count),
                        self.gun_direction,
                        game.sprites
                        )
                count -= 1
            self.gun_cooldown = random.uniform(
                    self.boss_gun_cooldown_range[0],
                    self.boss_gun_cooldown_range[1]
                    )
        self.gun_cooldown = max(0, self.gun_cooldown - dt)

    def _get_move_speed(self):
        """Get regular or boss move speed."""
        if self.is_boss:
            return self.BOSS_SPEED
        return self.REGULAR_SPEED

    def __get_bullet_pos(self, count):
        """Manages the boss bullets position."""
        if count == 4:
            return self.rect.midleft
        elif count == 3:
            return (
                    self.rect.midleft[0] + 10,\
                    self.rect.midleft[1]\
                    )
        elif count == 2:
            return self.rect.midright
        elif count == 1:
            return (
                    self.rect.midright[0] - 10,\
                    self.rect.midright[1]\
                    )

    def __get_role(self):
        """Get True for Boss and False for regular enemy."""
        if self.level == 5:
            return True
        return False

    def gun_dmg_by_level(self):
        """Get random weapon damage depending on self.dmg_level."""
        self.dmg_level = self.dmg_levels[self.level - 1]
        rand = random.randint(self.dmg_level[0], self.dmg_level[1])
        return rand

    def __get_rand_bonus(self):
        """Loads the bonus for the enemy to drop when killed."""
        num = random.randint(0, 100)
        if num <= 30:
            return self.GIFTS[0]
        if num <= 55:
            return self.GIFTS[1]
        if num <= 75:
            return self.GIFTS[2]
        if num <= 85:
            return self.GIFTS[3]
        if num <= 95:
            return self.GIFTS[4]
        if num <= 100:
            return self.GIFTS[5]

    def update(self, tick, game):
        last_position = self.rect.copy()
        self._movement(tick)
        self.__shoot(game, tick)
        self.__collide_controller(game, last_position)
