# Name: Ajay Saini
# Date: May 22nd
# Purpose: To create a game for the ICS3U0 course.


import pygame
import random
from pygame.constants import MOUSEBUTTONDOWN

width, height = 800, 600
pygame.display.set_caption("PixelHaven: Realms of Wonders")
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
game_state = "Main"
starting = pygame.image.load("starting.png")
lives = 3
# HP
hp = pygame.image.load("hp.png")
hp = pygame.transform.scale(hp, (50, 50))
# Blood
blood = pygame.image.load("blood.png")
blood = pygame.transform.scale(blood, (500, 500))
# Play Button
play_button = pygame.image.load("play_button.png")
play_button = pygame.transform.scale(play_button, (300, 150))
# Exit Button
exit_button = pygame.image.load("exit_button.png")
exit_button = pygame.transform.scale(exit_button, (300, 150))
# Settings Button
settings_button = pygame.image.load("settings_button.png")
settings_button = pygame.transform.scale(settings_button, (85, 85))
# Pause Menu
pause_menu = pygame.image.load("pause_menu.png")
pause_menu = pygame.transform.scale(pause_menu, (550, 575))
resume_button = pygame.image.load("resume_button.png")
resume_button = pygame.transform.scale(resume_button, (200, 100))
settings_pause = pygame.image.load("settings_pause.png")
settings_pause = pygame.transform.scale(settings_pause, (200, 100))
quit_pause = pygame.image.load("quit_pause.png")
quit_pause = pygame.transform.scale(quit_pause, (200, 100))
# Check Button
check_button = pygame.image.load("check_button.png")
check_button = pygame.transform.scale(check_button, (200, 200))
check_button2 = pygame.image.load("check_button2.png")
check_button2 = pygame.transform.scale(check_button2, (150, 150))
# Settings Tab
settings_tab = pygame.image.load("settings_tab.png")
settings_tab = pygame.transform.scale(settings_tab, (390, 440))
# Level 1 background:
lvl1_bk = pygame.image.load("Level_1.jpg")
lvl1_bk = pygame.transform.scale(lvl1_bk, (width, height))
# Level 2 background:
lvl2_bk = pygame.image.load("Level_2.jpg")
lvl2_bk = pygame.transform.scale(lvl2_bk, (width, height))
# Welcome Tab
wlc_tab = pygame.image.load("Welcome_tab.png")
wlc_tab = pygame.transform.scale(wlc_tab, (400, 500))
# Game Over Tab
game_over = pygame.image.load("game_over.png")
game_over = pygame.transform.scale(game_over, (width, height))
# Sprite
spr_idle_r = pygame.image.load("sprite_idle_right.png")
spr_idle_r = pygame.transform.scale(spr_idle_r, (100, 100))
spr_walk_r = pygame.image.load("sprite_walk_right.png")
spr_walk_r = pygame.transform.scale(spr_walk_r, (105, 105))
spr_idle_l = pygame.image.load("sprite_idle_right.png")
spr_walk_l = pygame.transform.scale(spr_walk_r, (75, 75))
spr_walk_l = pygame.transform.flip(spr_walk_r, True, False)
spr_attack_r = pygame.image.load("spr_attack_r.png")
spr_attack_r = pygame.transform.scale(spr_attack_r, (105, 105))
spr_block_r = pygame.image.load("spr_block_r.png")
spr_block_r = pygame.transform.scale(spr_block_r, (110, 110))
# Zombie
zombie_idle_r = pygame.image.load("zombie_idle_r.png")
zombie_idle_r = pygame.transform.scale(zombie_idle_r, (63, 63))
zombie_idle_l = pygame.transform.flip(zombie_idle_r, True, False)
cave_monster = pygame.image.load("cave_monster.png")
cave_monster = pygame.transform.scale(cave_monster, (63, 63))
num_zombies = random.randint(2, 5)
zomb_x = []
zomb_y = []
zomb_lives = []
for i in range(num_zombies):
    zomb_x.append(850 + i * 100)
    zomb_y.append(443)
    zomb_lives.append(3)
