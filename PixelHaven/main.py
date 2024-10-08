# Name: Ajay Saini
# Date: May 22nd
# Purpose: To create a game for the ICS3U0 course.

import pygame
import random
from pygame.constants import MOUSEBUTTONDOWN

width, height = 800, 600  # Initializes width and height
pygame.display.set_caption("PixelHaven: Realms of Wonders")
pygame.init()  # initializes pygame
screen = pygame.display.set_mode((width, height))  # initializes screen (makes the screen)
clock = pygame.time.Clock()  # initializes clock (makes the clock)
game_state = "Login"  # makes the gamestate start off at main
starting = pygame.image.load("starting.png")
# HP
hp = pygame.image.load("hp.png")  # loads hp image
hp = pygame.transform.scale(hp, (50, 50))  # scales hp image
# Blood
blood = pygame.image.load("blood.png")  # loads blood
blood = pygame.transform.scale(blood, (500, 500))  # scales blood
# Play Button
play_button = pygame.image.load("play_button.png")  # loads play button
play_button = pygame.transform.scale(play_button, (300, 150))  # Scales play button
# Exit Button
exit_button = pygame.image.load("exit_button.png")  # Loads exit button
exit_button = pygame.transform.scale(exit_button, (300, 150))  # Scales exit button
# Settings Button
settings_button = pygame.image.load("settings_button.png")  # Loads settings button
settings_button = pygame.transform.scale(settings_button, (85, 85))  # Scales settings button
# Pause Menu
pause_menu = pygame.image.load("pause_menu.png")  # Loads pause menu
pause_menu = pygame.transform.scale(pause_menu, (550, 575))  # Scales pause menu
resume_button = pygame.image.load("resume_button.png")  # Loads resume button
resume_button = pygame.transform.scale(resume_button, (200, 100))  # Scales resume button
settings_pause = pygame.image.load("settings_pause.png")  # Loads settings button 2
settings_pause = pygame.transform.scale(settings_pause, (200, 100))  # Scales settings button 2
quit_pause = pygame.image.load("quit_pause.png")  # Loads quit button for pause menu
quit_pause = pygame.transform.scale(quit_pause, (200, 100))  # Scales pause menu quit button
# Check Button
check_button = pygame.image.load("check_button.png")  # loads check mark button
check_button = pygame.transform.scale(check_button, (200, 200))  # Scales check mark button
check_button2 = pygame.image.load("check_button2.png")  # Loads check mark button 2
check_button2 = pygame.transform.scale(check_button2, (150, 150))  # Scales check mark button 2
# Settings Tab
settings_tab = pygame.image.load("settings_tab.png")  # Loads settings tab
settings_tab = pygame.transform.scale(settings_tab, (390, 440))  # Scales settings tab
# Level 1 background:
lvl1_bk = pygame.image.load("Level_1.jpg")  # Loads level one background
lvl1_bk = pygame.transform.scale(lvl1_bk, (width, height))  # Scales level one background
# Level 2 background:
lvl2_bk = pygame.image.load("Level_2.jpg")  # Loads level two background
lvl2_bk = pygame.transform.scale(lvl2_bk, (width, height))  # Scales level two background
# Welcome Tab
wlc_tab = pygame.image.load("Welcome_tab.png")  # Loads welcome tab
wlc_tab = pygame.transform.scale(wlc_tab, (400, 500))  # Scales welcome tab
# Game Over Tab
game_over = pygame.image.load("game_over.png")  # Loads game over image
game_over = pygame.transform.scale(game_over, (width, height))  # SCALES game over tab
# Sprite
spr_idle_r = pygame.image.load("sprite_idle_right.png")  # Loads sprite idle right
spr_idle_r = pygame.transform.scale(spr_idle_r, (100, 100))  # scales sprite idle right
spr_walk_r = pygame.image.load("sprite_walk_right.png")  # loads sprite walk right
spr_walk_r = pygame.transform.scale(spr_walk_r, (105, 105))  # Scales sprite walk right
spr_idle_l = pygame.image.load("sprite_idle_right.png")  # loads sprite idle left
spr_walk_l = pygame.transform.scale(spr_walk_r, (75, 75))  # scales sprite idle left
spr_walk_l = pygame.transform.flip(spr_walk_r, True, False)  # flips sprite idle right so it looks to the left
spr_attack_r = pygame.image.load("spr_attack_r.png")  # loads attack to the right
spr_attack_r = pygame.transform.scale(spr_attack_r, (105, 105))  # scales attacking to the right image
spr_block_r = pygame.image.load("spr_block_r.png")  # loads sprite block right
spr_block_r = pygame.transform.scale(spr_block_r, (110, 110))  # Scales sprite block right
# Zombie
zombie_idle_r = pygame.image.load("zombie_idle_r.png")  # Loads zombie right
zombie_idle_r = pygame.transform.scale(zombie_idle_r, (63, 63))  # scales zombie right
zombie_idle_l = pygame.transform.flip(zombie_idle_r, True, False)  # flips right image zombie to the left
cave_monster = pygame.image.load("cave_monster.png")  # loads cave monster image
cave_monster = pygame.transform.scale(cave_monster, (63, 63))  # scales cave monster image
num_zombies = random.randint(2, 5)  # makes a random number from 2-5 for amount of zombies that may spawn
zomb_x = []  # creates a list for zombie x cord
zomb_y = []  # creates a list for zombie y cord
zomb_lives = []  # creates a list for zombie hp
for i in range(num_zombies):  # creates a for loop for amount of zombies
    zomb_x.append(850 + i * 100)  # spawns zombie at 850, and at each zombie after the first zombie is 100 cords further
    zomb_y.append(443)  # Spawns all zombies at 443 y cord
    zomb_lives.append(3)  # appends 3 lives for each zombie
