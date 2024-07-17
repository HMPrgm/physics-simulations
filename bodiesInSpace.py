import pygame
from difeqs import universalGravitation, kinematics

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

G = 1000
dt = .01


m1 = 10
x1 = (200,300)
v1 = (0,70.71)
r1 = 10
color1=(255,0,0)

m2 = 1000
x2=(400,300)
v2 = (0,0)
r2 = 10
color2 = (0,0,255)


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))




run = True
collision = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    if collision:
        continue
    screen.fill((0,0,0))




    pygame.draw.circle(screen,color1,x1, r1)
    pygame.draw.circle(screen,color2,x2, r2)
    
    #param: b1 = ((x1,y1),m1), b2 = ((x2,y2),m2),G=Gravitational Constant
    #returns: force = (fx,fy)
    a1 = universalGravitation((x1,m1),(x2,m2),G,returnsAcceleration=True)
    # print(a1)
    a2 = universalGravitation((x2,m2),(x1,m1),G,returnsAcceleration=True)
    # a2 = (0,0)
    #param: x = (x,y), v = (vx,vy), a = (ax,ay), dt = Δt
    #returns: (xf = (x,y), vf = (vx,vy))
    x1,v1 = kinematics(x1,v1,a1,dt)
    x2,v2 = kinematics(x2,v2,a2,dt)
    
    pygame.draw.line(screen,color1,(x1),(5*v1[0]+x1[0],5*v1[1]+x1[1]))
    pygame.draw.line(screen,color1,(x2),(5*v2[0]+x2[0],5*v2[1]+x2[1]))
    
    pygame.draw.line(screen,(255,255,0),(x1),(5*a1[0]+x1[0],5*a1[1]+x1[1]))
    pygame.draw.line(screen,(255,255,0),(x2),(5*a2[0]+x2[0],5*a2[1]+x2[1]))
    
    xDistance = abs(x2[0]-x1[0])
    yDistance = abs(x2[1]-x1[1])
    print (xDistance,yDistance)
    if (xDistance<(r1+r2)/2 and yDistance<(r1+r2)/2):
        print("COLLISION")
        collision = True
    x2 = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    

pygame.quit()