# Yes and No Button:
yes_button = pygame.image.load("yes_button.png")
yes_button = pygame.transform.scale(yes_button, (150, 160))
no_button = pygame.image.load("no_button.png")
no_button = pygame.transform.scale(no_button, (150, 160))
# Pos
spr_x = 100
spr_y = 418
bg_move = 0
bg_move2 = 0
portal_x = 550
# Flags
start_jump = False
can_go_up = True
hit_left_border = False
hit_right_border = False
blocking = False
# Rectangles around images
img_rect = play_button.get_rect(center=(425, 240))
img_rect2 = exit_button.get_rect(center=(400, 350))
img_rect3 = settings_button.get_rect(center=(730, 60))
img_rect4 = check_button.get_rect(center=(400, 415))
img_rect5 = check_button2.get_rect(center=(400, 430))
img_rect6 = yes_button.get_rect(center=(300, 413))
img_rect7 = no_button.get_rect(center=(500, 413))
img_rect8 = resume_button.get_rect(center=(393, 350))
img_rect9 = settings_pause.get_rect(center=(393, 250))
img_rect10 = quit_pause.get_rect(center=(393, 150))
portal = pygame.image.load("portal.png")
portal = pygame.transform.scale(portal, (125, 125))
img_rect_portal = portal.get_rect(center=(625, 500))
img_rect_spr_idle = spr_idle_r.get_rect(center=(spr_x + 100, spr_y))
# Rectangles around sprites
spr_mask = pygame.mask.from_surface(spr_idle_r)
zomb_mask = pygame.mask.from_surface(zombie_idle_l)
cave_monster_mask = pygame.mask.from_surface(cave_monster)
# Constants
PLAYER_SPEED = 0.8
BG_SPEED = 1.7
ZOMB_SPEED = 1.2
BOSS_1_SPEED = 0.3

# Boss
'''
Old Version:
boss_lvl1 = pygame.image.load("final_boss_monster.png")
boss_lvl1 = pygame.transform.scale(boss_lvl1, (350, 350))
boss_lvl1_l = pygame.transform.flip(boss_lvl1, True, False)
'''
boss_lvl1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("final_boss_monster.png"), (350, 350)),
                                  True, False)
boss_x = 800
boss_hp = 30


# Functions
def jumping():
    global spr_y, start_jump, can_go_up
    JUMP_MAX = 390
    GROUND = 418
    if can_go_up:
        if spr_y > 409:
            spr_y -= 4
            return None
        elif 409 >= spr_y > 400:
            spr_y -= 2
            return None
        elif 400 >= spr_y > JUMP_MAX:
            spr_y -= 1.5
            return None
        elif spr_y <= JUMP_MAX:
            can_go_up = False
            spr_y += 1.5
            return None
    elif JUMP_MAX < spr_y <= 400:
        spr_y += 1.5
        return None
    elif 400 < spr_y <= 409:
        spr_y += 2
        return None
    elif 409 < spr_y < GROUND:
        spr_y += 4
        return None
    start_jump = False
    can_go_up = True


def update_portal_x():
    global portal_x
    # if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not hit_left_border:
    #     portal_x += BG_SPEED
    # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
    #     portal_x -= BG_SPEED


