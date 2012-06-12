#!/usr/bin/env python

import pygame


class Stats:

    def __init__(self, game):
        self.game = game
        self.player = game.gamer
        self.p_health_pos = (760, 650)
        self.p_shield_pos = (760, 670)
        self.p_score_pos = (50, 650)
        self.gun_overflow_pos = (50, 670)
        self.enemy_down_pos = (500, 650)
        self.gun_lvl_pos = (500, 670)
        self.color = (200, 200, 200)
        self.color_red = (200, 10, 10)
        self.color_green = (10, 200, 10)
        self.color_orange = (250, 145, 0)
        self.color_yellow = (255, 245, 0)
        self.overflow_color = self.color_green
        self.health_color = self.color_green
        self.shield_color = self.color_green
        self.stats = dict() 


    def load_player_health(self):
        pygame.font.init()
        font = pygame.font.Font(None, 20)

        #health_msg = "Health: {health}".format(health = self.player.health)
        health_msg = self.__get_health_status__()
        health_txt = font.render(health_msg, 1, self.health_color)
        self.stats.__setitem__('health', (health_txt, self.p_health_pos))

        shield_msg = self.__get_shield_status__() 
        shield_txt = font.render(shield_msg, 1, self.shield_color)
        self.stats.__setitem__('shield', (shield_txt, self.p_shield_pos))

        score_msg = "Score: {score}".format(score = self.player.score)
        score_txt = font.render(score_msg, 1, self.color)
        self.stats.__setitem__('score', (score_txt, self.p_score_pos))

        overflow_msg = self.__get_overflow_status__()
        overflow_txt = font.render(overflow_msg, 1, self.overflow_color)
        self.stats.__setitem__('overflow', (overflow_txt, self.gun_overflow_pos))

        enemy_down_msg = "Kills: {kills}".format(kills = self.player.kills)
        enemy_down_txt = font.render(enemy_down_msg, 1, self.color)
        self.stats.__setitem__('kills', (enemy_down_txt, self.enemy_down_pos))

        gun_lvl_msg = "Gun: {gun}".format(gun = self.player.gun_level)
        gun_lvl_txt = font.render(gun_lvl_msg, 1, self.color)
        self.stats.__setitem__('gun', (gun_lvl_txt, self.gun_lvl_pos))

        return self.stats


    def game_has_enemies(self):
        if self.game.enemies.sprites().__len__() < 1:
            return False
        return True


    def __get_health_status__(self):
        hp = self.player.health
        health_stat = '|' * int(hp // 5)
        if hp <= 80 and hp > 60:
            self.health_color = self.color_yellow
        if hp <= 60 and hp > 20:
            self.health_color = self.color_orange
        if hp <= 20:
            self.health_color = self.color_red

        health_msg = "HP: " + health_stat + '  ( ' + int(hp).__str__() + ' )'
        return health_msg


    def __get_overflow_status__(self):
        overflow = self.player.gun_overflow
        overflow_stat = '|' * int(overflow)
        if overflow <= 10:
            self.overflow_color = self.color_green
        if overflow > 10 and overflow <= 20:
            self.overflow_color = self.color_yellow
        if overflow > 20 and overflow <= 40:
            self.overflow_color = self.color_orange
        if overflow > 40: 
            self.overflow_color = self.color_red

        overflow_msg = 'Overflow: ' + overflow_stat + ' '
        return overflow_msg


    def __get_shield_status__(self):
        shield = self.player.shield
        shield_stat = '|' * int(shield // 5)
        if shield <= 80 and shield > 60:
            self.shield_color = self.color_yellow
        if shield <= 60 and shield > 20:
            self.shield_color = self.color_orange
        if shield <= 20:
            self.shield_color = self.color_red

        shield_msg = "Shield: " + shield_stat + '  ( ' + int(shield).__str__() + ' )'
        return shield_msg
