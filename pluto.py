import numpy as np
import adi
import matplotlib.pyplot as plt
import time
class SDR:
    def __init__(self, IP, sample_rate=1e6, center_freq=100e6, num_samps=10000):
        self.pluto = adi.Pluto(f"ip:{IP}")
        self.sample_rate = sample_rate
        self.center_freq = center_freq
        self.num_samps = num_samps
        self.pluto.sample_rate = int(sample_rate)
        
    def rx_config(self, mode="manual", gain=30.0):
        # Configure RX
        self.pluto.rx_lo = int(self.center_freq)
        self.pluto.rx_rf_bandwidth = int(self.sample_rate)
        print(f"\033[92m [RECIVE BANDWIDTH] \033[00m {self.pluto._get_iio_attr('voltage0','rf_bandwidth', False)} Hz")
        self.pluto.rx_buffer_size = self.num_samps
        self.pluto.gain_control_mode_chan0 = mode
        print(f"\033[92m [RECIVE MODE] \033[00m {mode}")
        if mode == "manual":
            if gain >= 0 and gain <= 74.5:
                self.pluto.rx_hardwaregain_chan0 = gain
            else:
                print("\033[91m [WARNING] \033[00m RECIVE Gain must be between 0 and 74.5 dB")
        print(f"\033[92m [RECIVE GAIN] \033[00m {self.pluto._get_iio_attr('voltage0','hardwaregain', False)} dB")
                
        
    def tx_config(self, mode="manual", gain=0.0):
        # Configure TX  
        self.pluto.tx_lo = int(self.center_freq)
        self.pluto.tx_rf_bandwidth = int(self.sample_rate)
        print(f"\033[92m [RECIVE BANDWIDTH] \033[00m {self.pluto._get_iio_attr('voltage0','rf_bandwidth', False)} Hz")
        self.pluto.gain_control_mode_chan0 = mode
        print(f"\033[92m [TRANSMIT MODE] \033[00m {mode}")
        if mode == "manual":
            if  gain >= -90 and gain <= 0:
                self.pluto.tx_hardwaregain_chan0 = gain
            else:
                print("\033[91m [WARNING] \033[00m TRANSMIT Gain must be between -50 and 0 dB")
        print(f"\033[92m [TRANSMIT GAIN] \033[00m {self.pluto._get_iio_attr('voltage0','hardwaregain', True)} dB")
    
    def recive(self):
        self.rx_samples = self.pluto.rx()
        return self.rx_samples
    
    def transmit(self, tx_samples):
        self.pluto.tx_destroy_buffer()
        self.pluto.tx(tx_samples)
    
    def signal(self, i_samples, q_samples):
        signal = i_samples + 1j*q_samples
        samples = np.repeat(signal, 1)
        samples *= 2**14
        return samples