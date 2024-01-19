import glm
from model import ExtendedBase

SPEED = 0.08
GRAVITY = 0.0001


class BallAttached(ExtendedBase):
    def __init__(self, app, vao_name='ball', texture_id=3, pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.005, 0.005, 0.005)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
        self.texture = self.app.mesh.texture.textures[self.texture_id]
        self.on_init()

    def make_step(self):
        reletive_pos = self.app.camera.forward*0.2 + self.app.camera.right*0.08 - self.app.camera.up*0.05
        self.pos = self.app.camera.position + reletive_pos
        self.m_model = self.get_model_matrix()
    
    def update(self):
        self.make_step()
        super().update()


class Ball(ExtendedBase):
    def __init__(self, app, vao_name='ball', texture_id=3, pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.05, 0.05, 0.05)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
        self.texture = self.app.mesh.texture.textures[self.texture_id]
        self.dt = self.app.delta_time
        self.on_init()

    def get_velocity_vector(self):
        yaw, pitch = glm.radians(self.app.camera.yaw), glm.radians(self.app.camera.pitch)
        vel = SPEED * glm.vec3(
            glm.cos(pitch) * glm.cos(yaw),
            glm.sin(pitch),
            glm.cos(pitch) * glm.sin(yaw)  
        )
        return vel

    def make_step(self):
        if self.pos.y <= -4:
            self.velocity = glm.vec3(0, 0, 0)
            self.destroy()
        else:
            self.pos += self.velocity * self.dt
            self.velocity.y -= GRAVITY * self.dt

        self.m_model = self.get_model_matrix()
    
    def update(self):
        self.dt = self.app.delta_time
        self.make_step()
        super().update()

    def on_init(self):
        super().on_init()
        self.velocity = self.get_velocity_vector()

    def destroy(self):
        self.app.scene.remove_object(self)