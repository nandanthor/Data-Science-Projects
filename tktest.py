# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:39:26 2016

@author: nandanthor
"""

import tkinter as tk
import time

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# canvas.create_rectangle(x0, y0, x1, y1, option, ... )
# x0, y0, x1, y1 are corner coordinates of ulc to lrc diagonal
rc1 = canvas.create_rectangle(-800, 0, 0, 20, outline='white', fill='black')
circ = canvas.create_oval(280, 280, 320, 320, fill = 'yellow')

x = 5
y=0

for loops in range(125):
    
    canvas.move(rc1, x, y)
    time.sleep(0.1)
    canvas.grid()
    #canvas.move(rc2, x, y)
    canvas.update()

canvas.delete(rc1)
rc2 = canvas.create_rectangle(-800, 30, 0, 50, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc2, x, y)
    canvas.update()
  
canvas.delete(rc2)
rc3 = canvas.create_rectangle(-800, 60, 0, 80, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc3, x, y)
    canvas.update()
  
canvas.delete(rc3)

rc4 = canvas.create_rectangle(-800, 90, 0, 110, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc4, x, y)
    canvas.update()
  
canvas.delete(rc4)

rc5 = canvas.create_rectangle(-800, 120, 0, 140, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc5, x, y)
    canvas.update()
  
canvas.delete(rc5)

rc6 = canvas.create_rectangle(-800, 150, 0, 170, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc6, x, y)
    canvas.update()
  
canvas.delete(rc6)

rc7 = canvas.create_rectangle(-800, 180, 0, 200, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 210, 0, 230, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 240, 0, 260, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 270, 0, 290, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 300, 0, 320, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  

canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 330, 0, 350, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 360, 0, 380, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 390, 0, 410, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 420, 0, 440, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 450, 0, 470, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 480, 0, 500, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 510, 0, 530, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 540, 0, 560, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

rc7 = canvas.create_rectangle(-800, 570, 0, 590, outline='white', fill='black')

for loops in range(125):
    time.sleep(0.1)
    #canvas.move(rc1, x, y)
    canvas.move(rc7, x, y)
    canvas.update()
  
canvas.delete(rc7)

root.mainloop()
