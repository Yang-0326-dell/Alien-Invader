class Settings():

    def __init__ (self):
        self.level_factor=1.2
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(20,25,30)
        self.wall_pattern='junrtql!zzsgn!junrtql!zzsgn!'
        self.ship_height=54
        self.ship_width=100
        self.ship_speed=1
        self.ship_speed_time=0.06
        self.bullet_speed=6
        self.bullet_speed_time=0.01
        self.bullet_width=4
        self.bullet_height=12
        self.bullet_color=(255,60,60)
        self.bullet_number=0.5
        self.alien_speed=10
        self.alien_speed_time=0.1
        self.wall_color=(60,60,255)
        self.wall_height=30
        self.wall_width=5
        self.wall_gap=1
        self.alien_width=30
        self.alien_height=30
        self.alien_distance=self.screen_height/7
        self.bomb_width=6
        self.bomb_height=15
        self.bomb_color=(255,255,255)
        self.bomb_speed=10
        self.bomb_speed_time=0.1
        self.bomb_gap=0.7
        self.bomb_number=1
        self.ufo_width=263
        self.ufo_height=82
        self.ufo_speed=15
        self.ufo_speed_time=0.1
        self.ufo_gap=10
        self.score_alien=20
        self.score_ufo=100
        self.punish=-50
        self.score=0
        self.button_color=(0,255,255)
        self.text_color=(255,255,255)
        self.bomb_speed_time_stat=0.1
        self.alien_speed_time_stat=0.1
        self.ufo_speed_time_stat=0.1
        self.bomb_gap_stat=0.7
        self.alien_distance_stat=self.screen_height/7
        self.ship_speed_time_stat=0.06
        self.bullet_speed_time_stat=0.01
        
