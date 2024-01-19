import glm
from model import BaseModel

SPEED = 0.1
GRAVITY = 0.0002

class Ball(BaseModel):
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
        if self.pos.y <= -3:
            self.velocity = glm.vec3(0, 0, 0)
        else:
            self.pos += self.velocity * self.dt
            self.velocity.y -= GRAVITY * self.dt

        self.m_model = self.get_model_matrix()
    
    def update(self):
        self.dt = self.app.delta_time
        self.texture.use()
        self.program['m_model'].write(self.m_model)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['camPos'].write(self.app.camera.position)
        self.make_step()

    def on_init(self):
        self.velocity = self.get_velocity_vector()
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)
        # texture
        self.program['u_texture_0'] = 0
        self.texture.use()
        # matrixes
        self.program['m_proj'].write(self.app.camera.m_proj)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['m_model'].write(self.m_model)