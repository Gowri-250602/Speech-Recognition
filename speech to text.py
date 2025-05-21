#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyttsx3


# In[2]:


pip install SpeechRecognition


# In[5]:


pip install PyAudio


# In[1]:


import speech_recognition as sr
import pyttsx3
r= sr.Recognizer()
def speaktext(command):
    engine= pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# In[3]:


with sr.Microphone() as source2:
    print("Silence Please")
    r.adjust_for_ambient_noise(source2,duration=2)
    print("Let's Speak......")
    audio2= r.listen(source2)
    MyText =r.recognize_google(audio2)
    MyText= MyText.lower()
    print("Did you say "+ MyText)
    speaktext(MyText)

