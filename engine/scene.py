from model import Cube


class Scene:
    def __init__(self, app) -> None:
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)
    
    def load(self):
        app = self.app
        add = self.add_object

        n, s = 50, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z), scale=(1, 0.2, 1)))
        
    
    def render(self):
        for obj in self.objects:
            obj.render()