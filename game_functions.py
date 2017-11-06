import sys
import pygame
from bullet import *

# Temporary data for bullets allowed in svv_settings
list = []

def check_events(svv_settings, screen, stats, play_button, spidey, bullets, venom, venom_bullets, vomit_bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, svv_settings, screen, spidey, bullets, venom, venom_bullets, vomit_bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spidey, venom, svv_settings)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            check_play_button(svv_settings, screen, stats, play_button, spidey, bullets, venom, venom_bullets, vomit_bullets, mouse_x, mouse_y)


def check_play_button(svv_settings, screen, stats, play_button, spidey, bullets, venom, venom_bullets, vomit_bullets, mouse_x, mouse_y):

    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:

        svv_settings.start_dynamic_settings()
        pygame.mouse.set_visible(False)


        if play_button.rect.collidepoint(mouse_x,mouse_y):
            stats.game_active = True

            bullets.empty()
            venom_bullets.empty()
            vomit_bullets.empty()

            spidey.center_spidey()
            venom.center_venom()


def check_keydown_events(event, svv_settings, screen, spidey, bullets, venom, venom_bullets, vomit_bullets):
    global list

    """Respond to keypresses for Spidey."""

    if event.key == pygame.K_d:
        spidey.counter = 1
        spidey.moving_right = True

    elif event.key == pygame.K_a:
        spidey.counter = 0
        spidey.moving_left = True

    # While the user goes up and down, the bullet doesn't exist.
    elif event.key == pygame.K_w:
        spidey.moving_up = True
        list.append(svv_settings.bullets_allowed)
        ''' -1 does not exist because the bullets allowed is from 0 to n
         Therefore, while holding down W, the user cannot fire a bullet because 
         the condition is 0 to 5 bullets'''
        svv_settings.bullets_allowed = -1

    elif event.key == pygame.K_s:
        spidey.moving_down = True
        list.append(svv_settings.bullets_allowed)
        # -1 does not exist because the bullets allowed is from 0 to n
        # Therefore, while holding down S, the user cannot fire a bullet because the condition is 0 to 5 bullets
        svv_settings.bullets_allowed = -1

    elif event.key in [pygame.K_c, pygame.K_v]:
        spidey.punch = True


        if event.key == pygame.K_v:
            list.append(svv_settings.bullets_allowed)
            svv_settings.bullets_allowed = -1
            spidey.counter = 1
            sound = pygame.mixer.Sound('songs/punch_sound.wav')
            sound.play()

        elif event.key == pygame.K_c:
            list.append(svv_settings.bullets_allowed)
            svv_settings.bullets_allowed = -1
            spidey.counter = 0
            sound = pygame.mixer.Sound('songs/punch_sound.wav')
            sound.play()


    elif event.key in [pygame.K_g, pygame.K_f]:
        if len(bullets) <= svv_settings.bullets_allowed:
            spidey.shoot = True
            if event.key == pygame.K_g:
                spidey.counter = 1
                new_bullet = Webshot_right(svv_settings, screen, spidey)
                sound = pygame.mixer.Sound('songs/webshot_sound.wav')
                sound.play()

            elif event.key == pygame.K_f:
                spidey.counter = 0
                new_bullet = Webshot_left(svv_settings, screen, spidey)
                sound = pygame.mixer.Sound('songs/webshot_sound.wav')
                sound.play()

            bullets.add(new_bullet)

    elif event.key in [pygame.K_q, pygame.K_e]:
        spidey.swing = True


        if event.key == pygame.K_e:
            list.append(svv_settings.bullets_allowed)
            svv_settings.bullets_allowed = -1
            spidey.counter = 1
            sound = pygame.mixer.Sound('songs/webswing_sound.wav') #Load the Sound Effect File
            sound.play()
            #Music('songs/webswing_sound.mp3', 0.4, 0).sound_effects_settings()

        elif event.key == pygame.K_q:
            list.append(svv_settings.bullets_allowed)
            svv_settings.bullets_allowed = -1
            spidey.counter = 0
            sound = pygame.mixer.Sound('songs/webswing_sound.wav') #Load the Sound Effect File
            sound.play()
            #Music('songs/webswing_sound.mp3', 0.4, 0).sound_effects_settings()

    elif event.key in [pygame.K_r, pygame.K_t]:
        spidey.roll = True
        if event.key == pygame.K_t:
            spidey.counter = 1
        elif event.key == pygame.K_r:
            spidey.counter = 0

    '''Venom's movements based on its own keypresses'''

    if event.key == pygame.K_RIGHT:
        venom.counter = 1
        venom.moving_right = True

    elif event.key == pygame.K_LEFT:
        venom.counter = 0
        venom.moving_left = True


    elif event.key == pygame.K_UP:
        venom.moving_up = True
        list.append(svv_settings.bullets_allowed)
        svv_settings.bullets_allowed = -1


    elif event.key == pygame.K_DOWN:
        venom.moving_down = True
        list.append(svv_settings.bullets_allowed)
        svv_settings.bullets_allowed = -1


    elif event.key in [pygame.K_m, pygame.K_n]:
        venom.punch = True


        if event.key == pygame.K_m:
            list.append(svv_settings.bullets_allowed)
            svv_settings.bullets_allowed = -1
            venom.counter = 1
            sound = pygame.mixer.Sound('songs/punch_sound.wav')
            sound.play()
        elif event.key == pygame.K_n:
            list.append(svv_settings.bullets_allowed)
            svv_settings.bullets_allowed = -1
            venom.counter = 0
            sound = pygame.mixer.Sound('songs/punch_sound.wav')
            sound.play()


    elif event.key in [pygame.K_RIGHTBRACKET, pygame.K_LEFTBRACKET]:
        venom.vanish = True


        if event.key == pygame.K_RIGHTBRACKET:
            list.append(svv_settings.bullets_allowed)
            svv_settings.bullets_allowed = -1
            venom.counter = 1

        elif event.key == pygame.K_LEFTBRACKET:
            list.append(svv_settings.bullets_allowed)
            svv_settings.bullets_allowed = -1
            venom.counter = 0


    elif event.key in [pygame.K_l, pygame.K_k]:
        if len(venom_bullets) <= svv_settings.venom_bullets_allowed:
            venom.shoot = True
            if event.key == pygame.K_l:
                venom.counter = 1
                new_bullet = Venomshot_right(svv_settings, screen, venom)
                sound = pygame.mixer.Sound('songs/webshot_sound.wav')
                sound.play()


            elif event.key == pygame.K_k:
                venom.counter = 0
                new_bullet = Venomshot_left(svv_settings, screen, venom)
                sound = pygame.mixer.Sound('songs/webshot_sound.wav')
                sound.play()


            venom_bullets.add(new_bullet)

    elif event.key in [pygame.K_p, pygame.K_o]:
        if len(vomit_bullets) <= svv_settings.vomit_bullets_allowed:
            venom.vomit = True
            if event.key == pygame.K_p:
                list.append(svv_settings.bullets_allowed)
                svv_settings.bullets_allowed = -1
                venom.counter = 1
                new_bullet = Vomit_right(svv_settings, screen, venom)

            elif event.key == pygame.K_o:
                list.append(svv_settings.bullets_allowed)
                svv_settings.bullets_allowed = -1
                venom.counter = 0
                new_bullet = Vomit_left(svv_settings, screen, venom)

            vomit_bullets.add(new_bullet)


