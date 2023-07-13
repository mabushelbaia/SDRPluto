from pluto import SDR
import matplotlib.pyplot as plt
import numpy as np


sdr = SDR("192.168.2.1", sample_rate=1e6, center_freq=50e6, num_samps=10000)

ts = 1/float(sdr.sample_rate)
t = np.arange(0, sdr.num_samps*ts, ts)
sdr.rx_config(mode="manual", gain=50)
rx_samples = sdr.recive()
plt.plot(t, np.real(rx_samples))
plt.plot(t, np.imag(rx_samples))
plt.show()