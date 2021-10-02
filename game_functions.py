import sys

import pygame

from bullet import Bullet

from pygame.sprite import Group

from bomb import Bomb

import score as s

import time

import random

def check_keydown(event,settings,screen,ship,bullet):
    sticks=time.time()
    if sticks-settings.ship_speed_time>=ship.time:   
        ship.time=sticks
        if event.key==pygame.K_RIGHT:
            ship.moving_right=True
        if event.key==pygame.K_LEFT:
            ship.moving_left=True
            
    stick_list=[0]
    for bu in bullet:
        stick_list.insert(0,bu.time)
            
    if event.key==pygame.K_SPACE:
        #print(stick_list)
        if stick_list[0]<=sticks-settings.bullet_number or stick_list[0]==0:
            new_bullet=Bullet(screen,settings,ship,sticks)
            bullet.add(new_bullet)
                 

def check_keyup(event,ship):
            if event.key==pygame.K_RIGHT:
                ship.moving_right=False
            if event.key==pygame.K_LEFT:
                ship.moving_left=False

def check_play_button(play_button,mouse_x,mouse_y,stat):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stat.game_active=True

def check_events(ship,bullet,aliens,walls,bombs,ai_settings,screen,sb,play_button,stat):
    #print(ship.rect.centerx)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown(event,ai_settings,screen,ship,bullet)  
        elif event.type==pygame.KEYUP:
            check_keyup(event,ship)  
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(play_button,mouse_x,mouse_y,stat)
            
    for every_bullet in bullet:
        for alien in aliens:
            dx=(ai_settings.bullet_width+ai_settings.alien_width)/2
            dy=(ai_settings.bullet_height+ai_settings.alien_height)/2
            if every_bullet.rect.y-alien.rect.y<alien.height and alien.rect.y-every_bullet.rect.y<every_bullet.height and every_bullet.rect.x-alien.rect.x<alien.width and alien.rect.x-every_bullet.rect.x<every_bullet.width:
                aliens.remove(alien)
                bullet.remove(every_bullet)
                sb.update(ai_settings.score_alien,stat)

        for wall in walls:
            if every_bullet.rect.x-wall.rect.x<wall.width and wall.rect.x-every_bullet.rect.x<every_bullet.width and wall.rect.y-every_bullet.y<every_bullet.height and every_bullet.rect.y-wall.rect.y<wall.height:
                walls.remove(wall)
                bullet.remove(every_bullet)
    alien_number=0
    for alien in aliens:
        alien_number+=1 
    if alien_number>0:
        bomb_time=alien.bomb_time
    bomb_list=[]
    sticks=time.time()
    
    bn=random.randint(0,ai_settings.bomb_number)
    if alien_number!=0 and sticks-ai_settings.bomb_gap>bomb_time and len(bomb_list)<=bn:
        alien.bomb_time=sticks
        an=0
        for i in range(0,bn):
            if alien_number>0:
                an=random.randint(0,alien_number)
            if an not in bomb_list:
                bomb_list.append(an)
    i=0
    for alien in aliens:
        if i in bomb_list:
            bomb=Bomb(screen,(alien.rect.x,alien.rect.y),ai_settings)
            bombs.add(bomb)
        i+=1
        

def update_screen(ai_settings,screen,ship,bullet,aliens,walls,bombs,sb,stat,play_button,ufo):
    stick=time.time()

    for bu in bullet:
        if stick-ai_settings.bullet_speed_time>bu.time1:
            bu.update_bullet(ship)
            #print(bu.rect.y)
            bu.draw_bullet()
            bu.time1=stick
        if bu.rect.y<0:
            bullet.remove(bu)
        if bu.rect.x-ufo.rect.x<ai_settings.ufo_width and ufo.rect.x-bu.rect.x<ai_settings.bullet_width and bu.rect.y-ufo.rect.y<ai_settings.ufo_height and ufo.rect.y-bu.rect.y<ai_settings.bullet_height :
            ufo.x=-ai_settings.ufo_width
            
            ufo.appear=False
            sb.update(ai_settings.score_ufo,stat)
            bullet.remove(bu)
            ufo.time1=stick
    if ufo.rect.x>ai_settings.screen_width:
        ufo.x=-ai_settings.ufo_width
        ufo.appear=False
        ufo.time1=stick

    for bomb in bombs:
        for wall in walls:
            if bomb.rect.x-wall.rect.x<wall.width and wall.rect.x-bomb.rect.x<bomb.width and bomb.rect.y-wall.rect.y<wall.height and wall.rect.y-bomb.rect.y<bomb.height:
                if bomb.col==1:
                    #collisions1 = pygame.sprite.groupcollide(bombs, walls, True, True)
                    bombs.remove(bomb)
                else:
                    bomb.col+=1
                walls.remove(wall)
        for bu in bullet:
            dx=(ai_settings.bomb_width+ai_settings.bullet_width)/2
            dy=(ai_settings.bomb_height+ai_settings.bullet_height)/2
            if bu.rect.x-bomb.rect.x<bomb.width and bomb.rect.x-bu.rect.x<bu.width and bu.rect.y-bomb.rect.y<bomb.height and bomb.rect.y-bu.rect.y<bu.height:
                bullet.remove(bu)
                bombs.remove(bomb) 
        if bomb.rect.x-ship.rect.x<ship.width and ship.rect.x-bomb.rect.x<bomb.width and bomb.rect.y-ship.rect.y<ship.height and ship.rect.y-bomb.rect.y<bomb.height:
            stat.ship_left-=1
            sb.ship_left=stat.ship_left
            ship.rect.centerx=ai_settings.screen_width/2
            bombs.remove(bomb)
            sb.update(ai_settings.punish,stat)
        if bomb.rect.y>ai_settings.screen_height:
            bombs.remove(bomb)

    if stick-ai_settings.ufo_gap>ufo.time1:
        ufo.appear=True
    #print(ufo.appear)
    #print(stick)
    #print(ufo.time1)
    ship.update(ai_settings)
    for bomb in bombs:
        if stick-ai_settings.bomb_speed_time>bomb.time:
            bomb.time=stick
            bomb.update()
    screen.fill(ai_settings.bg_color)

    ship.blitme()
    for bu in bullet.sprites():
        if stick-ai_settings.bullet_speed_time>bu.time:
            bu.draw_bullet()
    aliens_state=0
    for alien in aliens.sprites():
        #print(alien.stick)

        if alien.stick<=stick-ai_settings.alien_speed_time or alien.stick==0:
            alien.update()
            alien.stick=stick
        if alien.rect.x>=ai_settings.screen_width-ai_settings.alien_width-2:
            #for a in aliens:
                #a.moving_right=False
                aliens_state=1
        elif alien.rect.x<10:
            #for a in aliens:
                #a.moving_right=True
                aliens_state=-1
    for alien in aliens:
        if aliens_state==1:
            alien.moving_right=False
        elif aliens_state==-1:
            alien.moving_right=True
        alien.blitme()
    if stick-ai_settings.ufo_speed_time>ufo.time:
        ufo.update(ai_settings)
        ufo.time=stick
    ufo.blitme()
    
    for wall in walls:
        wall.draw()
    for bomb in bombs:
        bomb.draw()
    
    sb.show_score()
    pygame.display.flip()