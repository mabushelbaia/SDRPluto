from pluto import SDR
import matplotlib.pyplot as plt
import numpy as np
import time

sdr = SDR("192.168.2.1", sample_rate=1e6, center_freq=1000e6, num_samps=10000)
sdr.rx_config(mode="manual", gain=50.0)
ts = 1/float(sdr.sample_rate)
t = np.arange(0, sdr.num_samps*ts, ts)
plt.figure(0)

while plt.fignum_exists(0):
    rx_samples = sdr.recive()
    plt.clf()
    plt.plot(t, np.real(rx_samples))
    plt.pause(0.05)
    time.sleep(2)