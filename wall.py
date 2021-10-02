import pygame

from pygame.sprite import Sprite

class Wall(Sprite):
    def __init__(self,screen,position,ai_settings):
        super(Wall,self).__init__()
        self.screen=screen
        self.color=ai_settings.wall_color
        self.rect=pygame.Rect(0,0,ai_settings.wall_width,ai_settings.wall_height)
        self.rect.top=0
        self.rect.centerx=0
        self.height=ai_settings.wall_height
        self.width=ai_settings.wall_width
        self.gap=ai_settings.wall_gap
        self.rect.x=(position[0]-1)*(self.width+self.gap)+self.width/2
        #print(position)
        self.rect.y=ai_settings.screen_height-(position[1]-1)*(self.height+self.gap)-150

    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        #print(self.rect)
        