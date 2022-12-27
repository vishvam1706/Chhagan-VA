# Created By TV
# Subscribe to TrySoTv

import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pyautogui
import time
from selenium import webdriver
import os
import pywhatkit

engine = pyttsx3.init()
rate = engine.getProperty('rate') 
engine.setProperty('rate', 160) 

def takeaction():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        # r.pause_threshold = 1
        # r.energy_threshold = 2000
        audio = r.listen(source,0,8)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-IN')
            print(query)
        except Exception as e:
            print("Say again")
            return "none"
        return query
    

def speak(audio):
   
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def intoduction():
    hour = int(datetime.datetime.now().hour)

    if(hour>=0 and hour<12):
        print("Hello Good Morning!")
        speak("Hello Good Morning!")
    elif(hour>=12 and hour<18):
        print("Hello Good Afternoon!")
        speak("Hello Good Afternoon!")
    else:
        print("Hello Good Evening!")
        speak("Hello Good Evening!")
    
    print("I am chhgan sir. please tell me how I may help you.")
    speak("I am chhgan sir. please tell me how I may help you.")
    
if __name__ == "__main__":
    intoduction()
    while True:
        action = takeaction().lower()
        # action = takeaction()
        if "open youtube" in action:
            speak("Opening youtube")
            webbrowser.open_new_tab("https://youtube.com/")
        if "open codewithharry" in action:
            speak("Opening codewithharry on youtube")
            webbrowser.open_new_tab("https://www.youtube.com/@CodeWithHarry/featured")
        elif "open spotify" in action:
            speak("Opening Soptify")
            webbrowser.open_new_tab("https://spotify.com/")
        elif "narendra modi" in action:
            speak("this is the information i found.")
            ny = wikipedia.summary("Narendra Modi",sentences=3)
            speak(ny)
        elif "c syntax" in action:
            speak("sure i will write a code for you")
            speak("Writing start in 3 second")
            time.sleep(3);
            pyautogui.typewrite('#include<stdio.h>\n')
            pyautogui.typewrite('#include<conio.h>\n')
            pyautogui.typewrite('#include<string.h>\n')
            pyautogui.typewrite('int main()\n')
            pyautogui.typewrite('{\n\n')
            pyautogui.typewrite('return 0;')
        elif "time" in action:
            print(f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}')
            speak(f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}')
        elif "scroll down" in action:
            speak('scrolling down')
            pyautogui.scroll(-500)
        elif "scroll up" in action:
            speak('scrolling down')
            pyautogui.scroll(500)
        elif "play" in action:
            speak(action)
            search = action.replace("play",'')
            pywhatkit.playonyt(search,False,True)
            # (search,True)
        elif "search" in action:
            speak(action)
            search = action.replace("search",'')
            pywhatkit.search(search)
            # (search,True)
        elif "screenshot" in action:
            speak('screenshot save successful')
            ssname = str(datetime.datetime.now().ctime())
            ssname = ssname.replace('.','_')
            ssname = ssname.replace(':','_')[0:-5]
            os.chdir('C:\T V\Screenshot')
            img = pyautogui.screenshot();
            img.save(f'{ssname}.png')
        elif "shutdown" in action:
            speak("I am going to shut down")
            break
        elif "thanks" in action:
            speak("Your Welcome sir")
        else:
            print("not action define")