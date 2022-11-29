from tkinter import * 
from tkinter import ttk 
import time
from playsound import playsound
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from graph import square
from graph import summation

root = Tk()
root.title("Wave Selector")
mainframe = ttk.Frame(root, width=50, height=50, padding = "12 12 12 12")

def btn_pressed(text):
    if text == 1: 
        playsound("sine.wav", False)
        x=np.linspace(2*-np.pi,2*np.pi,100)
        y=np.sin(x)
        plt.figure(num="Sine Wave")
        plt.plot(x,y,linewidth=1.0)
        plt.title(r'$f(x)=\sin(x)$')
        plt.show()
        time.sleep(4)
        plt.close()
    elif text == 2:
        playsound("square.wav", False)
        x=np.linspace(2*-np.pi,2*np.pi,100)
        y=summation(1,5,x,2)
        
        plt.figure(num="Square Wave")
        plt.plot(x,y,linewidth=1.0)
        plt.title(r'$f(x)=\sum_{n=1}^\infty (\frac{1}{\pi}) (\frac{2-2(-1)^n}{n}) \sin(xn)$')
        plt.show()
        time.sleep(4)
        plt.close()
    elif text == 3: 
        playsound("saw.wav", False)
        x=np.linspace(2*-np.pi,2*np.pi,100)
        y=summation(1,5,x,3)

        plt.figure(num="Sawtooh Wave")
        plt.plot(x,y,linewidth=1.0)
        plt.title(r'$f(x)=\sum_{n=1}^\infty (\frac{1}{\pi}) (\frac{2(-1)^n}{n}) \sin(xn)$')
        plt.show()
        time.sleep(4)
        plt.close()
    else:
        playsound("triangle.wav", False)
        x=np.linspace(2*-np.pi,2*np.pi,100)
        y=summation(1,5,x,4)
        
        plt.figure(num="Triangle Wave")
        plt.plot(x,y,linewidth=1.0)
        plt.title(r'$f(x)=\sum_{n=1}^\infty (\frac{1}{\pi}) (\frac{2-2(-1)^n}{n^2}) \cos(xn)$')
        plt.show()
        time.sleep(4)
        plt.close()




#sine photo and btn
sinep= PhotoImage(file="589707-200.png")
sinep=sinep.subsample(3,3)
sine=Button(root, height=100, width=100, image=sinep, command=lambda: btn_pressed(1)).grid(row=0,column=1, sticky=W)

#square photo and btn
sqp=PhotoImage(file="2613422-200.png")
sqp=sqp.subsample(2,2)
square=Button(root, text="2", height=100, width=100, image=sqp, command=lambda: btn_pressed(2)).grid(row=0,column=2, sticky=W)

#saw photo and btn
sawp=PhotoImage(file="863-8636352_sound-wave-sawtooth-synth-music-comments.png")
sawp=sawp.subsample(19,19)
saw=Button(root, text="3", height=100, width=100, image=sawp, command=lambda: btn_pressed(3)).grid(row=0,column=3)

#triangle photo and btn
trip=PhotoImage(file="3629643-200.png")
trip=trip.subsample(3,3)
triangle=Button(root,text="4", height=100, width=100, image=trip, command=lambda: btn_pressed(4)).grid(row=0,column=4)




root.mainloop()
    
    
