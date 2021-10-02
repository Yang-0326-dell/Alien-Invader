

import pygame.ftfont

class Scoreboard():

    def __init__(self, ai_settings, screen,stat, score):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.score = score
        self.ship_left=stat.ship_left
        self.text_color = (255,255,255) 
        self.font = pygame.font.SysFont(None, 48)
        self.level=stat.level
        self.prep_score()

    def prep_score(self):
        if self.ship_left==1:
            score_str = str(self.score)+'\nLevel: '+str(self.level) +' You have '+str(self.ship_left)+' ship left!'
        elif self.ship_left==2 or self.ship_left==3:
            score_str = str(self.score)+'\nYou have '+str(self.ship_left)+' ship left!'
        elif self.ship_left==0:
            score_str=str(self.score)+'Ooops, you have NO ship left!!!'
        self.score_image = self.font.render(score_str, True, self.text_color,self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def update(self,ds,stat):
        self.score+=ds
        if self.ship_left==1:
            score_str ='score: '+ str(self.score)+'  Level:'+str(stat.level) +'  You have '+str(stat.ship_left)+' ship left!'
        elif self.ship_left>=2:
            score_str = 'score: '+ str(self.score)+'  Level:'+str(stat.level) +'  You have '+str(stat.ship_left)+' ship left!'
        elif self.ship_left<=0:
            score_str='score: '+ str(self.score)+'  Level:'+str(stat.level) +'  Ooops, you have NO ship left!!!'
        self.score_image = self.font.render(score_str, True, self.text_color,self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        #print(self.score)
