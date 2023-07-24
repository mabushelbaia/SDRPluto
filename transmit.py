from pluto import SDR
import matplotlib.pyplot as plt
import numpy as np
import time

sdr = SDR("192.168.2.1", sample_rate=1e6, center_freq=1000e6, num_samps=1000)
sdr.tx_config("manual", 0.0)
wc =  2*np.pi*2000
# Signal Configuration
ts = 1/float(sdr.sample_rate)
t = np.arange(0, sdr.num_samps*ts, ts)
samples = sdr.signal(np.sin(wc*t), np.cos(wc*t))
plt.plot(t, np.real(samples))
sdr.pluto.tx_destroy_buffer()
sdr.pluto.tx_cyclic_buffer = True
sdr.transmit(samples)
plt.show()

    