from Engine.object_3d import *
from Engine.camera import *
from Engine.projection import *
import pygame as pg

class SoftwareRender:
    def __init__(self,file):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects(file)

    def create_objects(self,file):
        self.camera = Camera(self, [-5, 6, -55])
        self.projection = Projection(self)
        self.object = self.get_object_from_file(file)
        self.object.rotate_y(-math.pi / 4)

    def get_object_from_file(self, filename):
        vertex, faces = [], []
        try:
            with open(filename) as f:
                for line in f:
                    if line.startswith('v '):
                        vertex.append([float(i) for i in line.split()[1:]] + [1])
                    elif line.startswith('f'):
                        faces_ = line.split()[1:]
                        faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        except: print("\033[91mError: This file doesnt exist \033[0m"); exit(1)
        return Object3D(self, vertex, faces)

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        self.object.draw()

    def run(self):
        count = 0
        while True:
            if count == 0:
                print("\033[92mPress ctrl+c to end the engine or alt + F4\033[0m")
                count += 1
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

def start_engine(path : str | None=""):
    """Starting the module formatting aka engine"""
    if not path == "":
        if not ".obj" in path:
            path += ".obj"
        print(path)
        app = SoftwareRender(path)
        app.run()
    print("\n\033[94mWich .obj file should viewed in 3d Engine? \033[96m(assets/obj/roboter.obj)\033[0m")

    FileName = input("\033[95m"+r"Path to file -> "+"\033[0m")
    if not ".obj" in FileName:
        FileName += ".obj"
    print(FileName)
    app = SoftwareRender(FileName)
    app.run()

if __name__ == "__main__":
    start_engine()