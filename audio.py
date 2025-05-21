#!/usr/bin/env python
# coding: utf-8

# In[17]:


from sklearn.preprocessing import MinMaxScaler
import numpy as np
import librosa
import IPython.display as ipd
import matplotlib.pyplot as plt


# In[18]:


audio_data, rate = librosa.load("record_out.wav")  

def show_data(audio_data):
    plt.figure()
    plt.title("data")
    plt.plot(audio_data)
    plt.show()

    
show_data(audio_data)
ipd.Audio(audio_data, rate=22050)


# In[19]:


data = librosa.feature.mfcc(y=audio_data)
print('before transform ', data[0][:10])
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(data)
data = scaler.transform(data)

show_data(data)
print('mfcc shape ', data.shape)


# In[20]:


data = scaler.inverse_transform(data)

print('after inverse transform ', data[0][:10])

wav = librosa.feature.inverse.mfcc_to_audio(data)
show_data(wav)
ipd.Audio(wav, rate=22050)


# In[ ]:




