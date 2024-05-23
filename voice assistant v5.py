import tkinter as tk
import os
import datetime
import webbrowser
import requests
import pyjokes
import wolframalpha
import subprocess
import time
import winshell
import json
import pyttsx3
import speech_recognition as sr
from urllib.request import urlopen
from twilio.rest import Client
import shutil
import wikipedia

def clear():
    search_output.delete(0,tk.END)

def wishMe():   # this handles all the initial stage of assistant
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sir!")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")
    speak("I am your Assistant")
    speak("siri 1010101.101010ABC")
    # asking the name of owner
    speak("please tell me your name sir")

    search_bar.config(state=tk.NORMAL)
    name = search_bar.get()
    speak("hi Mr. "+name+ "how can i assist today ??")
    search_output.config(state=tk.NORMAL)

def open_websites(text) :
    speak(text+" is "+"opening , please wait")
    search_output.insert(0,text+" opening......")
    url = "https://www."+text+".com"
    webbrowser.open(url)

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()



def assistant():
    clear() 
    if search_bar.get() == "" :
        wishMe()
    searched_text = search_bar.get().lower()

    if 'wikipedia' in searched_text:
        search_output.insert(0,'Searching Wikipedia...')
        speak('Searching Wikipedia...')
        searched_text = searched_text.replace("wikipedia", "")
        results = wikipedia.summary(searched_text, sentences=3)
        search_output.delete(0,tk.END)
        speak(results)
        search_output.insert(0,results)

    elif "open" in searched_text :
        open_websites(searched_text.replace("open ",""))

    elif "today" in searched_text:
        text = datetime.datetime.now()
        speak(str(text))
        search_output.insert(0,text)

    
    




    




root = tk.Tk()
root.geometry("1000x1000")
root.title("voice assistant")

label = tk.Label(root , text="search here..." ,font=("arial" ,30) , fg = "#0d380e")
label.pack(pady=5)

search_bar = tk.Entry(root ,width=70,font=("arial" ,30) , fg = "#0a261a")
search_bar.pack(pady=15,padx=10)


btn = tk.Button(text="click here" ,fg="#36ff97" , bg="#11282e",command=assistant,font=('arial',25),height=1,width=10)
btn.pack(pady=10)

search_output = tk.Entry(root,width=130,font=('arial',60) ,fg="#122923")
search_output.pack(padx=10,pady=10)
search_output.config(state=tk.DISABLED)
















root.mainloop()