class Settings():

    def __init__(self):
        self.screen_width = 700
        self.screen_height = 300
        self.bg_color = (255,255,255)

        self.spidey_limit = 5
        self.venom_limit = 5

        self.bullets_allowed = 2
        self.venom_bullets_allowed = 2
        self.vomit_bullets_allowed = 0

        self.start_dynamic_settings()

    def start_dynamic_settings(self):

        self.spidey_speed_factor = 3
        self.spidey_climb_sf = 1.5
        self.spidey_swing_sf = 5
        self.spidey_roll_sf = 6

        self.venom_speed_factor = 3
        self.venom_vanish_sf = 11
        self.venom_climb_sf = 1
