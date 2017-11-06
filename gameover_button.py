import pygame.ftfont

class GO_button:
    def __init__(self, screen, stats):
        self.stats = stats
        self.count = 0

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = self.screen_rect.width, self.screen_rect.height

        if self.stats.spidey_died:
            self.color = (102, 0, 204)
            self.text_color = (0, 204, 0)

        elif self.stats.venom_died:
            self.color = (0, 100, 0)
            self.text_color = (219,112,147)

        self.y = self.screen_rect.centery

        self.font = pygame.font.SysFont(None, 22)
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.msg_image = self.font.render("Game Over!", True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

        self.msg1_image = self.font.render("Click to Play Again!", True, self.text_color, self.color)
        self.msg1_image_rect = self.msg1_image.get_rect()
        self.msg1_image_rect.center = self.screen_rect.center
        self.msg1_image_rect.bottom = self.screen_rect.bottom

    def update_image(self):

        if self.stats.venom_died:
            sound = pygame.mixer.Sound('songs/spiderman_speech.wav')
            sound.play(0)
            self.win_spidey = pygame.image.load('images/mask_off_spidey{}.png'.format(int(self.count%6)))
            self.big_spidey_image = pygame.transform.scale(self.win_spidey, (200, 280))
            self.big_spidey_image_rect = self.big_spidey_image.get_rect()
            self.big_spidey_image_rect.center = (self.screen_rect.centerx/2, self.y)

            self.dying_venom = pygame.image.load('venom_images/dead_venom.png')
            self.big_venom_image = pygame.transform.scale(self.dying_venom, (250, 150))
            self.big_venom_image_rect = self.big_venom_image.get_rect()
            self.big_venom_image_rect.center =  ((self.screen_rect.centerx/2)*3, self.y)

        elif self.stats.spidey_died:
            sound = pygame.mixer.Sound('songs/venom_speech.wav')
            sound.play(0)
            self.dying_spidey = pygame.image.load('images/dead_spidey.png')
            self.big_spidey_image = pygame.transform.scale(self.dying_spidey, (220,120))
            self.big_spidey_image_rect = self.big_spidey_image.get_rect()
            self.big_spidey_image_rect.center =  (self.screen_rect.centerx/2, self.y)

            self.win_venom = pygame.image.load('venom_images/mask_off_venom{}.png'.format(int(self.count%6)))
            self.big_venom_image = pygame.transform.scale(self.win_venom, (200,280))
            self.big_venom_image_rect = self.big_venom_image.get_rect()
            self.big_venom_image_rect.center = ((self.screen_rect.centerx/2)*3, self.y)

        self.count += 0.05

    def draw_button(self):

        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.msg1_image, self.msg1_image_rect)
        self.screen.blit(self.big_spidey_image, self.big_spidey_image_rect)
        self.screen.blit(self.big_venom_image, self.big_venom_image_rect)
