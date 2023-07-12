import numpy as np
import adi
import matplotlib.pyplot as plt
import time

center_freq = 100e6 # 
sample_rate = 1e6 # Hz
num_samps = 10000 # number of samples returned per call to rx()

sdr = adi.Pluto("ip:192.168.2.1")
sdr.gain_control_mode_chan0 = 'manual'
fc = 2000
ts = 1/float(sample_rate)
t = np.arange(0, num_samps*ts, ts)
sdr.rx_lo = int(center_freq)
sdr.rx_rf_bandwidth = int(sample_rate)
sdr.rx_buffer_size = num_samps
sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 10.0 # dB, increase to increase the receive gain, but be careful not to saturate the ADC
while True:
    for i in range(0, 10):
        clear_buffer = sdr.rx()
    rx_samples = sdr.rx()
    
    plt.clf()
    plt.plot(t,np.real(rx_samples))
    plt.pause(0.05)
    # auto exit when closing the plot window
    time.sleep(2)