# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import pyglet
import time
from pyglet import shapes

#rendering

width = 500
height = 200

cell_size = 10

window = pyglet.window.Window(width=width,height=height)

batch = pyglet.graphics.Batch()

clk = pyglet.clock.get_default()

t0 = time.time()

label = pyglet.text.Label('time:'+"{:.3f}".format(time.time()-t0),
                      font_name='Times New Roman',
                      font_size=10,
                      x=2, y=2,
                      anchor_x='left', anchor_y='bottom')

'''#Meshing

meshgrid = np.empty((int(width/cell_size), int(height/cell_size)), dtype=dict)
for i in range(int(width/cell_size)):
    for j in range(int(height/cell_size)):
        meshgrid[i][j] = {
            "density" : 1,
            "V" : (0,0),
            "P" : 1,
            "pos" : (i,j)
            "faces" : [
                {"x1"}
                ]
            }

meshgrid[1][1]["V"]=(10,0)'''

x_size = (int(width/cell_size))

x = np.empty(x_size+1)
for i in range(x_size+1):
    x[i] = (i+0.5) * cell_size
    
xb = np.empty(x_size+2)
for i in range(x_size+2):
    xb[i] = i * cell_size
    
y_size = (int(height/cell_size))

y = np.empty(y_size+1)
for i in range(y_size+1):
    y[i] = (i+0.5) * cell_size
    
yb = np.empty(y_size+2)
for i in range(y_size+2):
    yb[i] = (i) * cell_size
    
u = np.zeros((x_size, y_size), dtype=float)
v = np.zeros((x_size, y_size), dtype=float)

#simulation
t = 0
dt = 0.05

up = np.zeros((x_size, y_size), dtype=float)
vp = np.zeros((x_size, y_size), dtype=float)


def update(dt):
    label.text = 'time:'+"{:.3f}".format(time.time()-t0)
    for i in range(1,x_size):
        for j in range(1,y_size):
            
            d2udx2 = (u[i-1][j]-2*u[i][j]+u[i+1][j])/cell_size/cell_size
            d2udy2 = (u[i][j-1]-2*u[i][j]+u[i][j+1])/cell_size/cell_size
            ududx = u[i][j]*(u[i+1][j]-u[i-1][j])/(2*cell_size)
            vdudy = v[i][j]*(u[i][j+1]-u[i][j-1])/(2*cell_size)
            
            
            #vel = meshgrid[i][j]["V"]

    
pyglet.clock.schedule_interval(update, dt)



@window.event
def on_draw():
    window.clear()
    
    label.draw()
    
pyglet.app.run()