from model import Cube, Tail
from random import randint

SCENE_WIDTH = 20
SCENE_DEPTH = 20


class Scene:
    def __init__(self, app) -> None:
        self.app = app
        self.objects = []
        self.map = set()
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)
    
    def load(self):
        self.generate(self.app)

    def generate(self, app):
        s = 2
        numbers = [4, 5, 6]
        for x in range(-SCENE_WIDTH + 1, SCENE_WIDTH, s):
            for z in range(-SCENE_DEPTH + 1, SCENE_DEPTH, s):
                if randint(1, 10) in numbers and (x, z) != (0, 0):
                    position = (x, -s, z)
                    self.add_object(Cube(app, pos=position, scale=(1, 2, 1), texture_id=2))
                    self.map.add((position[0], position[2]))  # store x, z
        self.add_object(Cube(app, pos=(0, -s*2.01, 0), scale=(SCENE_WIDTH, 0.2, SCENE_DEPTH), rot=(0, 0, 0), texture_id=1))
    
    def render(self):
        for obj in self.objects:
            obj.render()