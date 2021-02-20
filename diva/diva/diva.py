import sounddevice as sd
import numpy as np
from math import pi

fs = 16000 #Freq Base

n = np.arange(0,30,1/fs) #time axis (x,y,z) y adjusts duration
f = 1600; #Freq 1
f1 = 600; #Freq 2
x = np.sin(2*pi*f*n)
x1 = np.sin(2*pi*f1*n)
x = x + x1; #combining two freqs
sd.play(x, fs)

