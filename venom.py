import pygame
from pygame.sprite import Sprite

class Venom(Sprite):

    def __init__(self, svv_settings, screen):

        super(Venom,self).__init__()
        self.svv_settings = svv_settings
        self.screen = screen

        self.count = 0
        self.counter = 1

        self.image = pygame.image.load(
            'venom_images/standing_venom{}.png'.format(int(self.count%2)))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # Start venom at the bottom of the screen
        self.rect.right = self.screen_rect.right - 65
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # Movement flags
        self.mask_on = False
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.punch = False
        self.vanish = False
        self.shoot = False
        self.vomit = False

    def intro(self):
        if self.mask_on == False:
            if self.count % 5 < 3.9:
                self.intro_image = pygame.image.load('venom_images/intro_venom{}.png'.format(int(self.count%4)))
                self.big_intro_image = pygame.transform.scale(self.intro_image, (300,300))
                self.flipped_BIM = pygame.transform.flip(self.big_intro_image,True,False)
                self.count += 0.038
                self.screen.blit(self.flipped_BIM, (400,20))
            else:
                self.mask_on = True



    def update(self):

        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

        if self.moving_up or self.moving_down or self.moving_left or self.moving_right or self.punch or self.vanish or self.shoot or self.vomit:
            pass
        else:
            self.image = pygame.image.load('venom_images/standing_venom{}.png'.format(int(self.count%2)))
            self.count += 0.025
            self.screen.blit(self.image, self.rect)


        if self.shoot and self.moving_right and self.rect.right < self.screen_rect.right:
            self.image = pygame.image.load(
                'venom_images/running_attack_venom{}.png'.format(int(self.count%3)))
            self.count += 0.125
            self.screen.blit(self.image, self.rect)
            self.centerx += self.svv_settings.venom_speed_factor


        elif self.shoot and self.moving_left and self.rect.left > 0:
            self.image = pygame.transform.flip(pygame.image.load
                         ('venom_images/running_attack_venom{}.png'.format(int(self.count%3))),
                                               True, False)
            self.count += 0.125
            self.screen.blit(self.image, self.rect)
            self.centerx -= self.svv_settings.venom_speed_factor

        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.image = pygame.image.load('venom_images/running_venom{}.png'.format(int(self.count%3)))
            self.count += 0.2
            self.screen.blit(self.image, self.rect)
            self.centerx += self.svv_settings.venom_speed_factor

        elif self.moving_left and self.rect.left > 0:
            self.image = pygame.transform.flip(pygame.image.load(
                'venom_images/running_venom{}.png'.format(int(self.count%3))),True, False)
            self.count += 0.2
            self.screen.blit(self.image, self.rect)
            self.centerx -= self.svv_settings.venom_speed_factor


        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.shoot = False
            self.image = pygame.image.load('venom_images/climb_venom{}.png'.format(int(self.count%2)))
            self.count += 0.125
            self.screen.blit(self.image, self.rect)
            self.centery -= self.svv_settings.venom_speed_factor

        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.shoot = False
            self.image = pygame.transform.flip(pygame.image.load(
                'venom_images/climb_venom{}.png'.format(int(self.count%2))),True, False)
            self.count += 0.125
            self.screen.blit(self.image, self.rect)
            self.centery += self.svv_settings.venom_speed_factor




        elif self.punch == True:
            if self.counter == 1:
                self.image = pygame.image.load('venom_images/attack_venom.png')
                self.screen.blit(self.image, self.rect)

            elif self.counter == 0:
                self.ori_image = pygame.image.load('venom_images/attack_venom.png')
                self.image = pygame.transform.flip(self.ori_image,True,False)
                self.screen.blit(self.image, self.rect)


        elif self.shoot == True:
            if self.counter == 1:
                self.image = pygame.image.load('venom_images/shooting_venom.png')
                self.screen.blit(self.image, self.rect)

            elif self.counter == 0:
                self.ori_image = pygame.image.load('venom_images/shooting_venom.png')
                self.image = pygame.transform.flip(self.ori_image,True, False)
                self.screen.blit(self.image, self.rect)

        elif self.vanish == True and self.rect.right < self.screen_rect.right and self.rect.left > 0:
            if self.counter == 1:
                self.image = pygame.image.load('venom_images/vanish{}.png'.format(int(self.count%2)))
                self.count += 0.075
                self.screen.blit(self.image, self.rect)
                self.centerx += self.svv_settings.venom_vanish_sf


            elif self.counter == 0:
                self.ori_image = pygame.image.load('venom_images/vanish{}.png'.format(int(self.count%2)))
                self.count += 0.075
                self.image = pygame.transform.flip(self.ori_image,True, False)
                self.screen.blit(self.image, self.rect)
                self.centerx -= self.svv_settings.venom_vanish_sf

        elif self.vomit == True:
            if self.counter == 1:
                self.image = pygame.image.load('venom_images/vomit_venom{}.png'.format(int(self.count%2)))
                self.count += 0.075
                self.screen.blit(self.image, self.rect)

            elif self.counter == 0:
                self.ori_image = pygame.image.load('venom_images/vomit_venom{}.png'.format(int(self.count%2)))
                self.count += 0.075
                self.image = pygame.transform.flip(self.ori_image,True, False)
                self.screen.blit(self.image, self.rect)

        self.rect.center = (self.centerx,self.centery)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_venom(self):
        self.rect.right = self.screen_rect.right - 65
        self.rect.bottom = self.screen_rect.bottom
