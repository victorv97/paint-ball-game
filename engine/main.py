import sys
import pygame as pg
import moderngl as mgl

from camera import Camera
from player import Player
from light import Light
from mesh import Mesh
from scene import Scene


class Engine:
    def __init__(self, win_size=(800, 600)) -> None:
        pg.init()
        
        self.WIN_SIZE = win_size
        
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST)
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # light
        self.light = Light()
        # camera
        self.camera = Player(self)  #Camera(self)
        # mesh
        self.mesh = Mesh(self)
        # scene
        self.scene = Scene(self)
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()
            self.camera.handle_event(event)
    
    def render(self):
        self.ctx.clear(color=(0.64, 0.898, 0.92))
        
        self.scene.render()

        pg.display.flip()
        
    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def update_fps(self):
        print('fps: ', int(self.clock.get_fps()), end='\r')

    def run(self):
        while True:
            self.get_time()
            self.update_fps()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)


if __name__ == '__main__':
    app = Engine()
    app.run()


