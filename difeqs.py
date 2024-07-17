import math
#Defines the law of universalGravitation
#param: b1 = ((x1,y1),m1), b2 = ((x2,y2),m2),G=Gravitational Constant
#returns: force = (fx,fy)

def universalGravitation(b1,b2,G,returnsAcceleration = False):
    GRAVITY_MAX = 1000
    distance = math.dist(b1[0],b2[0])
    xDistance = (b2[0][0]-b1[0][0])
    yDistance = (b2[0][1]-b1[0][1])
    forceMagnitude = G * (b1[1]*b2[1])/(distance**2)
    theta = math.atan2(yDistance,xDistance)
    force = (min(GRAVITY_MAX,forceMagnitude*math.cos(theta)),min(GRAVITY_MAX,forceMagnitude*math.sin(theta)))
    # force = (forceMagnitude*b2[0][0]-b1[0][0],forceMagnitude*b2[0][1]-b1[0][1])
    if not(returnsAcceleration):
        return force
    acceleration = (force[0]/b1[1],force[1]/b1[1])
    return acceleration

#Returns new position from old position and acceleration
#param: x = (x,y), v = (vx,vy), a = (ax,ay), dt = Δt
#returns: (xf = (x,y), vf = (vx,vy))
def kinematics(x,v,a,dt):
    vf = (v[0] + a[0] * dt,v[1] + a[1] * dt)
    xf = (x[0] + v[0]*dt + 0.5*a[0]*(dt**2),x[1] + v[1]*dt + 0.5*a[1]*(dt**2))
    return (xf,vf)
    