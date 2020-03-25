import os
import numpy as np
import noiselib
reload(noiselib)
from dataChest import *
import matplotlib.pyplot as plt

class QPTunneling(object):
    
    def __init__(self, fs=1/100e-6):
        self.fs = fs
        vis = 1
        self.transfer = 1/vis**2
    
    def add_datasets(self, file_path, data_str='Single_Shot_Occupations_SB1'):
        if type(file_path) == str:
            file_path = [file_path]
        for f in file_path:
            data = noiselib.loadmat(f)
            o = np.array(data[data_str])
            trials, reps = o.shape
            if not hasattr(self, 'data'):
                self.data = np.empty((0,reps))
            self.data = np.concatenate([self.data, o])
    
    def add_data(self, o):
        trials, reps = o.shape
        if not hasattr(self, 'data'):
            self.data = np.empty((0,reps))
        self.data = np.concatenate([self.data, o])
    
    def get_psd(self, window_averaging = True):
        cpsd, f = noiselib.partition_and_avg_psd(self.data, self.fs)
        cpsd = self.transfer * cpsd
        if window_averaging:
            cpsd = noiselib.window_averaging(cpsd)
        return cpsd, f
        
    def plot_psd(self, window_averaging = True, figNum=None, label=None):
        psd, f = self.get_psd(window_averaging)
        fig = plt.figure(figNum)
        ax = fig.add_subplot(111)
        ax.set_title('PSD')
        ax.set_xlabel('Frequency [Hz]')
        ax.set_ylabel('$S_\eta (\eta^2/Hz)$')
        ax.plot(f, psd, label=label)
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.legend()
        ax.grid()
        plt.draw()
        plt.pause(0.05)
        return fig.number