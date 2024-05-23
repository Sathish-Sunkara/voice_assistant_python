from gtts import gTTS
import os
from playsound import playsound
import pyttsx3

"""it saves the text into mp3 file in folder"""
def text_to_speech1(text,language = "en") :
    tts = gTTS(text = text , lang = language , slow = False)
    tts.save("C:\\Users\\S Satish\\OneDrive\\Documents\\Python Projects\\voice assistant project\\voice.mp3")
    os.system("mpg123 voice.mp3")


def text_to_speech2(text,language = "en") :
    engine = pyttsx3.init()
    # getting voices
    voices = engine.getProperty("voices")
    engine.setProperty('voice' , voices[0].id)
    engine.say(text)
    engine.runAndWait()





text = "hello how are you ??" 
text_to_speech2(text)