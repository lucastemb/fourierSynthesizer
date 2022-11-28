from pyo import *


#start server

sound=1



def testRun(server,snd):
    server.shutdown()
    server.boot()
    server.gui(locals())
    notes = Notein(poly=8, scale=0, first=0, last=127, channel=0, mul=1)
    notes.keyboard(title="Fourier Synthesizer")
    freqs= MToF(notes["pitch"])

    amps = Port(notes["velocity"], risetime =0.005, falltime=0.25, mul=1)

    sigL= LFO(freq=freqs, sharp=0, type=sound, mul=amps)
    sigR= LFO(freq=freqs, sharp=0, type=sound, mul=amps)

    outL=sigL.mix(1).out()
    outR=sigR.mix(1).out(1)

    def noteon(voice): 
        pit=int(notes["pitch"].get(all=True)[voice])
        vel=int(notes["velocity"].get(all=True)[voice] * 127)

    def noteoff(voice):
        pit=int(notes["pitch"].get(all=True)[voice])
        vel=int(notes["velocity"].get(all=True)[voice] * 127)

    def select_opt():
        print("Hello")

    start=TrigFunc()
    tfon = TrigFunc(notes["trigon"],noteon, arg=list(range(8)))
    tfoff = TrigFunc(notes["trigoff"], noteoff, arg=list(range(8)))
    graph = Scope(sigL)
    server.gui(locals())
    

    
    


s = Server()
s.setMidiInputDevice(99)
s.boot()


notes = Notein(poly=8, scale=0, first=0, last=127, channel=0, mul=1)
notes.keyboard(title="Fourier Synthesizer")
freqs= MToF(notes["pitch"])

amps = Port(notes["velocity"], risetime =0.005, falltime=0.25, mul=1)

sigL= LFO(freq=freqs, sharp=0, type=sound, mul=amps)
sigR= LFO(freq=freqs, sharp=0, type=sound, mul=amps)

outL=sigL.mix(1).out()
outR=sigR.mix(1).out(1)

def noteon(voice): 
    pit=int(notes["pitch"].get(all=True)[voice])
    vel=int(notes["velocity"].get(all=True)[voice] * 127)

def noteoff(voice):
    pit=int(notes["pitch"].get(all=True)[voice])
    vel=int(notes["velocity"].get(all=True)[voice] * 127)

tfon = TrigFunc(notes["trigon"],noteon, arg=list(range(8)))
tfoff = TrigFunc(notes["trigoff"], noteoff, arg=list(range(8)))

graph = Scope(sigL)

s.gui(locals())





    