# Lives
lives = 3  # creates lives for player
# Pos
spr_x = 100  # sprite spawn position
spr_y = 418  # sprite spawn posistion y axis
bg_move = 0  # initializes bg_move to 0
bg_move2 = 0  # initializes bg_move2 to 0
portal_x = 0  # initializes portals x cord to 0
# Flags
start_jump = False  # initializes start_jump to False
can_go_up = True  # initializes can_go_up to True
hit_left_border = False  # initializes hit_left_border to False
hit_right_border = False  # initializes hit_right_border to False
blocking = False  # initializes blocking to False
can_spawn_fireball = True  # initializes can_spawn_fireball to True
sign_in_check = False  # initializes sign_in_check to False
# Rectangles around images
img_rect = play_button.get_rect(center=(425, 240))  # Creates a rectangle around the play button
img_rect2 = exit_button.get_rect(center=(400, 350))  # Creates a rectangle around the exit button
img_rect3 = settings_button.get_rect(center=(730, 60))  # Creates a rectangle around the settings button
img_rect4 = check_button.get_rect(center=(400, 415))  # Creates a rectangle around the check mark button 1
img_rect5 = check_button2.get_rect(center=(400, 430))  # Creates a rectangle around the check mark button 2
img_rect7 = exit_button.get_rect(center=(400, 350))  # Creates a rectangle around the 2nd exit button
img_rect8 = resume_button.get_rect(center=(393, 350))  # Creates a rectangle around the resume button for pause menu
img_rect9 = settings_pause.get_rect(
    center=(393, 250))  # Creates a rectangle around the the settings button on pause menu
img_rect10 = quit_pause.get_rect(center=(393, 150))  # Creates a rectangle around the quit button on pause menu
portal = pygame.image.load("portal.png")  # Loads portal image
portal = pygame.transform.scale(portal, (125, 125))  # Scales portal image
img_rect_portal = portal.get_rect(center=(portal_x + 75, 500))  # Creates a rectangle around the portal
img_rect_spr_idle = spr_idle_r.get_rect(center=(spr_x + 200, spr_y))  # Creates a rectangle around the sprite idle pos
# Rectangles around sprites
spr_mask = pygame.mask.from_surface(spr_idle_r)  # Creates a mask around the sprite idle right
zomb_mask = pygame.mask.from_surface(zombie_idle_l)  # Creates a mask around the zombie
cave_monster_mask = pygame.mask.from_surface(cave_monster)  # Creates a mask around the cave monster
# Boss
boss_lvl1 = pygame.image.load("final_boss_monster.png")  # Loads boss lvl 1 image
boss_lvl1 = pygame.transform.scale(boss_lvl1, (350, 350))  # Scales boss lvl 1 image
boss_lvl1 = pygame.transform.flip(boss_lvl1, True, False)  # Flips boss to look to the left
boss_x = 800  # Starting boss pos
boss_hp = 30  # Boss HP
# Boss 2
boss_lvl2 = pygame.image.load("boss_lvl2.png")  # Loads boss image 2
boss_lvl2 = pygame.transform.scale(boss_lvl2, (350, 350))  # scales boss lvl2 image
boss_x2 = 1000  # starting pos of boss 2
boss_hp2 = 30  # hp for boss 2
# Boss Fireball
falling_fireball = pygame.image.load("falling_fireball.png")  # Loads falling fireball image
falling_fireball = pygame.transform.scale(falling_fireball, (125, 125))  # Scales falling fireball image
# Boss Rocks
falling_rock = pygame.image.load("falling_rock.png")  # Loads falling rock image
falling_rock = pygame.transform.scale(falling_rock, (125, 125))  # Scales falling rock image
img_rect_fireball = None  # Makes no rectangle around fireball but is needed so the rect is in the global scope
num_of_fireballs = random.randint(5, 12)  # Creates a random amount of fire balls from 5-12
fireballs_x = []  # Makes a list for the fireballs x pos
fireballs_y = []  # Makes a list for the fireballs y pos
fireballs_hitbox = []  # Makes a list for the fireballs hitbox
# Constants
PLAYER_SPEED = 0.8  # Player speed
BG_SPEED = 1.7  # Background lvl 1 speed
ZOMB_SPEED = 1.2  # Zombie speed
BOSS_1_SPEED = 0.3  # Boss 1 speed
BOSS_2_SPEED = 0.6  # Boss 2 speed
FIREBALL_RADIUS = 300  # How much to the left or right that the fireballs can spawn relative to the player
FIREBALL_Y_SPAWN = -125  # Starting y pos
SWING_DURATION = 5  # starting amount for the duration for the swing (Swing cooldown)

# Winner screen
winner_screen = pygame.image.load("winner_screen.png")  # Loads winner screen
winner_screen = pygame.transform.scale(winner_screen, (width, height))  # Scales winner screen
# Fill fireball coordinate lists:
for fireball in range(num_of_fireballs):  # checks the amount of fireballs and runs the for loop that many times
    fireballs_x.append(300)  # default values
    fireballs_y.append(FIREBALL_Y_SPAWN)  # default value
    fireballs_hitbox.append(
        None
    )  # predetermine number of hitboxes (these will be later replaced with real hitbox rectangles)
# Misc.
swing_timer = SWING_DURATION  # Swing cooldown

