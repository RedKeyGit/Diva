import sounddevice as sd
import numpy as np
from math import pi
from pynput.keyboard import Listener, KeyCode

fs = 1800 #Freq Base
Phone_call = KeyCode(char='1');
Stop = KeyCode(char='2');

def on_press(key):
    if key == Phone_call:
        n = np.arange(9,500,1/fs) #time axis (x,y,z) x is offset? y could be duration. But that doesn't matter anymore.
        f = 1000; #Freq 1
        f1 = 10; #Freq 2
        x = np.cos(2*pi*f*n)
        x1 = np.sin(2*pi*f1*n)
        x = x * x1; #combining two freqs
        sd.play(x, fs)
    elif key == Stop:
        sd.stop()

with Listener(on_press=on_press) as listener:
    listener.join()


