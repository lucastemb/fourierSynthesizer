import numpy as np

def summation(start,end,x,func):

    fn=0
    for i in range(start, end+1):
        if func == 2: 
            fn+=square(x,i)
        if func == 3:
            fn+=sawtooth(x,i)
        if func == 4: 
            fn+=triangle(x,i)
        
    return fn


def square(x,n):
   return (((1/np.pi)*((2-2*(-1)**n)/(n)))*(np.sin(x*n)))

def sawtooth(x,n):
    return (((1/np.pi)*((2*(-1)**n)/(n)))*(np.sin(x*n)))

def triangle(x,n):
    return (((1/np.pi)*((2-2*(-1)**n)/(n**2)))*(np.cos(x*n)))



