import pygame
from pygame.sprite import Group

import game_functions as gf

from settings import Settings
from spidey import Spidey
from venom import Venom
from bullet import *
from button import Button
from gameover_button import GO_button as GO
from gamestats import GameStats
from health_bar import HealthBar as HB
from health_bar import HealthBar_images as HB_I


def run_game():
    pygame.init()

    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.mixer.music.load('songs/8bit_bgm.wav')
    pygame.mixer.music.play(-1)

    svv_settings = Settings()
    stats = GameStats(svv_settings)

    screen = pygame.display.set_mode((
        svv_settings.screen_width, svv_settings.screen_height))
    pygame.display.set_caption("SPIDEY VS VENOM")

    play_button = Button(svv_settings, screen, "Click to Play")

    s_hb = HB(screen, 0, (255, 0, 0))
    v_hb = HB(screen, 1, (0, 0, 255))
    s_i_hb = HB_I(screen, 0)
    v_i_hb = HB_I(screen, 1)

    spidey = Spidey(svv_settings, screen)
    venom = Venom(svv_settings, screen)

    bullets = Group()
    venom_bullets = Group()
    vomit_bullets = Group()

    while True:

        if not stats.spidey_died and not stats.venom_died:
            gf.check_health_bar(s_hb, v_hb, stats)

            if stats.spidey_died or stats.venom_died:
                play_button = GO(screen, stats)

        if stats.spidey_died or stats.venom_died:
            play_button.update_image()

        gf.check_events(svv_settings, screen, stats, play_button, spidey,
                        bullets, venom, venom_bullets, vomit_bullets)
        gf.update_screen(svv_settings, screen, spidey, stats, play_button,
                         bullets, venom, venom_bullets, vomit_bullets
                         ,(s_hb, v_hb) , (s_i_hb, v_i_hb))

        if stats.game_active == False:
            s_hb.reset_health_bar()
            v_hb.reset_health_bar()

            spidey.center_spidey()
            venom.center_venom()

        if stats.game_active:
            stats.spidey_died = False
            stats.venom_died = False

            spidey.intro()
            venom.intro()

            if spidey.mask_on and venom.mask_on == True:
                spidey.update()
                venom.update()

                bullets.update()
                venom_bullets.update()
                vomit_bullets.update()

                gf.update_bullets(bullets, venom_bullets, vomit_bullets)
                gf.check_collisions(venom, spidey, venom_bullets,
                                    vomit_bullets, bullets, s_hb, v_hb)

        pygame.display.flip()

run_game()
