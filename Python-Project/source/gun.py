#!/usr/bin/env python

import pygame
import bonus
import sounds
import effects


class Gun(pygame.sprite.Sprite):

    gun_1 = pygame.image.load('images/lazer_green.png')
    gun_2 = pygame.image.load('images/lazer_red.png')
    gun_imgs = {'green': gun_1, 'red': gun_2}

    def __init__(self, gun, power, speed,
            is_enemy, position, direction, *groups):
        """Inits the bullets

        A bullet has power, direction, image and life.
        Direction depends on who shoots - player or enemy.
        Power depends from the outside.

        """
        self.move_speed = speed
        super(Gun, self).__init__(*groups)
        self.image = self.gun_imgs.get(gun)
        self.rect = pygame.rect.Rect(position, self.image.get_size())
        self.direction = direction
        self.power = power
        self.gun_life = 7
        self.is_enemy_bullet = is_enemy

    def _movement(self, dt):
        """Move the bullet up or down, depending on who is shooting."""
        self.rect.y += self.move_speed * dt * self.direction

    def __gun_life_controller(self, dt):
        """Kill the bullet after its life ends."""
        self.gun_life -= dt
        if self.gun_life < 0:
            self.kill()
            return

    def __collide_controller(self, game):
        """Check for collusions with enemy or player.

        Manages the health of the enemy and the player.
        Manages the shield of the player.
        Manages the sound and graphics effects on kill.
        Manages game stats.
        Creates the bonus if enemy is killed.

        """
        for enemy in game.enemies.sprites():
            if pygame.sprite.collide_circle(self, enemy) \
                    and not self.is_enemy_bullet \
                    and self.direction == -1:
                self.kill()
                enemy.health -= self.power
                sounds.Sound('e_hit').play()
                if enemy.health <= 0:
                    bonus.Bonus(enemy.bonus, enemy.rect.midtop, game.sprites)
                    enemy.kill()
                    effects.Explosion(enemy.rect.midtop, game, game.sprites)
                    sounds.Sound('death').play()
                    game.gamer.score += game.game_level * 1000
                    game.gamer.kills += 1
        for gamer in game.players.sprites():
            if pygame.sprite.collide_circle(self, gamer) \
                    and self.is_enemy_bullet:
                self.kill()
                if gamer.shield > 0:
                    gamer.shield -= self.power
                    sounds.Sound('shield_hit').play()
                    if gamer.shield <= 0:
                        gamer.health += gamer.shield
                        gamer.shield = 0
                        self.__check_death__(game, gamer)
                    gamer.shield = max(0, gamer.shield)
                else:
                    gamer.health -= self.power
                    gamer.health = max(0, gamer.health)
                    sounds.Sound('hit').play()
                    self.__check_death__(game, gamer)

    def __check_death__(self, game, gamer):
        """Check if the player is dead."""
        if gamer.health <= 0:
            gamer._zero_stats()
            gamer.kill()
            effects.Explosion(gamer.rect.midtop, game, game.sprites)
            sounds.Sound('death').play()

    def update(self, tick, game):
        self._movement(tick)
        self.__gun_life_controller(tick)
        self.__collide_controller(game)
