import pygame

class Ship():
    def __init__(self,screen,ai_settings):
        self.screen=screen
        self.height=ai_settings.ship_height
        self.width=ai_settings.ship_width
        self.image=pygame.image.load('images/ship1.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.time=0

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self,settings):
        if self.moving_right==True and self.rect.right<settings.screen_width:
            self.center+=settings.ship_speed
        
        if self.moving_left==True and self.rect.left>0:
            self.center-=settings.ship_speed
        
        self.rect.centerx=self.center

        if self.moving_up==True:
            self.bottom-=1

        if self.moving_down==True:
            self.bottom+=1

