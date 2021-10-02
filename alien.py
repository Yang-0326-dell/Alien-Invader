import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,screen,ai_settings,original,stick):
        super(Alien,self).__init__()
        self.screen=screen
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=pygame.Rect(0,0,original[0],original[1])
        self.rect.left=original[0]
        self.rect.top=original[1]
        self.originalx=original[0]
        self.originaly=original[1]
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.moving_right=True
        self.speed_factor=ai_settings.alien_speed
        self.stick=stick
        self.bomb_gap=ai_settings.bomb_gap
        self.bomb_time=0
        self.width=ai_settings.alien_width
        self.height=ai_settings.alien_height
        self.collide_times=0

    def update(self):
        if self.moving_right==True:
            self.x+=self.speed_factor
        else:
            self.x-=self.speed_factor  
        self.rect.x=self.x   

    def update_dist(self,dh):
        self.y-=dh
        self.rect.y=self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)