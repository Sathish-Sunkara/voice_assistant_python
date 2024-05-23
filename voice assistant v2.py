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

def open_websites(text) :
    pass


def assistant():
    clear() 
    searched_text = search_bar.get().lower()
    if 'wikipedia' in searched_text:
        print('Searching Wikipedia...')
        searched_text = searched_text.replace("wikipedia", "")
        results = wikipedia.summary(searched_text, sentences=5)
        search_output.insert(0,results)

    if 'open youtube' in searched_text:
        text = "youtube was opening...."
        search_output.insert(0,text)
        webbrowser.open("youtube.com")

    if 'open google' in searched_text:
        text = "Here you go to Google"
        search_output.insert(0,text)
        webbrowser.open("google.com")

    elif 'open stackoverflow' in searched_text:
        text = "Here you go to Stack Overflow. Happy coding!"
        search_output.insert(0,text)
        webbrowser.open("stackoverflow.com")
    elif "today" in searched_text:
        text = datetime.datetime.now()
        search_output.insert(0,text)
    elif 'open whatsapp' in searched_text:
        text = "Here you go to whatsapp !"
        search_output.insert(0,text)
        webbrowser.open("whatsapp.com")




    




root = tk.Tk()
root.geometry("1000x1000")
root.title("voice assistant")

label = tk.Label(root , text="search here..." ,font=("arial" ,30) , fg = "#0d380e")
label.pack(pady=5)

search_bar = tk.Entry(root ,width=70,font=("arial" ,30) , fg = "#0a261a")
search_bar.pack(pady=15,padx=10)

btn = tk.Button(text="search" ,fg="#36ff97" , bg="#11282e",command=assistant,font=('arial',25),height=1,width=5)
btn.pack(pady=10)

search_output = tk.Entry(root,width=130,font=('arial',60) ,fg="#122923")
search_output.pack(padx=10,pady=10)
















root.mainloop()