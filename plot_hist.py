import matplotlib.pyplot as plt
import pandas as pd


#read csv file and labels columns 
df_czt = pd.read_csv('data_20200506_003249.dat', header=None, sep='\s+', engine='python')
df_czt.columns = ['node', 'board', 'Rena', 'channel', 'polarity', 'ADC_e', 'ADC_s', 'ADC_v', 'counter']

print(df_czt.head())

#grouping by multiple columns 
grouped = df_czt.groupby(['node','board','Rena','channel','polarity'])

#plot column ADC energy
for key,group in grouped:
    
    grouped.get_group(key)['ADC_e'].plot(kind='hist', bins=50)
       
    max_val = grouped.get_group(key)['ADC_e'].max()
    min_val = grouped.get_group(key)['ADC_e'].min()
    
    axes = plt.gca()
    y_min, y_max = axes.get_ylim()
    plt.annotate('Max: '+str(max_val), xy=(30, y_max -(y_max * 0.1)))
    plt.annotate('Min: '+str(min_val), xy=(30, y_max -(y_max * 0.2)))
    
    #anode or cathode
    czt_values = grouped.get_group(key).values[0]
    
    #adce_freq = grouped.get_group(key)['ADC_e'].value_counts()
    #print(adce_freq)
    
    plt.autoscale(enable=True, axis='y', tight= False)
    plt.xlim(left=0)
    
    if czt_values[4] == 0: 
        plt.xlim(right=3450)
    else:
        if czt_values[2] == 1: 
            plt.xlim(right=500)
        else: 
            plt.xlim(right=650)
    
    title = "Node:" + str(czt_values[0]) + " Board:"+ str(czt_values[1]) + " Rena:"+ str(czt_values[2]) + " Channel:"+ str(czt_values[3])
    plt.title(title)

    #plt.relim(self, visible_only=False)
    #plt.autoscale_view(tight=None, scalex=False, scaley=True)
    plt.xlabel("ADC value")
    plt.ylabel("Counts")

    plt.show()
    