# Boss Bar
thirty_hp = pygame.image.load("30_hp.png")  # LOADS AND SCALES ALL IMAGES FOR BOSS BAR
thirty_hp = pygame.transform.scale(thirty_hp, (200, 100))
twenty_seven_hp = pygame.image.load("27_hp.png")
twenty_seven_hp = pygame.transform.scale(twenty_seven_hp, (200, 100))
twenty_four_hp = pygame.image.load("24_hp.png")
twenty_four_hp = pygame.transform.scale(twenty_four_hp, (200, 100))
twenty_one_hp = pygame.image.load("21_hp.png")
twenty_one_hp = pygame.transform.scale(twenty_one_hp, (200, 100))
eighteen_hp = pygame.image.load("18_hp.png")
eighteen_hp = pygame.transform.scale(eighteen_hp, (200, 100))
fifteen_hp = pygame.image.load("15_hp.png")
fifteen_hp = pygame.transform.scale(fifteen_hp, (200, 100))
twelve_hp = pygame.image.load("12_hp.png")
twelve_hp = pygame.transform.scale(twelve_hp, (200, 100))
nine_hp = pygame.image.load("9_hp.png")
nine_hp = pygame.transform.scale(nine_hp, (200, 100))
six_hp = pygame.image.load("6_hp.png")
six_hp = pygame.transform.scale(six_hp, (200, 100))
three_hp = pygame.image.load("3_hp.png")
three_hp = pygame.transform.scale(three_hp, (200, 100))
zero_hp = pygame.image.load("0_hp.png")
zero_hp = pygame.transform.scale(zero_hp, (200, 100))


# Functions
def jumping():  # Defines jumpiung function
    global spr_y, start_jump, can_go_up  # globalizes variables that are needed in global scope
    JUMP_MAX = 390  # Max jump height
    GROUND = 418  # Ground
    if can_go_up:  # If you can go up,
        if spr_y > 409:  # if the spr_y is greater than 409 y cord, jump -4 cords
            spr_y -= 4
            return None  # Return none
        elif 409 >= spr_y > 400:  # If spr_y is between 400 and 409, jump -2 cords
            spr_y -= 2
            return None  # Return None
        elif 400 >= spr_y > JUMP_MAX:  # If spr_y is between 400 and 390 (JUMP MAX), jump -1.5 cords
            spr_y -= 1.5
            return None  # Return None
        elif spr_y <= JUMP_MAX:  # If spr_y is less than jump max, can_go_up is False, and you add 1.5 cords
            can_go_up = False
            spr_y += 1.5
            return None  # Return None
    elif JUMP_MAX < spr_y <= 400:  # if spr_y is between 390 (jump max) and 400, go up 1.5 cords
        spr_y += 1.5
        return None  # Return None
    elif 400 < spr_y <= 409:  # If spr_y is betqween 400 and 409, add 2 cords
        spr_y += 2
        return None  # Return None
    elif 409 < spr_y < GROUND:  # If spr is betqween 409 and ground (418), add 4 cords
        spr_y += 4
        return None  # Return None
    start_jump = False  # Sets start_jump to False
    can_go_up = True  # Sets can_go_up to True


def update_portal_x():
    global portal_x, img_rect_portal  # Globalizes variables needed
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not hit_left_border:
        portal_x += BG_SPEED  # If you go left and are not hitting the left border, ther portal will go away from you.
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        portal_x -= BG_SPEED  # If you go right, the portal will come towards you
    img_rect_portal = portal.get_rect(center=(portal_x + 75, 500))  # Creates a rectangle around the portal


