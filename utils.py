from mne.io import read_raw_edf
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import plotly.express as px
def read_edf_by_fileindex(fileindex):
    filepath = f'data/{fileindex}.edf'
    raw = read_raw_edf(filepath,verbose=False)
    raw.rename_channels({'EEG 1':'EEG','EEG 2':'EMG'})
    raw.set_channel_types({'Activity':'misc',
                        'EEG':'eeg',
                        'EMG':'emg',
                        'HD BattVoltage':'misc',
                        'On Time':'misc',
                        'Signal Strength':'misc',
                        'Temperature':'misc'})
    return raw
def read_metadata_by_fileindex(fileindex):
    df = pd.read_csv(f'data/{fileindex}.csv')
    df['timestamp'] = df['timestamp'].astype('datetime64')
    df.loc[df['label'] == 'W','label'] = 1
    df.loc[df['label'] == 'P','label'] = .5
    df.loc[df['label'] == 'S','label'] = 0
    for x,y in zip(df.columns[2:-2],np.linspace(0,19.5,40)):
        df = df.rename(mapper = {x:y},axis=1)
    df = df.rename(mapper = {'EEG 2 (Mean, 10s)':'emg'},axis=1)
    df = df.rename(mapper = {'Activity (Mean, 10s)':'activity'},axis=1)
    return df
def get_eeg_by_fileindex(fileindex):
    return read_edf_by_fileindex(fileindex).get_data(picks='EEG')[0]