from pyglet.gl import *

class Triangle:
    def __init__(self):
        self.vertices=pyglet.graphics.vertex_list(3, ('v3f',[-0.5,-0.5,0.0,0.5,-0.5,0.0,0.0,0.5,0.0]),
                                                     ('c3B',[100,200,220,200,110,100,100,250,100]))

class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

if __name__ == "__main__":
    window = MyWindow(1280,720,"my Pyglet window", resizablw=True)
    pyglet.app.run()
