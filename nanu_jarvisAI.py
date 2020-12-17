import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import pywhatkit as kit
# from twilio.rest import Client


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wish_me():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		speak('Good Morning sir')
	elif hour >= 12 and hour < 18:
		speak('Good Afternoon sir')
	else:
		speak('Good Evening sir')

	speak('I am Jarvis, an AI system,  made by kaushik gaur, how may i help you')

def takecommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n" )
	except Exception as e:
		print(e)
		speak("Say that again Please...")
		print("Say that again Please...")
		return "NONE"
	return query


def send_email(to, content):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.login("sender email id @gmail.com", "sender email id password") 
	server.sendmail("sender email id @gmail.com", to, content)
	server.close()

def send_sms(body, from_, to):
	account_sid = 'AC193b3a646397baad6fcc8ac3d413e34f'
	auth_token = '16d292460468586e5226781269cb8553'
	client = Client(account_sid, auth_token)

if __name__ == '__main__':
	speak('hello sir, how are you')
	wish_me()

	while True:
	# if 1:
		query = takecommand().lower()
		if 'exit the program' in query:
			speak('exiting the program and thank you for using me')
			break
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace('wikipedia', "")
			results = wikipedia.summary(query, sentences=2)
			speak("According to Wikipedia")
			print(results)
			speak(results)
		elif 'search on youtube' in query:
			speak('Sir, what should i search on youtube')
			ytm = takecommand().lower()
			kit.playonyt(ytm)
		elif 'open google' in query:
			speak('Sir, what should i search on google')
			gm = takecommand().lower()
			webbrowser.open(f"{gm}")
		elif 'open instagram' in query:
			webbrowser.open("instagram.com")
		elif 'open stack overflow' in query:
			webbrowser.open("stackoverflow.com")
		elif 'open facebook' in query:
			webbrowser.open("facebook.com")
		elif 'open wikipedia website' in query:
			webbrowser.open('wikipedia.com')
		elif 'open hackerrank' in query:
			webbrowser.open('hackerrank.com')
		elif 'open github' in query:
			webbrowser.open('www.github.com')
		elif 'open youtube' in query:
			webbrowser.open('youtube.com')
		elif 'open gmail' in query:
			webbrowser.open('gmail.com')

		elif 'play music' in query:
			music_dir = "C:\\Users\\amit sharma\\AppData\\Local\\Programs\\Python\\Python38-32\\song"
			songs = os.listdir(music_dir)
			md = random.choice(songs)
			os.startfile(os.path.join(music_dir, md))

		elif 'the time' in query:
			strtime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir the time is {strtime}")

		elif 'open pycharm' in query:
			path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.1.6\\bin\\pycharm.exe"
			os.startfile(path)

		elif 'show photos' in query:
			photo_dir = "B:\\amit\\4k wall"
			photos = os.listdir(photo_dir)
			pd = random.choice(photos)
			os.startfile(os.path.join(photo_dir, pd))


		elif 'open code' in query:
			code_path = "C:\\Users\\amit sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
			os.startfile(code_path)

		elif 'open total overdose' in query:
			tod_path = "C:\\Users\\amit sharma\\Downloads\\Total-Overdose_www.FreeGamesLand.net\\Total-Overdose_www.FreeGamesLand.net"
			os.startfile(tod_path)

		elif 'open notepad' in query:
			not_path = "C:\\Windows\\system32\\notepad.exe"
			os.startfile(not_path)

		elif 'open calculator' in query:
			cal_path = "C:\\Windows\\system32\\calc.exe"
			os.startfile(cal_path)

		elif 'can you do' in query:
			speak('i can send email, open social media, open any software, play songs, show photos and many more')

		elif 'send email' in query:
			try:
				speak("What should you want to say")
				content = takecommand()
				to = "receiver email id @gmail.com"
				send_email(to, content)
				speak("Email has been sent!")
				print("Email has been sent!")
			except Exception as e:
				print(e)
				speak('Sorry error occured')
				print('Sorry error occured')

	