def key_inputs():
    global spr_x, spr_y, bg_move, start_jump, can_go_up, bg_move2, lives, hit_left_border, hit_right_border, blocking
    left_click = pygame.mouse.get_pressed()[0]
    right_click = pygame.mouse.get_pressed()[2]

    moving = False
    interacting = False
    blocking = right_click

    # Handling Attacking and Blocking:
    if left_click:
        global boss_hp, boss_x
        interacting = True
        img_rect_spr_atk = pygame.Rect(spr_x + 20, spr_y + 20, 70, 50)
        for i in range(len(zomb_x)):
            if img_rect_spr_atk.colliderect(pygame.Rect(zomb_x[i], zomb_y[i], 70, 50)) and zomb_lives[i] > 0:
                zomb_lives[i] -= 1
                zomb_x[i] += 35
        screen.blit(spr_attack_r, (spr_x, spr_y - 6))
        # img_rect_spr_atk = pygame.Rect(spr_x + 20, spr_y + 20, 70, 50)
        # img_rect_boss_1 = boss_lvl1_l.get_rect(center=(boss_x + 215, 374))
        # if img_rect_spr_atk.colliderect(img_rect_boss_1):
        #     boss_hp -= 1
        #     boss_x += 10
    elif right_click:
        interacting = True
        img_rect_spr_block = pygame.Rect(spr_x + 20, spr_y + 20, 70, 50)
        screen.blit(spr_block_r, (spr_x, spr_y - 10))
        pygame.draw.rect(screen, (255, 0, 0), img_rect_spr_block, 2)
        for i in range(len(zomb_x)):
            if img_rect_spr_block.colliderect(pygame.Rect(zomb_x[i], zomb_y[i], 70, 50)) and zomb_lives[i] > 0:
                spr_x -= 100
                bg_move += 100

    # Handling Left & Right Movement:
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        moving = True
        spr_x -= PLAYER_SPEED
        if not interacting:
            screen.blit(spr_walk_l, (spr_x, spr_y - 3))
        bg_move += BG_SPEED
        bg_move2 += BG_SPEED
        if hit_right_border:
            hit_right_border = False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        moving = True
        spr_x += PLAYER_SPEED
        if not interacting:
            screen.blit(spr_walk_r, (spr_x, spr_y - 3))
        bg_move -= BG_SPEED
        bg_move2 -= BG_SPEED
        if hit_left_border:
            hit_left_border = False

    # Handling Jumping:
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and not start_jump:
        moving = True
        start_jump = True
        can_go_up = True

    # Handling Idleness:
    if not moving and not interacting:
        screen.blit(spr_idle_r, (spr_x, spr_y))


def zombies():
    if game_state == "Playing":
        for i in range(len(zomb_x)):
            if zomb_lives[i] > 0:
                screen.blit(zombie_idle_l, (zomb_x[i], zomb_y[i]))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not hit_left_border:
                    zomb_x[i] += -ZOMB_SPEED + BG_SPEED
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    zomb_x[i] -= ZOMB_SPEED + BG_SPEED
                elif zomb_x[i] >= 175:
                    zomb_x[i] -= ZOMB_SPEED
                elif zomb_x[i] < 175:
                    zomb_x[i] = 250 + i * 20
    elif game_state == "Level_2":
        for i in range(len(zomb_x)):
            if zomb_lives[i] > 0:
                screen.blit(cave_monster, (zomb_x[i], zomb_y[i]))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not hit_left_border and not hit_right_border:
                    zomb_x[i] += -ZOMB_SPEED + BG_SPEED
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and not hit_left_border and not hit_right_border:
                    zomb_x[i] -= ZOMB_SPEED + BG_SPEED
                else:
                    zomb_x[i] -= ZOMB_SPEED


def boss_1():
    global boss_x, spr_x
    if zomb_lives[i] <= 0 and boss_hp > 0:
        boss_x -= BOSS_1_SPEED  # for constant boss movement

        print(spr_x)
        # screen.blit(boss_lvl1, (boss_x, 174))
        # img_rect_boss_1 = boss_lvl1.get_rect(center=(boss_x + 215, 374))
        # pygame.draw.rect(screen, (255, 0, 0), img_rect_boss_1, 2)

        # Handling Player-Relative Movement:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not hit_left_border and not hit_right_border:
            boss_x += -BOSS_1_SPEED + BG_SPEED
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and not hit_left_border and not hit_right_border:
            boss_x -= BOSS_1_SPEED + BG_SPEED
        else:
            boss_x -= BOSS_1_SPEED


