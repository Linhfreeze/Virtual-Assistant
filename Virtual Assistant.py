import speech_recognition
import pyttsx3
from datetime import date, datetime
import time

robot_brain = ""
robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()

while True:
	with speech_recognition.Microphone() as mic:
		intro = "Hello Linh. Can I help you?"
		print("Rob: " + intro)
		robot_mouth.say(intro)
		robot_mouth.runAndWait()
		audio = robot_ear.listen(mic)
	print(".....")
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("Me: " + you)

	if you == "":
		robot_brain = "I can't hear you, try again"
	elif "hello" in you:
		robot_brain = "Hello Linh"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		t = time.localtime()
		robot_brain = time.strftime("%H:%M:%S", t)
	elif "bye" in you:
		robot_brain = "Bye Linh"
		print("Rob: " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "I don't know"

	print("Rob: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()