def check_keyup_events(event, spidey, venom, svv_settings):
    global list

    """Respond to key releases."""

    if event.key == pygame.K_d:
        spidey.moving_right = False

    elif event.key == pygame.K_a:
        spidey.moving_left = False

    elif event.key == pygame.K_w:
        if len(list) != 0:
            # When the user releases W, the first data from the list is taken, which is 5 bullets.
            # So, the user can fire the 5 bullets again.
            svv_settings.bullets_allowed = list[0]
            # This new declared list resets the temporary data
            list = []
        spidey.moving_up = False

    elif event.key == pygame.K_s:
        if len(list) != 0:
            # When the user releases W, the first data from the list is taken, which is 5 bullets.
            # So, the user can fire the 5 bullets again.
            svv_settings.bullets_allowed = list[0]
            # This new declared list resets the temporary data
            list = []
            spidey.moving_up = False
        spidey.moving_down = False

    elif event.key in [pygame.K_v, pygame.K_c]:
        if len(list) != 0:
            svv_settings.bullets_allowed = list[0]
            list = []
        spidey.punch = False

    elif event.key in [pygame.K_g, pygame.K_f]:
        spidey.shoot = False

    elif event.key in [pygame.K_e, pygame.K_q]:
        if len(list) != 0:
            svv_settings.bullets_allowed = list[0]
            list = []
        spidey.swing = False

    elif event.key in [pygame.K_r, pygame.K_t]:
        spidey.roll = False


    '''Key up events for Venom character'''


    if event.key == pygame.K_RIGHT:
        venom.moving_right = False

    elif event.key == pygame.K_LEFT:
        venom.moving_left = False

    elif event.key == pygame.K_UP:
        if len(list) != 0:
            svv_settings.bullets_allowed = list[0]
            list = []
        venom.moving_up = False

    elif event.key == pygame.K_DOWN:
        if len(list) != 0:
            svv_settings.bullets_allowed = list[0]
            list = []
            venom.moving_up = False

        venom.moving_down = False

    elif event.key in [pygame.K_m, pygame.K_n]:
        if len(list) != 0:
            svv_settings.bullets_allowed = list[0]
            list = []
        venom.punch = False

    elif event.key in [pygame.K_RIGHTBRACKET, pygame.K_LEFTBRACKET]:
        if len(list) != 0:
            svv_settings.bullets_allowed = list[0]
            list = []
        venom.vanish = False

    elif event.key in [pygame.K_l, pygame.K_k]:
        venom.shoot = False

    elif event.key in [pygame.K_p, pygame.K_o]:
        if len(list) != 0:
            svv_settings.bullets_allowed = list[0]
            list = []
        venom.vomit = False

