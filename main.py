import pygame
from difeqs import universalGravitation, kinematics

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

G = 100
dt = .1


m1 = 10
x1 = (100,500)
v1 = (7,0)
r1 = 10
color1=(255,0,0)

m2 = 200
x2=(400,300)
v2 = (0,0)
r2 = 10
color2 = (0,0,255)


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))




run = True
while run:

    screen.fill((0,0,0))




    pygame.draw.circle(screen,color1,x1, r1)
    pygame.draw.circle(screen,color2,x2, r2)
    
    #param: b1 = ((x1,y1),m1), b2 = ((x2,y2),m2),G=Gravitational Constant
    #returns: force = (fx,fy)
    a1 = universalGravitation(b1=(x1,m1),b2=(x2,m2),G=G,returnsAcceleration=True)
    # print(a1)
    a2 = universalGravitation((x2,m2),(x1,m1),G,returnsAcceleration=True)
    # a2 = (0,0)
    #param: x = (x,y), v = (vx,vy), a = (ax,ay), dt = Δt
    #returns: (xf = (x,y), vf = (vx,vy))
    x1,v1 = kinematics(x1,v1,a1,dt)
    x2,v2 = kinematics(x2,v2,a2,dt)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()