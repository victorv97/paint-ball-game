from model import Cube
from ball import BallAttached
from random import randint
from settings import SCENE_WIDTH, SCENE_DEPTH, GROUND_HEIGHT


class Scene:
    def __init__(self, app) -> None:
        self.app = app
        self.objects = []
        self.map = set()
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)
    
    def remove_object(self, obj):
        self.objects.remove(obj)
    
    def load(self):
        self.generate(self.app)

    def generate(self, app):
        s = 2
        numbers = [4, 5, 6]
        for x in range(-SCENE_WIDTH + 1, SCENE_WIDTH, s):
            for z in range(-SCENE_DEPTH + 1, SCENE_DEPTH, s):
                if randint(1, 10) in numbers and (x, z) != (0, 0):
                    position = (x, GROUND_HEIGHT + 2, z)
                    self.add_object(Cube(app, pos=position, scale=(1, 2, 1), texture_id=2))
                    self.map.add((position[0], position[2]))  # store x, z
        self.add_object(BallAttached(app, texture_id=3))
        self.add_object(Cube(app, pos=(0, GROUND_HEIGHT, 0), scale=(SCENE_WIDTH, 0.2, SCENE_DEPTH), texture_id=1))
    
    def render(self):
        for obj in self.objects:
            obj.render()