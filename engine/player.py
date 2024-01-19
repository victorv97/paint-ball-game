import glm
import pygame as pg
from camera import Camera
from ball import Ball

SPEED = 0.006
GRAVITY = 0.0002
HEIGHT_INIT = -2

class Player(Camera):
    def __init__(self, app, position=(0, HEIGHT_INIT, 0), yaw=-90, pitch=0) -> None:
        super().__init__(app, position, yaw, pitch)
        self.on_ground = True
        self.vertical_velocity = 0
    
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            ball_pos = (self.position + self.forward*1.5).to_tuple()
            self.app.scene.add_object(Ball(self.app, pos=ball_pos))
    
    def move(self):
        velocity = SPEED * self.app.delta_time
        next_step = glm.vec2() 
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            next_step = self.move_forward(velocity)
        if keys[pg.K_s]:
            next_step = self.move_backward(velocity)
        if keys[pg.K_d]:
            next_step = self.move_right(velocity)
        if keys[pg.K_a]:
            next_step = self.move_left(velocity)

        if self.on_ground and keys[pg.K_SPACE]:
            self.on_ground = False
            self.vertical_velocity = velocity
        
        if not self.on_ground:
            self.position.y += self.up.y * self.vertical_velocity
            self.vertical_velocity -= GRAVITY * self.app.delta_time
        
        if self.position.y < HEIGHT_INIT:
            self.position.y = HEIGHT_INIT
            self.on_ground = True
        
        self.make_step(next_step)
    
    def make_step(self, next_step):
        if not self.check_collision(d_x=next_step[0]):
            self.position.x += next_step[0]

        if not self.check_collision(d_z=next_step[1]):
            self.position.z += next_step[1]
    
    def move_forward(self, velocity):
        return self.forward.xz * velocity

    def move_backward(self, velocity):
        return -self.forward.xz * velocity

    def move_right(self, velocity):
        return self.right.xz * velocity

    def move_left(self, velocity):
        return -self.right.xz * velocity

    def check_collision(self, d_x=0, d_z=0):
        pos_x = (self.position.x + d_x + (1.5 if d_x > 0 else -1.5 if d_x < 0 else 0))
        pos_z = (self.position.z + d_z + (1.5 if d_z > 0 else -1.5 if d_z < 0 else 0))
        for obj in self.app.scene.map:
            if glm.sqrt((pos_x - obj[0])**2 + (pos_z - obj[1])**2) <= 1.01:
                return True
        return False
