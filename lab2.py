import sys
import random
from gl import Render
from obj import Texture

def planeta():
    r = Render(600, 600)
    r.load('./esfera.obj', (3, 3, 0), (100, 100, 100))
    r.display('venus.bmp')

planeta()
