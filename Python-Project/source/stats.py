#!/usr/bin/env python

import pygame
import shelve
import datetime
import enemy


class Stats:

    db_file = 'game.db'
    db_rec = 'scores'

    p_health_pos = (760, 650)
    p_shield_pos = (760, 670)
    p_score_pos = (50, 650)
    level_pos = (170, 650)
    gun_over_pos = (50, 670)
    enemy_down_pos = (290, 650)
    gun_lvl_pos = (230, 650)
    dmg_lvl_pos = (580, 650)
    e_dmg_lvl_pos = (420, 650)
    e_health_pos = (420, 670)

    color = (200, 200, 200)
    color_red = (200, 10, 10)
    color_green = (10, 200, 10)
    color_orange = (250, 145, 0)
    color_yellow = (255, 245, 0)

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.player = game.gamer
        self.overflow_color = self.color_green
        self.health_color = self.color_green
        self.shield_color = self.color_green
        self.stats = dict()

    def load_stats(self):
        """Loads game statistics

        Loads player score, kills, gun level,
        gun overflow, enemy's health and weapon power,
        player weapon power, health and shield.

        """
        pygame.font.init()
        font = pygame.font.Font(None, 20)

        health_msg = self.__get_health_status()
        health_txt = font.render(health_msg, 1, self.health_color)
        self.stats.__setitem__('health', (health_txt, self.p_health_pos))

        shield_msg = self.__get_shield_status()
        shield_txt = font.render(shield_msg, 1, self.shield_color)
        self.stats.__setitem__('shield', (shield_txt, self.p_shield_pos))

        score_msg = "Score: {score}".format(score=self.player.score)
        score_txt = font.render(score_msg, 1, self.color)
        self.stats.__setitem__('score', (score_txt, self.p_score_pos))

        overflow_msg = self.__get_overflow_status()
        overflow_txt = font.render(overflow_msg, 1, self.overflow_color)
        self.stats.__setitem__('overflow', (overflow_txt, self.gun_over_pos))

        enemy_down_msg = "Kills: {kills}".format(kills=self.player.kills)
        enemy_down_txt = font.render(enemy_down_msg, 1, self.color)
        self.stats.__setitem__('kills', (enemy_down_txt, self.enemy_down_pos))

        gun_lvl_msg = "Gun: {gun}".format(gun=self.player.gun_level)
        gun_lvl_txt = font.render(gun_lvl_msg, 1, self.color)
        self.stats.__setitem__('gun', (gun_lvl_txt, self.gun_lvl_pos))

        dmg_lvl_msg = "Your dmg: {dmg}".format(dmg=self.game.gamer.gun_powers)
        dmg_lvl_txt = font.render(dmg_lvl_msg, 1, self.color)
        self.stats.__setitem__('dmg', (dmg_lvl_txt, self.dmg_lvl_pos))

        e_dmg_lvl_msg = "Enemy dmg: {dmg}".format(dmg=self.game.e_dmg_level)
        e_dmg_lvl_txt = font.render(e_dmg_lvl_msg, 1, self.color)
        self.stats.__setitem__('e_dmg', (e_dmg_lvl_txt, self.e_dmg_lvl_pos))

        e_health_lvl_msg = "Enemy health: {health}".\
                format(health=self.game.e_health)
        e_health_lvl_txt = font.render(e_health_lvl_msg, 1, self.color)
        self.stats.__setitem__('e_health',\
                (e_health_lvl_txt, self.e_health_pos))

        game_level = "Level {level}".format(level=self.game.game_level)
        game_lvl_txt = font.render(game_level, 1, self.color)
        self.stats.__setitem__('level', (game_lvl_txt, self.level_pos))

        return self.stats

    def __get_health_status(self):
        """Manage health stats

        Set the health color depending on health levels.
        Creates the health text.

        """
        hp = self.player.health
        mult = int(hp // 5)
        health_stat = '|' * mult + ' ' * (20 - mult)
        if hp <= 80 and hp > 60:
            self.health_color = self.color_yellow
        if hp <= 60 and hp > 20:
            self.health_color = self.color_orange
        if hp <= 20:
            self.health_color = self.color_red

        health_msg = "Health: [" + health_stat + ']  ( ' \
                + int(hp).__str__() + ' )'
        return health_msg

    def __get_overflow_status(self):
        """Manages overflow stats

        Set the overflow color depending on overflow levels.
        Creates the overflow text.

        """
        overflow = self.player.gun_overflow
        mult = int(overflow)
        overflow_stat = '|' * mult + ' ' * (50 - mult)
        if overflow <= 10:
            self.overflow_color = self.color_green
        if overflow > 10 and overflow <= 20:
            self.overflow_color = self.color_yellow
        if overflow > 20 and overflow <= 40:
            self.overflow_color = self.color_orange
        if overflow > 40:
            self.overflow_color = self.color_red

        overflow_msg = 'Overflow: [' + overflow_stat + ']'
        return overflow_msg

    def __get_shield_status(self):
        """Manages shield stats

        Set the shield color depending on shiled level.
        Creates the shield text.

        """
        shield = self.player.shield
        mult = int(shield // 5)
        shield_stat = '|' * mult + ' ' * (20 - mult)
        if shield <= 80 and shield > 60:
            self.shield_color = self.color_yellow
        if shield <= 60 and shield > 20:
            self.shield_color = self.color_orange
        if shield <= 20:
            self.shield_color = self.color_red

        shield_msg = "Shield: [" + shield_stat \
                + ']  ( ' + int(shield).__str__() + ' )'
        return shield_msg

    def __calc_total__(self):
        """Calculate the player score

        Calculates the total player score.
        Persist the score and player name to the DB.

        """
        date = datetime.datetime.now()
        name = str(date) + '@' + self.game.player_name
        p_score = self.player.score

        db = shelve.open(self.db_file)
        if not db.get(self.db_rec):
            db[self.db_rec] = dict()

        scores = db.get(self.db_rec)
        scores.__setitem__(name, p_score)
        items = [(v, k) for k, v in scores.items()]
        items.sort()
        items.reverse()
        items = [(k, v) for v, k in items]
        if items.__len__() > 10:
            items.pop(10)

        new = dict()
        new.update(items)
        db.pop(self.db_rec)
        db[self.db_rec] = new
        db.close()
        return items

    def congratz(self):
        font = pygame.font.Font(None, 100)
        congratz = "YOU WON"
        congratz_txt = font.render(congratz, 1, self.color)

        cgrtz_rect = congratz_txt.get_rect()
        cgrtz_rect.centerx = self.screen.get_rect().centerx
        cgrtz_rect.centery = self.screen.get_rect().centery

        self.stats.__setitem__('congratz', (congratz_txt, cgrtz_rect))

    def lose(self):
        font = pygame.font.Font(None, 100)
        lose = "GAME OVER"
        lose_txt = font.render(lose, 1, self.color_red)

        lose_rect = lose_txt.get_rect()
        lose_rect.centerx = self.screen.get_rect().centerx
        lose_rect.centery = self.screen.get_rect().centery

        self.stats.__setitem__('lose', (lose_txt, lose_rect))

    def print_scores(self):
        """Print the high scores."""
        print("--------- High scores -------")
        scores = self.__calc_total__()
        idx = 1
        for score in scores:
            msg = "{place}. {name} \t:\t {result}"\
                    .format(\
                    place=idx,\
                    name=score[0][27:],\
                    result=score[1])
            print(msg)
            idx += 1
