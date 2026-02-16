import pygame
import numpy as np
import random

class Universe:
    def __init__(self):
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def update_all(self):
        for body in self.bodies:
            body.apply_gravity(self.bodies)
        for body in self.bodies:
            body.update()


class Body():
    def __init__(self,mass,pos,vel,color,radius):
        self.mass=mass
        self.pos=np.array(pos,dtype=np.float64)
        self.vel = np.array(vel, dtype=np.float64)
        self.acc = np.array([0,0], dtype=np.float64)
        self.color=color
        self.radius=radius

    def Gravity_Force(self,all_bodies):
        G = 0.1
        total_force = np.array([0.0, 0.0])
        for other_bodies in all_bodies:
            if other_bodies is self:
                continue
            else:
                dis_vec=other_bodies.pos-self.pos
                dis_mag=np.linalg.norm(dis_vec)+5
                f_dir=dis_vec/dis_mag
                grav_force=np.array(((G*self.mass*other_bodies.mass)/(dis_mag**2))*f_dir)
                total_force+=grav_force
        return total_force

    def apply_gravity(self, all_bodies):
        force_vector = self.Gravity_Force(all_bodies)
        self.acc = force_vector / self.mass


    def update(self):
        self.vel+=self.acc*dt
        self.pos+=self.vel*dt
        self.acc = np.array([0.0, 0.0])
    def Draw (self,window):
        pygame.draw.circle(window, self.color, self.pos.astype(int), self.radius)


COLORS = [
    (255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255),
    (255,0,255), (255,165,0), (128,0,128), (255,255,255), (255,192,203),
    (0,128,128), (128,128,0), (128,0,0), (0,128,0), (0,0,128),
    (255,99,71), (64,224,208), (255,215,0), (138,43,226), (255,20,147)]

Universe_1=Universe()
for i in range(0):
    mass = random.randint(500, 5000)
    pos_x = random.randint(50, 750)
    pos_y = random.randint(50, 750)
    vel_x = random.uniform(-5, 5)
    vel_y = random.uniform(-5, 5)
    color = random.choice(COLORS)
    radius = int(mass / 500) + 5
    Universe_1.add_body(Body(mass, (pos_x, pos_y), (vel_x, vel_y), color, radius))
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
ORANGE=(255,165,0)
PURPLE=(128,0,128)
WHITE=(255,255,255)

Universe_1.add_body(Body(50000,(400,400),(0,0),YELLOW,20))

Universe_1.add_body(Body(50,(400,300),(5,0),RED,5))
Universe_1.add_body(Body(50,(400,500),(-5,0),CYAN,5))


Universe_1.add_body(Body(100,(400,250),(4.08,0),BLUE,7))
Universe_1.add_body(Body(100,(400,550),(-4.08,0),MAGENTA,7))


Universe_1.add_body(Body(80,(400,200),(3.54,0),GREEN,6))
Universe_1.add_body(Body(80,(400,600),(-3.54,0),ORANGE,6))

Universe_1.add_body(Body(70,(527,400),(0,-3.73),PURPLE,6))
Universe_1.add_body(Body(70,(273,400),(0,3.73),WHITE,6))

pygame.init()
Height=800
Width=800
FPS=60
window=pygame.display.set_mode((Width,Height))
clock=pygame.time.Clock()
Running=True
window.fill((0,0,0))
dt=0.1
while Running:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Running=False
    for _ in range(5):
        Universe_1.update_all()
    for body in Universe_1.bodies:
        body.Draw(window)

    pygame.display.flip()
    clock.tick(FPS)
