import pygame

class HealthBar:
    def __init__(self, screen, location, color):
        self.screen = screen
        self.location = location
        self.screen_rect = self.screen.get_rect()

        # Adjusts the health bars' length based on the screen's width
        self.width = self.screen_rect.width / 3

        # Adjusts the health bars' height based on the screen's height
        self.height = self.screen_rect.height / 20

        self.color = color

    def update_HealthBar(self):

        # As long as the health bars aren't finished, it's length is reduced by 5%
        # This function is called in game_functions when the bullets collide with the characters

        if self.width != 0:
            self.width -= ((self.screen_rect.width / 2.3) * 5) / 100


    def draw_HealthBar(self):

        # 0 and 1 represents spidey's health bar on the left and venom's health bar on the right
        if self.location == 0:
            self.rect = pygame.Rect(0, 0, self.width, self.height)
        elif self.location == 1:
            self.rect = pygame.Rect(self.screen_rect.width - self.width, 0, self.width, self.height)

        self.screen.fill(self.color, self.rect)

    def get_health_bar(self):
        return self.width

    def reset_health_bar(self):
        self.width = self.screen_rect.width / 3


class HealthBar_images:
    def __init__(self, screen, location):
        self.screen = screen
        self.location = location
        self.screen_rect = self.screen.get_rect()

        # Adjusts the spidey spinning image based on the screen's width
        self.width = self.screen_rect.width / 1.52
        self.height = self.screen_rect.height / 30

        self.count = 0

    def draw_HealthBar_images(self):

        # 0 and 1 represents spidey's health bar on the left and venom's health bar on the right
        if self.location == 0:
            self.hb_images = pygame.image.load('venom_images/hb_venom_image{}.png'.format(int(self.count%9)))
            self.count += 0.035

            # (310,0,self.width,self.height) = 310 adjusts the X coordinate of where venom's spinning image will be loaded
            self.rect = pygame.Rect(440, 0, self.width, self.height)

        elif self.location == 1:
            self.hb_images = pygame.image.load('images/hb_spidey_image{}.png'.format(int(self.count%9)))
            self.count += 0.035

            # the X coordinate of spidey's spinning image is at the screen's width - the declared width above
            self.rect = pygame.Rect(self.screen_rect.width - self.width, 0, self.width, self.height)

        self.screen.blit(self.hb_images, self.rect)
