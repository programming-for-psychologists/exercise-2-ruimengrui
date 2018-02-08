import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
lastNames = [name.split(' ')[1] for name in names]

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units="pix")
lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixation = visual.TextStim(win, text="+", height=40, color="white", pos=[0,0])

while True:
	fixation.draw()
	win.flip()
	core.wait(0.5)
	win.flip()
    	nameShown = random.choice(lastNames)
    	lastNameStim.setText(nameShown)
    	lastNameStim.draw()
    	win.flip()
    	core.wait(.75)
    	win.flip()
    	core.wait(.15)

    	if event.getKeys(['q']):
       		 break
