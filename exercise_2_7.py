import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units="pix")

def popupError(text):
	errorDlg = gui.Dlg(title="Error", pos=[200,400])
	errorDlg.addText('Error: '+text, color='red')
	errorDlg.show()

userInput = {'Name':'Enter first name'}

nameReceived = False

while not nameReceived:
	dlg = gui.DlgFromDict(userInput)
	if userInput['Name'] not in firstNames:
		popupError('Name does not exist')
	else:
		print userInput['Name']
		nameReceived = True
	if event.getKeys(['q']):
		break
