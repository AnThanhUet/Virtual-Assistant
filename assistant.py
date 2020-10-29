import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
voices = robot_mouth.getProperty('voices')
while True:
	with speech_recognition.Microphone() as mic:
		print("robot: I'm Listening")
		robot_ear.adjust_for_ambient_noise(mic)
		audio = robot_ear.listen(mic, timeout = 3, phrase_time_limit = 3)

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you == ""
	print("You: " + you)

	if you == "":
	    robot_branin = "I can't hear you, try again"
	elif "hello" in you:
	    robot_brain = "hello An Thanh"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		robot_brain = "Bye An Thanh"
		print("Robot: " + robot_brain)
		robot_mouth.setProperty('voice', voices[1].id)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
	    robot_brain = "I'm fine thank you and you"

	print("Robot: " + robot_brain)
	robot_mouth.setProperty('voice', voices[1].id)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
