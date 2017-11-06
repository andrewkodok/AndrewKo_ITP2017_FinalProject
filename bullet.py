import pygame
from pygame.sprite import Sprite

class Webshot_right(Sprite):

    def __init__(self, svv_settings, screen, spidey):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = svv_settings

        self.original_image = pygame.image.load('images/webshot.png')
        self.image = pygame.transform.scale(self.original_image , (8,8))
        self.rect = self.image.get_rect()
        self.rect.x = spidey.rect.right
        self.rect.y = spidey.rect.centery

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):

        self.x += 7
        self.rect.x = self.x

    def blitme(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)

class Webshot_left(Sprite):

    def __init__(self, svv_settings, screen, spidey):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = svv_settings

        self.original_image = pygame.image.load('images/webshot.png')
        self.image = pygame.transform.scale(self.original_image , (8,8))
        self.rect = self.image.get_rect()
        self.rect.x = spidey.rect.left
        self.rect.y = spidey.rect.centery

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):

        self.x -= 7
        self.rect.x = self.x

    def blitme(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)


class Venomshot_right(Sprite):

    def __init__(self, svv_settings, screen, venom):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = svv_settings

        self.original_image = pygame.image.load('venom_images/venom_bullet.png')
        self.image = pygame.transform.scale(self.original_image , (8,8))
        self.rect = self.image.get_rect()
        self.rect.x = venom.rect.right
        self.rect.y = venom.rect.centery

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):

        self.x += 7
        self.rect.x = self.x

    def blitme(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)

class Venomshot_left(Sprite):

    def __init__(self, svv_settings, screen, venom):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = svv_settings

        self.original_image = pygame.image.load('venom_images/venom_bullet.png')
        self.image = pygame.transform.scale(self.original_image , (8,8))
        self.rect = self.image.get_rect()
        self.rect.x = venom.rect.left
        self.rect.y = venom.rect.centery

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):

        self.x -= 7
        self.rect.x = self.x

    def blitme(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)


class Vomit_right(Sprite):

    def __init__(self, svv_settings, screen, venom):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = svv_settings

        self.original_image = pygame.image.load('venom_images/vomit.png')
        #self.image = pygame.transform.scale(self.original_image , (8,8))
        self.rect = self.original_image.get_rect()
        self.rect.x = venom.rect.right
        self.rect.y = venom.rect.centery-8

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):

        self.x += 12
        self.rect.x = self.x

    def blitme(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.original_image, self.rect)

class Vomit_left(Sprite):

    def __init__(self, svv_settings, screen, venom):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = svv_settings

        self.original_image = pygame.image.load('venom_images/vomit.png')
        self.flipped_image = pygame.transform.flip(self.original_image, True, False)
        #self.image = pygame.transform.scale(self.original_image , (8,8))
        self.rect = self.flipped_image.get_rect()
        self.rect.x = venom.rect.left
        self.rect.y = venom.rect.centery-8

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):

        self.x -= 12
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.flipped_image, self.rect)
