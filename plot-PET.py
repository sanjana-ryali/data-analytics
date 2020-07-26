import matplotlib.pyplot as plt
import pandas as pd
import math

import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

#read csv file and labels columns 
df_czt = pd.read_csv('data_small.dat', header=None, sep='\s+', engine='python')
df_czt.columns = ['node', 'board', 'Rena', 'channel', 'polarity', 'ADC_e', 'ADC_s', 'ADC_v', 'counter']

print(df_czt.head())

#grouping by multiple columns 
grouped = df_czt.groupby(['node','board','Rena','channel','polarity'])

n_sub_plots_cols = 2
n_sub_plots_rows = math.ceil(grouped.ngroups/n_sub_plots_cols)

fig, axes = plt.subplots(n_sub_plots_rows, n_sub_plots_cols, figsize=(10,65))
fig.subplots_adjust(hspace=3.0, wspace=1.2)
axes_list = [item for sublist in axes for item in sublist] 

#plot column ADC energy
for key,group in grouped:
    ax = axes_list.pop(0)
    
    grouped.get_group(key)['ADC_e'].plot(kind='hist', bins=50, ax=ax)
    
    czt_values = grouped.get_group(key).values[0]
    
    #min and max 
    max_val = grouped.get_group(key)['ADC_e'].max()
    min_val = grouped.get_group(key)['ADC_e'].min()
    y_min, y_max = ax.get_ylim()
    #ax.annotate('Max: ' +str(max_val), xy=(3, y_max -(y_max * 0.1)), size=80)
    #ax.annotate('Min: ' +str(min_val), xy=(3, y_max -(y_max * 0.2)), size=80)
    
    
    #titles
    title = "Node:" + str(czt_values[0]) + " Board:"+ str(czt_values[1]) + " Rena:"+ str(czt_values[2]) + " Channel:"+ str(czt_values[3])
    #ax.set_title(title, fontsize=80)
    
    #x and y axis labels
    ax.set_xlabel("ADC value", fontsize=4)
    ax.set_ylabel("Counts", fontsize=4)
    
    ax.tick_params(labelsize=2)
    
    ax.autoscale(enable=True, axis='y', tight= False)
    ax.set_xlim(left=0)
    
    #anode or cathode
    if czt_values[4] == 0: 
        ax.set_xlim(right=3450)
    else:
        if czt_values[2] == 1: 
            ax.set_xlim(right=500)
        else: 
            ax.set_xlim(right=650)
    

for ax in axes_list:
    ax.remove()
    
plt.tight_layout()
#plt.show()

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

tkinter.mainloop()