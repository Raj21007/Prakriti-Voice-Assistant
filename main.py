import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('clearing background noise.. please wait ')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Hey This Side your Companion Prakritti', 'How can i help you?')
        recordedaudio = recognizer.listen(source)
        command = recognizer.recognize_google(recordedaudio)
        print('You said:', command)
        if 'chrome' in command:
            a = 'Opening Chrome..'
            engine.say(a)
            engine.runAndWait()
            program = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            subprocess.Popen([program])
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            engine.say(time)
            engine.runAndWait()
        elif 'play' in command:
            b = 'Opening Youtube'
            engine.say(b)
            engine.runAndWait()
            pywhatkit.playonyt(command)
        elif 'what' in command:
            c = 'Searching for ' + command
            engine.say(c)
            engine.runAndWait()
            search_term = command.replace('what is', '').strip()
            program = f"https://www.google.com/search?q={search_term}"
            webbrowser.open_new_tab(program)

        elif 'where' in command:
            c = 'Searching for ' + command
            engine.say(c)
            engine.runAndWait()
            search_term = command.replace('what is', '').strip()
            program = f"https://www.google.com/search?q={search_term}"
            webbrowser.open_new_tab(program)

        elif 'how' in command:
            c = 'Searching for ' + command
            engine.say(c)
            engine.runAndWait()
            search_term = command.replace('what is', '').strip()
            program = f"https://www.google.com/search?q={search_term}"
            webbrowser.open_new_tab(program)

        elif 'tell' in command:
            c = 'Searching for ' + command
            engine.say(c)
            engine.runAndWait()
            search_term = command.replace('what is', '').strip()
            program = f"https://www.google.com/search?q={search_term}"
            webbrowser.open_new_tab(program)

cmd()
