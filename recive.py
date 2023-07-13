from pluto import SDR
import matplotlib.pyplot as plt
import numpy as np


sdr = SDR("192.168.2.1")

ts = 1/float(sdr.sample_rate)
t = np.arange(0, sdr.num_samps*ts, ts)
sdr.rx_config(mode="manual", gain=50)
rx_samples = sdr.recive()
plt.plot(t, np.real(rx_samples))
plt.show()