def key_inputs():
    global spr_x, spr_y, bg_move, start_jump, can_go_up, bg_move2, lives, hit_left_border, hit_right_border, blocking, swing_timer, boss_x2, boss_hp2  # Globalizes variables needed
    left_click = pygame.mouse.get_pressed()[0]  # initializes left_click with clicking left on the mouse
    right_click = pygame.mouse.get_pressed()[2]  # initializes right_click with clicking right on the mouse

    moving = False  # Moving is set to False
    interacting = False  # Interacting is set to False
    blocking = right_click  # Blocking is set to right_click

    # Handling Attacking and Blocking:
    if left_click and swing_timer > 0:  # Checks if you are pressing the left click and the swing timer is greater than 0
        global boss_hp, boss_x  # Globalizes variables needed
        interacting = True  # Sets interacting to true
        img_rect_spr_atk = pygame.Rect(spr_x + 20, spr_y + 20, 70,
                                       50)  # Creates rectangle around the spr attacking image
        for i in range(
                len(zomb_x)):  # checks the length of the zombies x cords, and iterates the loops that many times .
            if img_rect_spr_atk.colliderect(
                    pygame.Rect(zomb_x[i], zomb_y[i], 70,
                                50)) and zomb_lives[i] > 0:
                zomb_lives[i] -= 1
                zomb_x[
                    i] += 35  # If the attacking image collides with the zombies rect and the zombie lives are greater than 0, zombie loses 1 life, and it gets knocked back 35.
        screen.blit(spr_attack_r, (spr_x, spr_y - 6))  # Blits image onto the screen

        # Deal damage to the boss:
        img_rect_spr_atk = pygame.Rect(spr_x + 20, spr_y + 20, 70, 50)  # Creates rect for the sprite attack image
        img_rect_boss_1 = boss_lvl1.get_rect(center=(boss_x + 215, 374))  # Creates rect for the boss
        if img_rect_spr_atk.colliderect(
                img_rect_boss_1):  # If the spr_atk image collides with the boss rect, boss will lose 1 life and will get knocked back 10 cords
            boss_hp -= 1
            boss_x += 10
        img_rect_boss_2 = pygame.Rect(boss_x2, 300, 300, 225)  # Creates rect for the boss 2
        if img_rect_spr_atk.colliderect(
                img_rect_boss_2):  # If the spr_atk image collides with the boss2 rect, boss2 will lose 1 life and will get knocked back 10 cords
            boss_hp2 -= 1
            boss_x2 += 10

        # Decrement the swing timer:
        swing_timer -= 1  # Will slowly lose 1
    elif right_click:  # If you click right click, interacting is true
        interacting = True
        img_rect_spr_block = pygame.Rect(spr_x + 20, spr_y + 20, 70, 50)  # Creates a rect around the blocking img.
        screen.blit(spr_block_r, (spr_x, spr_y - 10))  # blits image onto screen
        for i in range(len(zomb_x)):  # Iterates once for each zombie in the game and stores its x pos
            if img_rect_spr_block.colliderect(
                    pygame.Rect(zomb_x[i], zomb_y[i], 70,
                                50)) and zomb_lives[
                i] > 0:  # If the block img collides with the zombie and the zombie lives are greater than 0, you wil move back 100 and the bg will also move back 100
                spr_x -= 100
                bg_move += 100

    # Handling Left & Right Movement:
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        moving = True
        spr_x -= PLAYER_SPEED  # If you move left, moving will become true, and the spr_x will move to the left at PLAYER_SPEED (0.8)
        if not interacting:
            screen.blit(spr_walk_l, (spr_x, spr_y - 3))  # If you are not interacting, blit the walking image
        bg_move += BG_SPEED  # when you hit the left arrow key, bg_move will go left at 1.7 (BG_SPEED)
        bg_move2 += BG_SPEED  # when you hit the left arrow key, bg_move2 will go left at 1.7 (BG_SPEED)
        if hit_right_border:
            hit_right_border = False  # If you hit the right border, set hit_right_border as False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        moving = True
        spr_x += PLAYER_SPEED  # If you hit the right arrow, moving is set to true, and spr_x will move to the left at PLAYER SPEED (0.8)
        if not interacting:
            screen.blit(spr_walk_r, (spr_x, spr_y - 3))  # If you are not interacting, blit the walking image
        bg_move -= BG_SPEED  # when you hit the right arrow key, bg_move will go right at 1.7 (BG_SPEED)
        bg_move2 -= BG_SPEED  # when you hit the right arrow key, bg_move2 will go right at 1.7 (BG_SPEED)
        if hit_left_border:
            hit_left_border = False  # If you hit the left border, hit_left_border will be set to False

    # Handling Jumping:
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and not start_jump:
        moving = True
        start_jump = True
        can_go_up = True  # If you hit the up arrow, moving is set to true, start_jump is set to true, and can go up is set to True

    # Handling Idleness:
    if not moving and not interacting:  # If you are not moving and not interacting, blit the idle image
        screen.blit(spr_idle_r, (spr_x, spr_y))

    # Reset swing timer:
    if not left_click:  # If you are not clicking left click, reset the swing_timer with SWING_DURATION
        swing_timer = SWING_DURATION


def zombies():
    if game_state == "Playing":  # Checks game_state as "Playing"
        for i in range(len(zomb_x)):  # Checks x pos for each zombie and do all of the following for each zombie
            if zomb_lives[i] > 0:  # if the zombies life is greater than 0
                screen.blit(zombie_idle_l, (zomb_x[i], zomb_y[i]))  # blit  zombie idle
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not hit_left_border:
                    zomb_x[
                        i] += -ZOMB_SPEED + BG_SPEED  # If you hit the left arrow, and didnt hit the left border, zomb_x is -zomb_speed + bg_speed (Makes player-zombie relative movement)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    zomb_x[
                        i] -= ZOMB_SPEED + BG_SPEED  # If you hit the right arrow, zomb_x is zomb_speed + bg_speed (Makes player-zombie relative movement)
                elif zomb_x[
                    i] >= 175:  # This code checks if the zombie reaches a certain point, it will tp it back,and then make a 20 coord gap between each zombie
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
                    zomb_x[i] -= ZOMB_SPEED  # ALL THE SAME CODE BUT FOR LEVEL TWO AND CAVE MONSTERS INSTEAD


