# Starter Event Controls

player = pygame.Rect((300,250,50,50))
speed = 1;

pygame.draw.rect(screen, (0,255,0), player)

key = pygame.key.get_pressed()
if key[pygame.K_d] == True:
    player.move_ip(1*speed,0)
if key[pygame.K_a] == True:
    player.move_ip(-1*speed,0)
if key[pygame.K_w] == True:
    player.move_ip(0,-1*speed)
if key[pygame.K_s] == True:
    player.move_ip(0,1*speed)

# Test Oscilation
xTest = (200,250)
vTest = (0,0)

    pygame.draw.circle(screen,(20,30,200), xTest,30)
    xTest,vTest = kinematics(xTest,vTest,(-(xTest[0]-(SCREEN_WIDTH/2))/10000,0),dt)