def collision():
    global lives, spr_x, game_state, bg_move, boss_x

    if zomb_lives[-1] > 0:  # Last zombie life > 0, [-1] checks first element from the right side (the last element)
        # Entering this branch means the rightmost zombie is dead, and the rightmost zombie will always die last.
        for i in range(len(zomb_x)):
            if (zomb_lives[i] > 0 and spr_mask.overlap(zomb_mask, (spr_x + 50 - zomb_x[i], spr_y - zomb_y[i])) or
                    spr_mask.overlap(cave_monster_mask, (spr_x + 50 - zomb_x[i], spr_y - zomb_y[i]))):
                if not blocking:
                    lives -= 1
                spr_x -= 125
                bg_move += 75
    if boss_hp > 0:
        img_rect_boss_1 = boss_lvl1.get_rect(center=(boss_x + 215, 374))
        if img_rect_spr_idle.colliderect(img_rect_boss_1):
            boss_x += 165


        # Handling collision with final boss:

    if lives < 1:
        game_state = "Game_over"
    if lives == 2:
        screen.blit(blood, (650, 400))
    elif lives == 1:
        screen.blit(blood, (-175, -50))
        screen.blit(blood, (650, 400))
    if spr_x > 440 and game_state == "Playing":
        screen.blit(portal, (portal_x, 385))
        print(11111)
        pygame.draw.rect(screen, (255, 0, 0), img_rect_portal, 2)


def reset_zombie_lives():
    global zomb_lives
    for i in range(len(zomb_lives)):
        zomb_lives[i] = 3


def hearts(screen, x, y, lives):
    for i in range(lives):
        print(f'lives: {lives}')
        hp_rect = hp.get_rect()
        hp_rect.x = x + 40 * i
        hp_rect.y = y
        screen.blit(hp, hp_rect)