def boss_1():
    global boss_x, spr_x, can_spawn_fireball

    # Updates boss movement, rendering, and relative position to player
    if zomb_lives[
        i] <= 0 and boss_hp > 0:  # If the zombies are dead and the boss_hp is greater than 0, the boss should move at 0.3 (BOSS_1_SPEED)
        boss_x -= BOSS_1_SPEED  # for constant boss movement

        screen.blit(boss_lvl1, (boss_x, 174))  # Blit the boss
        img_rect_boss_1 = boss_lvl1.get_rect(center=(boss_x + 215, 374))  # Make a rect around the boss

        # Handling Player-Relative Movement:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not hit_left_border and not hit_right_border:
            boss_x += -BOSS_1_SPEED + BG_SPEED  # If you go left, the boss should slow down to go out the frame
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and not hit_left_border and not hit_right_border:
            boss_x -= BOSS_1_SPEED + BG_SPEED  # If you go right, the boss should come towards you.
        else:
            boss_x -= BOSS_1_SPEED  # Otherwise, keep it at normal speed (0.3)

    # Fireballs to be reset after hitting the ground:
    if fireballs_y[
        0] > 350 and can_spawn_fireball == False:  # access and check the y-level of the first fireball (they all share the same y-coords anyway)
        can_spawn_fireball = True  # Sets can_spawn_fireball to True
    # Use Fireballs at a Certain HP Value:
    elif 0 < boss_hp <= 25:  # 0 exclusive as the fireballs should disappear when the boss is defeated
        run_fireballs()  # if the boss hp is between 0 and 25, run the fireballs

    # BLITS THE BOSS BAR AT CERTAIN HPS
    if boss_hp == 29 or boss_hp == 28 or boss_hp == 27:
        screen.blit(thirty_hp, (300, 10))
    elif boss_hp == 26 or boss_hp == boss_hp == 25 or boss_hp == 24:
        screen.blit(twenty_four_hp, (300, 10))
    elif boss_hp == 23 or boss_hp == 22 or boss_hp == 21:
        screen.blit(twenty_one_hp, (300, 10))
    elif boss_hp == 20 or boss_hp == 19 or boss_hp == 18:
        screen.blit(eighteen_hp, (300, 10))
    elif boss_hp == 17 or boss_hp == 16 or boss_hp == 15:
        screen.blit(fifteen_hp, (300, 10))
    elif boss_hp == 14 or boss_hp == 13 or boss_hp == 12:
        screen.blit(twelve_hp, (300, 10))
    elif boss_hp == 11 or boss_hp == 10 or boss_hp == 9:
        screen.blit(nine_hp, (300, 10))
    elif boss_hp == 8 or boss_hp == 7 or boss_hp == 6:
        screen.blit(six_hp, (300, 10))
    elif boss_hp == 5 or boss_hp == 4 or boss_hp == 3 or boss_hp == 2 or boss_hp == 1:
        screen.blit(three_hp, (300, 10))
    elif boss_hp == 0:
        screen.blit(zero_hp, (300, 10))


def run_fireballs():
    global fireballs_x, fireballs_y, fireballs_hitbox, can_spawn_fireball, img_rect_fireball  # Globalizes variables needed

    # RESETTING THE FIREBALL:
    # Determine random x-positions for all fireballs
    if game_state == "Playing":  # Checks playing game_state
        if can_spawn_fireball:  # if you can spawn the fireball
            for fireball_num in range(
                    len(fireballs_x)):  # checks the fireballs_x position for a random number (fireball_num) and it loops fireball_num amount of times
                spawn_x_pos = random.randint(
                    int(spr_x - 2 * FIREBALL_RADIUS),
                    int(spr_x + 0.5 * FIREBALL_RADIUS)
                )  # to determine a random spawn x-position near the player
                fireballs_x[
                    fireball_num] = spawn_x_pos  # initializes spawn_x_pos as the random x positions for the fireballs
                fireballs_y[
                    fireball_num] = FIREBALL_Y_SPAWN  # initializes FIREBALL_Y_SPAWN at the y positions for the fireballs
            can_spawn_fireball = False  # sets can_spawn fireballs to False

        # Spawn all fireballs at once
        for fireball_num in range(
                len(fireballs_x)):  # checks the fireballs_x position for a random number (fireball_num) and it loops fireball_num amount of times
            # Reference fireball coordinates
            fb_x = fireballs_x[
                fireball_num]  # accesses the x-coord. for this specific fireball number
            fb_y = fireballs_y[fireball_num]  # vice versa for the y-coord.

            # Create hitbox
            img_rect_fireball = pygame.Rect(fb_x + 28, fb_y + 40, 60, 60)  # Creates fireball hitbox
            fireballs_hitbox[fireball_num] = img_rect_fireball  # Makes the hitbox for each fireball

            screen.blit(falling_fireball, (fb_x, fb_y))  # Render fireball to the display

            # Adjust y-position
            fireballs_y[fireball_num] += 2  # to make the fireball move down

            # Adjust (relative to player) x-position
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not hit_left_border and not hit_right_border:
                fireballs_x[fireball_num] += BG_SPEED  # If you go left, fireball will slow down (X pos)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and not hit_left_border and not hit_right_border:
                fireballs_x[fireball_num] -= BG_SPEED  # If you go right, fireball will speed up  (X pos)
    if game_state == "Level_2":
        # EXACT SAME CODE BUT FOR FALLING ROCKS
        if can_spawn_fireball:
            for fireball_num in range(len(fireballs_x)):
                spawn_x_pos = random.randint(
                    int(spr_x - 2 * FIREBALL_RADIUS),
                    int(spr_x + 0.5 * FIREBALL_RADIUS)
                )  # to determine a random spawn x-position near the player
                fireballs_x[
                    fireball_num] = spawn_x_pos  # to leverage the randomly generated spawn x-positions near spr_x
                fireballs_y[fireball_num] = FIREBALL_Y_SPAWN
            can_spawn_fireball = False

            # Spawn all fireballs at once
        for fireball_num in range(len(fireballs_x)):
            # Reference fireball coordinates
            fb_x = fireballs_x[
                fireball_num]  # accesses the x-coord. for this specific fireball number
            fb_y = fireballs_y[fireball_num]  # vice versa for the y-coord.

            # Create hitbox
            img_rect_fireball = pygame.Rect(fb_x + 28, fb_y + 40, 60, 60)
            fireballs_hitbox[fireball_num] = img_rect_fireball
            # Render fireball to the display
            screen.blit(falling_rock, (fb_x, fb_y))

            # Adjust y-position
            fireballs_y[fireball_num] += 2  # to make the fireball move down

            # Adjust (relative to player) x-position
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not hit_left_border and not hit_right_border:
                fireballs_x[fireball_num] += BG_SPEED
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and not hit_left_border and not hit_right_border:
                fireballs_x[fireball_num] -= BG_SPEED


logins = ["Ajay", "AJ", "Ms. Enoch", "Enoch"]  # creates certain login passwords