def update_screen(svv_settings, screen, spidey, stats , play_button, bullets, venom, venom_bullets, vomit_bullets, healthbar,
                  healthbar_images):
    """Update images on the screen and flip to the new screen."""
    screen.fill(svv_settings.bg_color)

    for bullet in bullets:
        bullet.blitme()
    for venom_bullet in venom_bullets:
        venom_bullet.blitme()
    for vomit_bullet in vomit_bullets:
        vomit_bullet.blitme()

    spidey.blitme()
    venom.blitme()

    if stats.game_active:
        for i in healthbar_images:
            i.draw_HealthBar_images()

        for i in healthbar:
            i.draw_HealthBar()

    if not stats.game_active:
        play_button.draw_button()




def update_bullets(bullets, venom_bullets, vomit_bullets):

    for bullet in bullets.copy():
        if bullet.rect.left <= 0 or bullet.rect.right >= 700:
            bullets.remove(bullet)

    for venom_bullet in venom_bullets.copy():
        if venom_bullet.rect.left <= 0 or venom_bullet.rect.right >= 700:
            venom_bullets.remove(venom_bullet)

    for vomit_bullet in vomit_bullets.copy():
        if vomit_bullet.rect.left <= 0 or vomit_bullet.rect.right >= 700:
            vomit_bullets.remove(vomit_bullet)

    check_bullet_venombullet_collisions(bullets,venom_bullets)
    check_bullet_venombullet_collisions(bullets,vomit_bullets)


def check_bullet_venombullet_collisions(bullets,venombullets):
     pygame.sprite.groupcollide(bullets,venombullets,True,True)


def check_collisions(venom,spidey,venom_bullets,vomit_bullets,bullets, s_hb, v_hb):

    # s_hb stands for spidey_health_bar. v_hb stands for venom_health_bar

    for bullet in bullets.copy():
        if pygame.sprite.spritecollideany(venom, bullets) and len(bullets) != 0:
            bullets.remove(bullet)
            v_hb.update_HealthBar()

    for venom_bullet in venom_bullets.copy():
        if pygame.sprite.spritecollideany(spidey, venom_bullets) and len(venom_bullets) != 0:
            venom_bullets.remove(venom_bullet)
            s_hb.update_HealthBar()

    for vomit_bullet in vomit_bullets.copy():
        if pygame.sprite.spritecollideany(spidey, vomit_bullets) and len(vomit_bullets) != 0:
            vomit_bullets.remove(vomit_bullet)
            s_hb.update_HealthBar()

def check_health_bar(s_hb, v_hb, stats):

    if s_hb.get_health_bar() < 0:
        stats.spidey_died = True
        stats.game_active = False

    elif v_hb.get_health_bar() < 0:
        stats.venom_died = True
        stats.game_active = False
