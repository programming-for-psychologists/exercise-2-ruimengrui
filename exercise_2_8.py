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
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixation = visual.TextStim(win, text="+", height=40, color="white", pos=[0,0])
incorrectFeedback = visual.TextStim(win, text="X", height=40, color="red", pos=[0,0])

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

while True:		
	fixation.draw()
	win.flip()
	core.wait(0.5)
	win.flip()
	firstNameShown = random.choice(firstNames)
	firstNameStim.setText(firstNameShown)
	firstNameStim.draw()
	win.flip()
	if firstNameShown == userInput['Name']:
		corrctResp = ['space']
	else:
		corrctResp = None
	resp = event.waitKeys(maxWait = 3, keyList='space')
	if resp != corrctResp:
		incorrectFeedback.draw()
		win.flip()
		core.wait(1)
	if event.getKeys(['q']):
		break
