import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__ (self, screen,settings,ship,time):
        super(Bullet,self).__init__()
        self.width=settings.bullet_width
        self.height=settings.bullet_height
        self.screen=screen
        self.time=time
        self.fire=False
        self.rect=pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
        self.color=settings.bullet_color
        self.rect.top=ship.rect.top
        self.rect.centerx=ship.rect.centerx
        self.y=float(self.rect.y)
        self.speed_factor=settings.bullet_speed
        self.time1=0
        


    def update_bullet(self,ship):
        #print(self.rect.centerx)
        #print(self.rect.top)

        self.y-=self.speed_factor
        self.rect.y=self.y

        #print(self.rect.y)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)