def login_screen():  # Defines login_screen
    global logged_in
    sign_up = open("sign_in.txt", "r")  # Opens the file
    username = input("Please enter your username: ")  # Takes input for username, password, and the search checker.
    print("---------")
    pw = input("Please enter your password: ")
    print("---------")
    checker = input("If you would like to search for your username, press y, otherwise press n: ")

    if checker == 'y':  # Checks if the input is y from the checker
        search_username = input("Please enter your username: ")
        if search_username in logins:
            print("---------")
            print("This username is in use. Try again")  # If the username is in use, call the function again
            login_screen()
        else:
            print("---------")
            print(
                "Username is good")  # Otherwise, your username is okay and the logged_in variable is true (It will switch gamestate to main and  you can play)
            logged_in = True
    if username in logins and checker == 'n':
        print("---------")
        print(
            "Username is used. Try again")  # If you do not search for the username but it is being used, the function will be called
        login_screen()
    else:
        print("---------")
        print(
            'Login complete, return to (Output)')  # If everything is passed, login will be completed and it will switch gamestate to main and  you can play. It will also write all the text into the sign_in file.
        logged_in = True
        sign_up = open('sign_in.txt', "a")
        sign_up.write(username + "," + pw + '\n')


def collision():
    global lives, spr_x, spr_y, game_state, bg_move, img_rect_fireball, fireballs_hitbox
    img_rect_spr_atk = pygame.Rect(spr_x + 20, spr_y + 20, 70, 50)  # Creates rect for spr attack and spr block
    img_rect_spr_block = pygame.Rect(spr_x + 20, spr_y + 20, 70, 50)
    if zomb_lives[
        -1] > 0:  # Last zombie life > 0, [-1] checks first element from the right side (the last element)
        # Entering this branch means the rightmost zombie is dead, and the rightmost zombie will always die last.
        for i in range(len(zomb_x)):
            if (zomb_lives[i] > 0 and spr_mask.overlap(
                    zomb_mask, (spr_x + 50 - zomb_x[i], spr_y - zomb_y[
                        i]))  # If the spr_mask overlaps with the cave monster or zombie, and you are not blocking, you lose a life and get knocked back.
                    or spr_mask.overlap(
                        cave_monster_mask,
                        (spr_x + 50 - zomb_x[i], spr_y - zomb_y[i]))):
                if not blocking:
                    lives -= 1
                spr_x -= 125
                bg_move += 75
    if boss_hp > 0:
        img_rect_boss_1 = boss_lvl1.get_rect(center=(boss_x + 215,
                                                     374))  # If the bosses HP is greater than 0, it createa a rect, and then if it collides with the idle spr img, and you are not blocking you will lose 2 lives and get knocked back. If you are blocking you will only lose 1 life
        if img_rect_spr_idle.colliderect(img_rect_boss_1):
            spr_x -= 165
            if not blocking:
                lives -= 2
            else:
                lives -= 1
    if boss_hp2 > 0:
        img_rect_boss_2 = pygame.Rect(boss_x2, 300, 300, 225)  # Same code as above
        if img_rect_spr_idle.colliderect(img_rect_boss_2):
            if not blocking:
                lives -= 3
            else:
                lives -= 2

    if boss_hp <= 25 or boss_hp2 <= 25:  # meaning the boss has been damaged enough to spawn rocks
        for hitbox in fireballs_hitbox:
            if hitbox.colliderect(
                    img_rect_spr_idle or img_rect_spr_atk  # checks how many hitboxes there are, and then if it collides you lose all hp.
                    or img_rect_spr_block):
                lives -= 3  # instant loss due to contact with fire

        # Handling collision with final boss:

    if lives < 1:
        game_state = "Game_over"  # if you have less than 1 life, game state is game over.
    if lives == 2:
        screen.blit(blood, (650, 400))  # If your lives is 2, blit 1 blood, if you have 1 life then blit 2 bloods.
    elif lives == 1:
        screen.blit(blood, (-175, -50))
        screen.blit(blood, (650, 400))

    if game_state == "Playing" and boss_hp <= 0 and spr_x - portal_x <= 440:
        screen.blit(portal, (portal_x, 385))  # if you are in playing game_state, and boss is dead, blit portal


def reset_zombie_lives():
    global zomb_lives
    for i in range(len(zomb_lives)):
        zomb_lives[i] = 3  # resets zombie lives


