import pygame
from pygame.sprite import Sprite

class Spidey(Sprite):

    def __init__(self, svv_settings, screen):

        super(Spidey,self).__init__()
        self.svv_settings = svv_settings
        self.screen = screen

        self.count = 0
        self.counter = 1

        self.image = pygame.image.load(
            'images/stand_spidey{}.png'.format(int(self.count%2)))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start spidey at the left bottom of the screen
        self.rect.left = self.screen_rect.left + 65
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # Movement flags
        self.mask_on = False
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.punch = False
        self.shoot = False
        self.swing = False
        self.roll = False
        self.descend = False

    def intro(self):
        if self.mask_on == False:
            if self.count % 6 < 4.9:
                self.intro_image = pygame.image.load('images/intro{}.png'.format(int(self.count%5)))
                self.big_intro_image = pygame.transform.scale(self.intro_image, (300,300))
                self.screen.blit(self.big_intro_image, (30,20))
                self.count += 0.046
            else:
                self.mask_on = True

    def update(self):

        self.centerx = self.rect.centerx
        self.centery = self.rect.centery



        if self.moving_right or self.moving_left or self.moving_up or self.moving_down or self.punch or self.shoot or self.swing or self.roll:
            pass
        else:
            self.image = pygame.image.load('images/stand_spidey{}.png'.format(int(self.count%2)))
            '''Modulo only outputs 0 and 1. Count is declared to start from 0.
             Every time the program is run, the count's value is increased by x.
             The value of count is continuously added up until a certain value such as 1 or 2.
             This value continuously undergoes modulo and outputs 0 and 1
             0 loads the first image, 1 loads the next one and so on.'''
            self.count += 0.035
            self.screen.blit(self.image, self.rect)


        if self.shoot and self.moving_right and self.rect.right < self.screen_rect.right:
            self.image = pygame.image.load(
                'images/running_attack_spidey{}.bmp'.format(int(self.count%3)))
            self.count += 0.125
            self.screen.blit(self.image, self.rect)
            self.centerx += self.svv_settings.spidey_speed_factor



        elif self.shoot and self.moving_left and self.rect.left > 0:
            self.image = pygame.transform.flip(pygame.image.load
                         ('images/running_attack_spidey{}.bmp'.format(int(self.count%3))),
                                               True, False)
            self.count += 0.125
            self.screen.blit(self.image, self.rect)
            self.centerx -= self.svv_settings.spidey_speed_factor

        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.image = pygame.image.load('images/running_spidey{}.bmp'.format(int(self.count%3)))
            self.count += 0.2
            self.screen.blit(self.image, self.rect)
            self.centerx += self.svv_settings.spidey_speed_factor

        elif self.moving_left and self.rect.left > 0:
            self.image = pygame.transform.flip(pygame.image.load(
                'images/running_spidey{}.bmp'.format(int(self.count%3))),True, False)
            self.count += 0.2
            self.screen.blit(self.image, self.rect)
            self.centerx -= self.svv_settings.spidey_speed_factor

        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.shoot = False
            self.image = pygame.image.load('images/climbing_spidey{}.bmp'.format(int(self.count%2)))
            self.count += 0.125
            self.screen.blit(self.image, self.rect)
            self.centery -= self.svv_settings.spidey_speed_factor

        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.shoot = False
            self.image = pygame.transform.flip(pygame.image.load(
                'images/climbing_spidey{}.bmp'.format(int(self.count%2))),True, False)
            self.count += 0.125
            self.screen.blit(self.image, self.rect)
            self.centery += self.svv_settings.spidey_speed_factor


        elif self.punch == True:
            if self.counter == 1:
                self.image = pygame.image.load('images/punch_spidey{}.png'.format(int(self.count%3)))
                self.screen.blit(self.image, self.rect)


            elif self.counter == 0:
                self.image = pygame.image.load('images/punch_spidey{}.png'.format(int(self.count%3)))
                self.flipped_image = pygame.transform.flip(self.image,True, False)
                self.screen.blit(self.flipped_image, self.rect)


        elif self.shoot == True:
            if self.counter == 1:
                self.image = pygame.image.load('images/shooting_spidey{}.png'.format(int(self.count%2)))
                self.screen.blit(self.image, self.rect)

            elif self.counter == 0:
                self.image = pygame.image.load('images/shooting_spidey{}.png'.format(int(self.count%2)))
                self.flipped_image = pygame.transform.flip(self.image,True, False)
                self.screen.blit(self.flipped_image, self.rect)


        elif self.roll == True:
            if self.roll and self.rect.right < self.screen_rect.right:
                if self.counter == 1:
                    self.image = pygame.image.load('images/roll_spidey{}.png'.format(int(self.count%8)))
                    self.count += 0.3
                    self.screen.blit(self.image, self.rect)
                    self.centerx += self.svv_settings.spidey_roll_sf

            if self.roll and self.rect.left > 0:
                if self.counter == 0:
                    self.image = pygame.image.load('images/roll_spidey{}.png'.format(int(self.count%8)))
                    self.count += 0.3
                    self.flipped_image = pygame.transform.flip(self.image,True, False)
                    self.screen.blit(self.flipped_image, self.rect)
                    self.centerx -= self.svv_settings.spidey_roll_sf

        elif self.swing == True:

            if self.swing and self.rect.right < self.screen_rect.right:
                if self.swing and self.rect.bottom < self.screen_rect.bottom:
                    if self.counter == 1:
                        self.image = pygame.image.load('images/b_swinging_spidey{}.png'.format(int(self.count%7)))
                        self.count += 0.125
                        self.screen.blit(self.image,self.rect)
                        self.centerx += self.svv_settings.spidey_swing_sf
                        if int(self.count%7) == 6 :
                            self.centery += (self.image.get_rect().height - 20)/8

            if self.swing and self.rect.left > 0:
                if self.swing and self.rect.bottom < self.screen_rect.bottom:

                    if self.counter == 0:
                        self.image = pygame.image.load('images/b_swinging_spidey{}.png'.format(int(self.count%7)))
                        self.count += 0.125
                        self.flipped_image = pygame.transform.flip(self.image,True,False)
                        self.screen.blit(self.flipped_image,self.rect)
                        self.centerx -= self.svv_settings.spidey_swing_sf
                        if int(self.count%7) == 6 :
                            self.centery += (self.image.get_rect().height - 20)/8

        self.rect.center = (self.centerx,self.centery)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_spidey(self):
        self.rect.left = self.screen_rect.left + 65
        self.rect.bottom = self.screen_rect.bottom
