from pluto import SDR
import matplotlib.pyplot as plt
import numpy as np
import time

sdr = SDR("192.168.2.1", sample_rate=1e6, center_freq=100e6, num_samps=10000)
sdr.tx_config("fast_attack", 0.0)
wc =  2*np.pi*2000
# Signal Configuration
ts = 1/float(sdr.sample_rate)
t = np.arange(0, sdr.num_samps*ts, ts)
samples = sdr.signal(-np.sin(wc*t), np.cos(wc*t))
plt.plot(t, np.real(samples))
# plt.show()
while True:
    sdr.pluto.tx_destroy_buffer()
    sdr.transmit(samples)
    time.sleep(1)
