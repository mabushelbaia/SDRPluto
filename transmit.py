from pluto import SDR
import matplotlib.pyplot as plt
import numpy as np


sdr = SDR("192.168.2.1")
sdr.tx_config("manual", 0.0)
wc =  2*np.pi*2000
# Signal Configuration
ts = 1/float(sdr.sample_rate)
t = np.arange(0, sdr.num_samps*ts, ts)
samples = sdr.signal(-np.sin(wc*t), np.cos(wc*t))
sdr.transmit(samples)