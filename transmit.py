import numpy as np
import adi
import matplotlib.pyplot as plt
import time
sample_rate = 1e6 # Hz
center_freq = 100e6 # Hz
num_samps = 10000 # number of samples returned per call to rx()

sdr = adi.Pluto("ip:192.168.2.1")
sdr.gain_control_mode_chan0 = 'manual'

print(sdr._get_iio_attr('voltage0','hardwaregain', False))
sdr.sample_rate = int(sample_rate)
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 0 # dB

fc = 2000
ts = 1/float(sample_rate)
t = np.arange(0, num_samps*ts, ts)
x_symbols_i = np.sin(2*np.pi*t*fc) # Amplitude of the I-signal
x_symbols_q = np.cos(2*np.pi*t*fc) # Amplitude of the Q-signal
x_symbols_iq = x_symbols_i + 1j*x_symbols_q # j = sqrt(-1) . This is the Iq signal
samples = np.repeat(x_symbols_iq, 1)
tx_samples=np.copy(samples)
samples *= 2**14 # To scale the signal according to the range of the SDR

while True:
    sdr.tx_destroy_buffer()
    #time.sleep(2)

    # Start the transmitter
    sdr.tx_cyclic_buffer = True # Enable cyclic buffers
    sdr.tx(tx_samples) # start transmitting
    plt.clf()
    plt.plot(t,np.real(tx_samples))
    plt.pause(0.05)
    # auto exit when closing the plot window
    time.sleep(2)
plt.show