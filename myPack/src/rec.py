#!/usr/bin/env python3
# license removed for brevity

import speech_recognition as sr

def speech_recognizer(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("speak any thing: ")
      audio = r.listen(source)
      try:  
        text = r.recognize_google(audio)
      except:
        print('sorry')
        return ''
    return text

speech_recognizer()