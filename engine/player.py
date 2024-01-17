import glm
import pygame as pg
from camera import Camera

SPEED = 0.008
GRAVITY = 0.0008
HEIGHT_INIT = -2

class Player(Camera):
    def __init__(self, app, position=(0, HEIGHT_INIT, 0), yaw=-90, pitch=0) -> None:
        super().__init__(app, position, yaw, pitch)
        self.on_ground = True
        self.vertical_velocity = 0
    
    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.move_forward(velocity)
        if keys[pg.K_s]:
            self.move_backward(velocity)
        if keys[pg.K_d]:
            self.move_right(velocity)
        if keys[pg.K_a]:
            self.move_left(velocity)

        if self.on_ground and keys[pg.K_SPACE]:
            self.on_ground = False
            self.vertical_velocity = velocity
        
        if not self.on_ground:
            self.position.y += self.up.y * self.vertical_velocity
            self.vertical_velocity -= GRAVITY * self.app.delta_time
        
        if self.position.y < HEIGHT_INIT:
            self.position.y = HEIGHT_INIT
            self.on_ground = True
    
    def move_forward(self, velocity):
        self.position.x += self.forward.x * velocity
        self.position.z += self.forward.z * velocity

    def move_backward(self, velocity):
        self.position.x -= self.forward.x * velocity
        self.position.z -= self.forward.z * velocity

    def move_right(self, velocity):
        self.position.x += self.right.x * velocity
        self.position.z += self.right.z * velocity

    def move_left(self, velocity):
        self.position.x -= self.right.x * velocity
        self.position.z -= self.right.z * velocity
