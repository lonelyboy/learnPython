import math

def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle);
    ny = y + step*math.sin(angle);
    return nx,ny;

x,y =  move(100,100,1);
print(x,y);