def bound():
    global spr_x, bg_move, bg_move2, hit_left_border, hit_right_border
    if game_state == "Playing":
        if spr_x < 105:
            spr_x = 110
            bg_move = -3.6
            hit_left_border = True
        if spr_x > 600:
            spr_x = 595
            bg_move = -695
            hit_right_border = True
    elif game_state == "Level_2":
        if spr_x < 107:
            spr_x = 108
            bg_move2 = -17
            hit_left_border = True
        elif spr_x > 472:
            spr_x = 470
            bg_move2 = -773
            hit_right_border = True


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_state = "Paused"
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # Checks for collision with mouse
            if img_rect.collidepoint(event.pos):
                game_state = "Welcome Screen"
            elif img_rect2.collidepoint(event.pos):
                game_state = "Exit"
            elif img_rect3.collidepoint(event.pos):
                game_state = "Settings"
            elif img_rect4.collidepoint(event.pos):
                game_state = "Main"
            elif img_rect5.collidepoint(event.pos):
                game_state = "Playing"
            elif img_rect6.collidepoint(event.pos):
                game_state = "Main"
            elif img_rect7.collidepoint(event.pos) or img_rect8.collidepoint(event.pos):
                game_state = "Exit"
            elif img_rect9.collidepoint(event.pos):
                game_state = "Settings"
            elif img_rect10.collidepoint(event.pos):
                game_state = "Playing"
    # Game states
    if game_state == "Main":
        lives = 3
        spr_x = 100
        bg_move = 0
        bg_move2 = 0
        num_zombies = random.randint(2, 5)
        zomb_x = []
        zomb_y = []
        zomb_lives = []
        # Set initial values for zombies
        for i in range(num_zombies):
            zomb_x.append(850 + i * 100)
            zomb_y.append(443)
            zomb_lives.append(3)
        screen.blit(starting, (0, 0))
        screen.blit(play_button, (250, 150))
        starting = pygame.transform.scale(starting, (width, height))
        screen.blit(exit_button, (250, 300))
        starting = pygame.transform.scale(starting, (width, height))
        screen.blit(settings_button, (700, 20))
        img_rect = play_button.get_rect(center=(400, 220))
        img_rect2 = exit_button.get_rect(center=(400, 375))
        img_rect3 = settings_button.get_rect(center=(745, 60))
        img_rect4 = check_button.get_rect(center=(400, 415))
        img_rect5 = check_button2.get_rect(center=(400, 430))
    elif game_state == "Playing":
        update_portal_x()
        img_rect_portal = portal.get_rect(center=(625, 500))
        img_rect_spr_idle = spr_idle_r.get_rect(center=(spr_x, spr_y))
        if img_rect_spr_idle.colliderect(img_rect_portal):
            game_state = "Level_2"
            for i in range(len(zomb_x)):
                zomb_x[i] = 800 + i * 100
            spr_x = 108
            bg_move2 = -17
            reset_zombie_lives()
        screen.blit(lvl1_bk, (bg_move, 0))
        screen.blit(lvl1_bk, (width + bg_move, 0))
        hearts(screen, 0, 5, lives)
        key_inputs()
        collision()
        zombies()
        boss_1()
        bound()
        if start_jump:
            jumping()
        img_rect5 = check_button2.get_rect(center=(1000, 1000))
        img_rect6 = yes_button.get_rect(center=(1000, 1000))
        img_rect7 = no_button.get_rect(center=(1000, 1000))
        img_rect8 = resume_button.get_rect(center=(1000, 1000))
        img_rect9 = settings_pause.get_rect(center=(1000, 1000))
        img_rect10 = quit_pause.get_rect(center=(1000, 1000))
    elif game_state == "Welcome Screen":
        screen.blit(lvl1_bk, (0, 0))
        screen.blit(wlc_tab, (200, 50))
        screen.blit(check_button2, (325, 400))
        img_rect = play_button.get_rect(center=(1000, 1000))
        img_rect2 = exit_button.get_rect(center=(1000, 1000))
        img_rect3 = settings_button.get_rect(center=(1000, 1000))
        img_rect4 = check_button.get_rect(center=(1000, 1000))
        img_rect5 = check_button2.get_rect(center=(400, 475))
        img_rect6 = yes_button.get_rect(center=(1000, 1000))
        img_rect7 = no_button.get_rect(center=(1000, 1000))
        img_rect8 = resume_button.get_rect(center=(1000, 1000))
        img_rect9 = settings_pause.get_rect(center=(1000, 1000))
        img_rect10 = quit_pause.get_rect(center=(1000, 1000))
    elif game_state == "Exit":
        pygame.quit()
    elif game_state == "Settings":
        screen.blit(settings_tab, (205, 100))
        screen.blit(check_button, (310, 400))
        img_rect5 = check_button2.get_rect(center=(400, 475))
    elif game_state == "Game_over":
        screen.blit(game_over, (0, 0))
        screen.blit(yes_button, (225, 400))
        screen.blit(no_button, (425, 413))
        img_rect6 = yes_button.get_rect(center=(300, 490))
        img_rect7 = no_button.get_rect(center=(500, 490))
    elif game_state == "Paused":
        screen.blit(pause_menu, (125, -35))
        screen.blit(resume_button, (290, 110))
        screen.blit(settings_pause, (290, 200))
        screen.blit(quit_pause, (290, 290))
        img_rect8 = resume_button.get_rect(center=(393, 350))
        img_rect9 = settings_pause.get_rect(center=(393, 250))
        img_rect10 = quit_pause.get_rect(center=(393, 150))
    elif game_state == "Level_2":
        screen.blit(lvl2_bk, (bg_move2, 0))
        screen.blit(lvl2_bk, (width + bg_move2, 0))
        hearts(screen, 0, 5, lives)
        key_inputs()
        collision()
        zombies()
        bound()
    if start_jump:
        jumping()
    # print(spr_x, bg_move, zomb_lives)
    pygame.display.update()
    clock.tick(60)

# add boss
# Add level 2-5
