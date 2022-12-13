
# Import libraries using import keyword
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from matplotlib import pyplot as plt
from pyESN.pyESN import ESN
from utils import *
from scipy.signal import periodogram,decimate
eeg = get_eeg_by_fileindex(1)
metadata = read_metadata_by_fileindex(1)
eeg = decimate(eeg, q=10)
train_ctrl = []
train_output = []
for i,epoch_label in enumerate(metadata['label'].to_numpy()):
    for j in range(500):
        train_ctrl.append([1,eeg[(i*500)+j]])
        train_output.append(epoch_label)
train_ctrl = np.array(train_ctrl)
train_output = np.array(train_output)
# Setting Plot and Axis variables as subplots()
# function returns tuple(fig, ax)
Plot, Axis = plt.subplots()

# Adjust the bottom size according to the
# requirement of the user
plt.subplots_adjust(bottom=0.25)
 
# plot the x and y using plot function
l = plt.plot(train_ctrl[:,1][:1000000])
plt.plot(train_output[:1000000]/10000)
 
# Choose the Slider color
slider_color = 'White'
 
# Set the axis and slider position in the plot
axis_position = plt.axes([0.2, 0.1, 0.65, 0.03],
                         facecolor = slider_color)
slider_position = Slider(axis_position,
                         'Pos', 0, 1000000)
 
# update() function to change the graph when the
# slider is in use
def update(val):
    pos = slider_position.val
    Axis.axis([pos, pos+50000, -.0003, .0003])
    Plot.canvas.draw_idle()
 
# update function called using on_changed() function
slider_position.on_changed(update)
 
# Display the plot
plt.show()