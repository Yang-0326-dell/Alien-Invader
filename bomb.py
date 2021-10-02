import pygame

from pygame.sprite import Sprite

class Bomb(Sprite):
    def __init__(self,screen,alien_posi,ai_settings):
        super(Bomb,self).__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,ai_settings.bomb_width,ai_settings.bomb_height)
        self.color=ai_settings.bomb_color
        self.rect.x=alien_posi[0]
        self.rect.y=alien_posi[1]
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.width=ai_settings.bomb_width
        self.height=ai_settings.bomb_height
        self.speed=ai_settings.bomb_speed
        self.time=0
        self.col=0

    def update(self):
        self.y+=self.speed
        self.rect.y=self.y
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        