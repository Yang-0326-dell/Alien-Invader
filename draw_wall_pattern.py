import json

from wall import Wall

def draw(walls,screen,ai_settings):
    alphaform='abcdefghijklmnopqrstuvwxyz!'
    list=[]
    data=[]
    wdata=[]
    wno=0
    for str in ai_settings.wall_pattern:
        i=0
        for alp in alphaform:
            if str==alp:
                list.append(i)
                break
            i+=1
    with open('wall_pattern.json') as file:
        data=json.load(file)
    for i in list:
        wdata.append(data[i])
    for tmp1 in wdata:
        raw=0
        for tmp2 in tmp1:
            for tmp3 in tmp2:
                if(raw>=10):
                    break
                wall=Wall(screen,(tmp3+wno*10,raw),ai_settings)
                walls.add(wall)
            raw+=1
                
        wno+=1
    return wdata
    
