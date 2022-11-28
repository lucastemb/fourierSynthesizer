from pyo import * 

s = Server().boot()
s.amp=0.1
s.start()
sound=LFO(freq=130.8, sharp=0.5, type=2, mul=1, add=0).out(dur=5)
s.gui(locals())
s.shutdown()
