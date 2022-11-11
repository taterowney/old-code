#a library upon which to build game sprites in tkinter

import tkinter as tk

class sprite:
    def __init__(self, creator, position, **kwargs):
        self._create = creator
        self.draw = creator.draw
        self.positon = position
#       self.y_pos = position[1]
        self.canvas = creator.canvas
        self.hitbox = creator.get_hitbox()
    def render(self):
        self._create(self.position[0], self.position[1])


class graphic:
    def __init__(self, canvas, srcFile = None, srcString = None, doAlternateHitbox = None):
        self.canvas = canvas
        if srcFile != None and srcString == None:
            pass
        elif srcString != None and srcFile == None:
            self.srcString = srcString
        else:
            raise TypeError("You must specify a file or string to render this graphic!")
    def draw(self, x, y)
        for shape in self.srcString:
            self.poly_ids.append(self.canvas._create(shape["shape"], shape["coordinates"], shape["parameters"]))
