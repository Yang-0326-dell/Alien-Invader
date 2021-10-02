import sys

import json

import pygame

import time

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

from wall import Wall

from bomb import Bomb

import draw_wall_pattern as dwp

import game_functions as gf

from pygame.sprite import Group

from score import Scoreboard

from game_stat import Stat

from button import Button

from ufo import Ufo

def run_game():
    stick1=time.time()
    pygame.init()
    score=0
    ai_settings=Settings()
    ai_settings.score=0
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #print(screen)
    pygame.display.set_caption("Space Invader")
    #bg_color=(230,230,230)
    play_button=Button(ai_settings,screen,'play',(200,50),ai_settings.button_color,ai_settings.text_color)
    ship=Ship(screen,ai_settings)
    bullet=Group()
    aliens=Group()
    walls=Group()
    bombs=Group()
    ufo=Ufo(screen,ai_settings,(0,0),stick1)
    for i in range(0,3):
        for j in  range(0,10): 
            alien=Alien(screen,ai_settings,(j*(ai_settings.screen_width*3/4-250)/10,i*(ai_settings.screen_height*1/3-80)/4+ai_settings.alien_distance),0)
            aliens.add(alien)
    #for i in range(0,int(ai_settings.screen_height/(ai_settings.wall_height+ai_settings.wall_gap)*2/5)):
        #for j in range(0,int(ai_settings.screen_width/(ai_settings.wall_width+ai_settings.wall_gap))):
            #wall=Wall(screen,(j,i),ai_settings)
            #walls.add(wall)
            #wall.draw()
    dwp.draw(walls,screen,ai_settings)
    stat=Stat()
    sb = Scoreboard(ai_settings,screen,stat,score)


    while True:
        an=0
        for alien in aliens:
            an+=1 
        if an==0:
            if stat.level>=17:
                stat.ship_left=3+2*(stat.level-16)
            else:
                stat.ship_left=3

        gf.check_events(ship,bullet,aliens,walls,bombs,ai_settings,screen,sb,play_button,stat)
        #print (stat.ship_left)
        if not stat.game_active:
            play_button.draw_button()
            pygame.display.flip()
        else:
            gf.update_screen(ai_settings,screen,ship,bullet,aliens,walls,bombs,sb,stat,play_button,ufo)
        
        if an==0:
            dwp.draw(walls,screen,ai_settings)
            for i in range(0,3):
                for j in  range(0,10): 
                    alien=Alien(screen,ai_settings,(j*(ai_settings.screen_width*3/4-250)/10,i*(ai_settings.screen_height*1/3-80)/4+ai_settings.screen_height/7),0)
                    aliens.add(alien)
            stat.level+=1
            ai_settings.bomb_speed_time=ai_settings.bomb_speed_time_stat/ai_settings.level_factor**(stat.level-1)
            ai_settings.alien_speed_time=ai_settings.alien_speed_time_stat/ai_settings.level_factor**(stat.level-1)
            ai_settings.ufo_speed_time=ai_settings.ufo_speed_time_stat/ai_settings.level_factor**(stat.level-1)
            ai_settings.bomb_gap=ai_settings.bomb_gap_stat/1.2**(stat.level-1)
            ai_settings.ship_speed_time=ai_settings.ship_speed_time_stat/2**(stat.level-1)
            ai_settings.bullet_speed_time=ai_settings.bullet_speed_time_stat/2**(stat.level-1)
        ai_settings.bomb_speed_time=ai_settings.bomb_speed_time_stat/ai_settings.level_factor**(stat.level-1)
        ai_settings.alien_speed_time=ai_settings.alien_speed_time_stat/ai_settings.level_factor**(stat.level-1)
        ai_settings.ufo_speed_time=ai_settings.ufo_speed_time_stat/ai_settings.level_factor**(stat.level-1)
        ai_settings.bomb_gap=ai_settings.bomb_gap_stat/1.2**(stat.level-1)
        ai_settings.ship_speed_time=ai_settings.ship_speed_time_stat/2**(stat.level-1)
        ai_settings.bullet_speed_time=ai_settings.bullet_speed_time_stat/2**(stat.level-1)

        if stat.ship_left==0:
            break

    
    while True:      
        print(1)  
        pygame.display.flip()
        game_over_button=Button(ai_settings,screen,'Game over! Your level is '+str(stat.level)+" , your score is "+str(sb.score),(1000,100),(255,255,255),(0,255,0 ))    
        game_over_button.draw_button()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_KP_ENTER:
                    sys.exit()
                
        
run_game()
