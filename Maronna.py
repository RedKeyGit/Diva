import sounddevice as sd
import numpy as np
from math import pi
from pynput.keyboard import Listener, KeyCode

fs = 1800 #Freq Base
Phone_call = KeyCode(char='2');
AAA = KeyCode(char='9')
Stop = KeyCode(char='0');
Exit = KeyCode(char=']');

def on_press(key):
    if key == Phone_call:
        n = np.arange(15,100,1/fs) #time axis (x,y,z) x is offset? y could be duration. But that doesn't matter anymore.
        f = 1000; #Freq 1
        f1 = 10; #Freq 2
        x = np.cos(2*pi*f*n)
        x1 = np.sin(2*pi*f1*n)
        x = x * x1; #combining two freqs
        sd.play(x, fs)
        print("Phone_Call")
    elif key == AAA:
        n = np.arange(0.8,100,1/fs)
        f = 800; #Freq 1
        f1 = 100; #Freq 2
        x = np.cos(2*pi*f*n)
        x1 = np.sin(2*pi*f1*n)
        x = x * x1; #combining two freqs
        sd.play(x, fs)
        print("Unnamed Sample")
    elif key == Stop:
        sd.stop()
        print("Stopped")
    elif key == Exit:
        sd.stop()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()