def boss_2():
    global boss_x2, spr_x, can_spawn_fireball

    # Updates boss movement, rendering, and relative position to player
    if zomb_lives[
        i] <= 0 and boss_hp2 > 0:  # if zombie lifes is less than 0 and boss hp2 is greater than 0, make boss move
        boss_x2 -= BOSS_1_SPEED  # for constant boss movement

        screen.blit(boss_lvl2, (boss_x2, 174))  # Blit boss
        # Handling Player-Relative Movement:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not hit_left_border and not hit_right_border:
            boss_x2 += -BOSS_2_SPEED + BG_SPEED  # Relative movement - left boss will slow down, right - boss will speed up
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and not hit_left_border and not hit_right_border:
            boss_x2 -= BOSS_2_SPEED + BG_SPEED
        else:
            boss_x2 -= BOSS_2_SPEED  # otherwise normal speed

    # Fireballs to be reset after hitting the ground:
    if fireballs_y[
        0] > 350 and can_spawn_fireball == False:  # access and check the y-level of the first fireball (they all share the same y-coords anyway)
        can_spawn_fireball = True
    # Use Fireballs at a Certain HP Value:
    elif 0 < boss_hp2 <= 25:  # 0 exclusive as the fireballs should disappear when the boss is defeated
        run_fireballs()
    # BOSS BAR check
    if boss_hp2 == 29 or boss_hp2 == 28 or boss_hp2 == 27:
        screen.blit(thirty_hp, (300, 10))
    elif boss_hp2 == 26 or boss_hp2 == 25 or boss_hp2 == 24:
        screen.blit(twenty_four_hp, (300, 10))
    elif boss_hp2 == 23 or boss_hp2 == 22 or boss_hp2 == 21:
        screen.blit(twenty_one_hp, (300, 10))
    elif boss_hp2 == 20 or boss_hp2 == 19 or boss_hp2 == 18:
        screen.blit(eighteen_hp, (300, 10))
    elif boss_hp2 == 17 or boss_hp2 == 16 or boss_hp2 == 15:
        screen.blit(fifteen_hp, (300, 10))
    elif boss_hp2 == 14 or boss_hp2 == 13 or boss_hp2 == 12:
        screen.blit(twelve_hp, (300, 10))
    elif boss_hp2 == 11 or boss_hp2 == 10 or boss_hp2 == 9:
        screen.blit(nine_hp, (300, 10))
    elif boss_hp2 == 8 or boss_hp2 == 7 or boss_hp2 == 6:
        screen.blit(six_hp, (300, 10))
    elif boss_hp2 == 5 or boss_hp2 == 4 or boss_hp2 == 3 or boss_hp2 == 2 or boss_hp2 == 1:
        screen.blit(three_hp, (300, 10))
    elif boss_hp2 == 0:
        screen.blit(zero_hp, (300, 10))
    if boss_hp2 <= 0:
        global game_state
        game_state = "Winner"


def hearts(screen, x, y, lives):  # Makes hearts
    for i in range(lives):
        hp_rect = hp.get_rect()  # makes a rect around the heart
        hp_rect.x = x + 40 * i  # spaces hearts out by 40
        hp_rect.y = y  # makes the y pos of the heart y
        screen.blit(hp, hp_rect)  # blits hp and rect


