import pyttsx3
a = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
robot_brain = "hello Mr.dung"
robot_mouth = pyttsx3.init()
robot_mouth.setProperty('voice', a)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
