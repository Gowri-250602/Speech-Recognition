#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition
import  pyaudio
import speech_recognition as sr


# In[ ]:


r= sr.Recognizer()
while True: #convert speech to text in real time
    with sr.Microphone() as source:
        #clear background noise
        r.adjust_for_ambient_noise(source, duration=0.3)
        
        print("Speak Now")
        print("Listening.....")
        #capture the audio
        audio = r.listen(source)
        text=r.recognize_google(audio,language='hi-IN')
        print("Speaker",text)
        text=r.recognize_google(audio,language='ta-IN')
        print("Speaker",text)
        text=r.recognize_google(audio,language='ml')
        print("Speaker",text)
        text=r.recognize_google(audio,language='kn')
        print("Speaker",text)
        text=r.recognize_google(audio,language='sa')
        print("Speaker",text)
        #text=r.recognize_google(audio,language='gu')
        #print("Speaker",text)
        #text=r.recognize_google(audio,language='pa')
        #print("Speaker",text)
        
        text=r.recognize_google(audio)
        print("Speaker",text)
        if text=="quit":
                break
        