def bound():
    global spr_x, bg_move, bg_move2, hit_left_border, hit_right_border
    if game_state == "Playing":  # If the game_state is playing, and the spr is less than 105, put it back to 110 and reset bg and make hit_left_border true
        if spr_x < 105:
            spr_x = 110
            bg_move = -3.6
            hit_left_border = True
        if spr_x > 600:  # Right side: If the spr_x > 600, make the spr_x move left by 5 and reset bg_move2.
            spr_x = 595
            bg_move = -695
            hit_right_border = True
    elif game_state == "Level_2":  # SAME AS ABOVE JUST LEVEL TWO NOW.
        if spr_x < 107:
            spr_x = 108
            bg_move2 = -17
            hit_left_border = True
        elif spr_x > 472:
            print(spr_x, bg_move2)
            spr_x = 470
            bg_move2 = -773
            hit_right_border = True


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Code for escape keydown
            game_state = "Paused"  # If you hit esc, make game_state paused
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # gets the pos of the mouse
            # Checks for collision with mouse
            if img_rect.collidepoint(
                    event.pos):  # If the mouse collides with the img_rect (play button) game_state is welcome screen
                game_state = "Welcome Screen"
            elif img_rect2.collidepoint(
                    event.pos):  # If the mouse collides with the img_rect2 (exit button) game_state is exit
                game_state = "Exit"
            elif img_rect3.collidepoint(
                    event.pos):  # If the mouse collides with the img_rect (settings icon ) game_state is settings
                game_state = "Settings"
            elif img_rect4.collidepoint(
                    event.pos):  # If the mouse collides with the img_rect (check mark) game_state is main
                game_state = "Main"
            elif img_rect5.collidepoint(
                    event.pos):  # If the mouse collides with the img_rect (check mark 2) game_state is Playing
                game_state = "Playing"
            elif img_rect7.collidepoint(event.pos) or img_rect8.collidepoint(
                    event.pos):  # If the mouse collides with the img_rect7 or 8 (Exit buttons) game_state is exit

                game_state = "Exit"
            elif img_rect9.collidepoint(
                    event.pos):  # # If the mouse collides with the img_rect9 (settings button (Pause menu)) game_state is settings
                game_state = "Settings"
            elif img_rect10.collidepoint(event.pos):
                game_state = "Playing"
    # Game states
    if game_state == 'Login':  # If the gamestate is login, call login.
        login_screen()
        if logged_in:  # If the sign in check is true, game_state is main
            game_state = 'Main'
    elif game_state == "Main":  # Game_state is main
        start_jump = False  # RESETTING VARIABLES
        can_go_up = True
        hit_left_border = False
        hit_right_border = False
        blocking = False
        lives = 3
        spr_x = 100
        boss_x = 800
        boss_hp = 30
        bg_move = -25
        bg_move2 = 0
        portal_x = 1400
        num_zombies = random.randint(2, 5)
        zomb_x = []
        zomb_y = []
        zomb_lives = []  # RESETTING VARIABLES

        # Set initial values for zombies
        for i in range(num_zombies):
            zomb_x.append(850 + i * 100)
            zomb_y.append(443)
            zomb_lives.append(3)
        screen.blit(starting, (0, 0))  # Blits starting screen
        screen.blit(play_button, (250, 150))  # Blits play button
        starting = pygame.transform.scale(starting, (width, height))  # scales starting
        screen.blit(exit_button, (250, 300))  # Blits exit button
        screen.blit(settings_button, (700, 20))  # blits settings button
        img_rect = play_button.get_rect(center=(
        400, 220))  # adds rectangles around play button, settings button, checkmark1 and checkmark2 buttons.
        img_rect2 = exit_button.get_rect(center=(400, 375))
        img_rect3 = settings_button.get_rect(center=(745, 60))
        img_rect4 = check_button.get_rect(center=(400, 415))
        img_rect5 = check_button2.get_rect(center=(400, 430))
    elif game_state == "Playing":  # If game state is playing:
        img_rect_portal = portal.get_rect(center=(portal_x + 75, 500))  # makes rect around portal
        img_rect_spr_idle = pygame.Rect(spr_x + 20, spr_y + 10, 50, 100)  # makes rect around spr idle img
        img_rect7 = exit_button.get_rect(center=(1000, 1000))  # moves exit button out of screen
        if img_rect_spr_idle.colliderect(
                img_rect_portal):  # If spr collides with portal, game_state is level 2 and lives reset
            game_state = "Level_2"
            lives = 3
            for fireball_num in range(
                    len(fireballs_y)):  # Iterates once for each fireball, and then resets the Y position.
                fireballs_y[fireball_num] = FIREBALL_Y_SPAWN
            for i in range(len(zomb_x)):
                zomb_x[i] = 800 + i * 100  # Resets the zombie position
            spr_x = 108
            bg_move2 = -17
            reset_zombie_lives()  # Calls reset zombie lives function
        # Level Background:
        screen.blit(lvl1_bk, (bg_move, 0))  # Blits level 1 background
        screen.blit(lvl1_bk, (width + bg_move, 0))  # blits lvl 1 background but adds width
        hearts(screen, 0, 5, lives)  # Calls hearts
        key_inputs()  # Calls key inputs3
        update_portal_x()  # Calls portals relative movement w/ sprite
        zombies()  # Calls zombies
        boss_1()  # Calls boss 1
        collision()  # Calls collison
        bound()  # Calls bounds
        if start_jump:  # if you can start your jump, call jump
            jumping()
        img_rect5 = check_button2.get_rect(center=(1000, 1000))  # Puts rectangles outside of screen
        img_rect8 = resume_button.get_rect(center=(1000, 1000))  # Puts rectangles outside of screen
        img_rect9 = settings_pause.get_rect(center=(1000, 1000))  # Puts rectangles outside of screen
        img_rect10 = quit_pause.get_rect(center=(1000, 1000))  # Puts rectangles outside of screen
    elif game_state == "Welcome Screen":  # WLC screen game state
        screen.blit(lvl1_bk, (0, 0))  # blits lvl 1 background
        screen.blit(wlc_tab, (200, 50))  # blits wlc_tab
        screen.blit(check_button2, (325, 400))  # blits second checkmark
        img_rect = play_button.get_rect(center=(1000, 1000))  # Puts rectangles outside of screen
        img_rect2 = exit_button.get_rect(center=(1000, 1000))  # Puts rectangles outside of screen
        img_rect3 = settings_button.get_rect(center=(1000, 1000))  # Puts rectangles outside of screen
        img_rect4 = check_button.get_rect(center=(1000, 1000))  # Puts rectangles outside of screen
        img_rect5 = check_button2.get_rect(center=(400, 475))
        img_rect8 = resume_button.get_rect(center=(1000, 1000))  # Puts rectangles outside of screen
        img_rect9 = settings_pause.get_rect(center=(1000, 1000))  # Puts rectangles outside of screen
        img_rect10 = quit_pause.get_rect(center=(1000, 1000))  # Puts rectangles outside of screen
    elif game_state == "Exit":
        pygame.quit()  # Quits
    elif game_state == "Settings":
        screen.blit(settings_tab, (205, 100))  # Blits settings tab and check mark
        screen.blit(check_button, (310, 400))
        img_rect5 = check_button2.get_rect(center=(400, 475))  # makes rect around second check mark
    elif game_state == "Game_over":  # Game state is game over
        screen.blit(game_over, (0, 0))  # blits game over screen
        img_rect7 = pygame.Rect(300, 450, 200, 100)
        screen.blit(exit_button, (250, 430))  # blits exit button
    elif game_state == "Paused":  # Paused game state
        screen.blit(pause_menu, (125, -35))  # blits paused menu
        screen.blit(resume_button, (290, 110))  # BLits Resume butto n
        screen.blit(settings_pause, (290, 200))  # Blits settings button on pause menu
        screen.blit(quit_pause, (290, 290))  # blits quit button on pause
        img_rect8 = resume_button.get_rect(center=(393, 350))  # rectangels around all those buttons
        img_rect9 = settings_pause.get_rect(center=(393, 250))
        img_rect10 = quit_pause.get_rect(center=(393, 150))
    elif game_state == "Level_2":
        screen.blit(lvl2_bk, (bg_move2, 0))  # blits level 2 background
        screen.blit(lvl2_bk, (width + bg_move2, 0))  # Blits level 2 bk with width added
        img_rect_spr_idle = pygame.Rect(spr_x + 20, spr_y + 10, 50, 100)  # Creates rect around sprite
        hearts(screen, 0, 5, lives)  # calls hearts
        key_inputs()  # calls key inputs
        collision()  # calls collison
        zombies()  # calls zombies
        bound()  # calls bounds
        boss_2()  # calls boss 2
    if start_jump:  # if you can start jump, call jump
        jumping()
    elif game_state == "Winner":  # Game state is winner
        screen.blit(winner_screen, (0, 0))  # blit the winner screen
        key_inputs()  # calls key inputs
        if start_jump:  # if you can start jump, call jump
            jumping()
    pygame.display.update()  # updates display
    clock.tick(60)  # FPS
