import pygame

class Ufo():
    def __init__(self,screen,ai_settings,pos,time):
        self.width=ai_settings.ufo_width
        self.height=ai_settings.ufo_height
        self.screen=screen

        self.image=pygame.image.load('images/ufo.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.x=-ai_settings.ufo_width
        self.rect.y=0
        self.x=float(self.rect.x)
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.appear=False
        self.time1=time
        self.time=time
        
    def blitme(self):
        if self.appear==False:
            self.rect.x=-self.screen_rect.width
            self.x=float(self.rect.x)
        self.screen.blit(self.image,self.rect)

    def update(self,settings):
        self.x+=settings.ufo_speed 
        self.rect.x=self.x
