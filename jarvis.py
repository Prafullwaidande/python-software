import pyttsx3
import os

# pyttsx3.speak("Hey this is me jarves how can i help you")

while True:
	print("What should i do for you  : " , end='')
	p = input()

	# print(p)
	# os.system(p)

	if (("run" in p) or ("execute" in p ) or ("open" in p )) and (("chrome" in p) or ("google" in p)):
  		os.system("chrome")

	elif (("run" in p) or ("execute" in p ) or ("open" in p )) and (("notepad" in p) or ("editor" in p)) :
  		os.system("notepad")

	elif (("run" in p) or ("execute" in p ) or ("open" in p )) and (("drawing board" in p) or ("Paint" in p)) :
  		os.system("Paint")

	elif (("run" in p) or ("execute" in p ) or ("open" in p )) and (("alarm" in p) or ("time" in p)) :
  		os.system("clock")

	elif (("run" in p) or ("execute" in p ) or ("open" in p )) and ("discord" in p) :
  		os.system("discord")

	elif (("run" in p) or ("execute" in p ) or ("open" in p )) and ("calculator" in p) :
  		os.system("calculator")

	elif (("run" in p) or ("execute" in p ) or ("open" in p )) and ("camera" in p) :
  		os.system("camera")

	elif (("run" in p) or ("execute" in p ) or ("open" in p )) and ("map" in p) :
  		os.system("map")

	elif ("exit" in p) or ("quit" in p):
		break
	else:
  		print("dont support")