
### Import Statements

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def load_streamflow(filename):
    array2 = np.genfromtxt(filename, delimiter=',',dtype=str,skip_header=1)
    dates = array2[:,0].astype('datetime64')
    y_1 = array2[:,1].astype(float)
    y_2 = array2[:,2].astype(float)
    y_3 = array2[:,3].astype(float)
    y_4 = array2[:,4].astype(float)
    y_5 = array2[:,5].astype(float)
    flows = np.array([y_1, y_2, y_3, y_4, y_5])
    return dates, flows


def plot_streamflow(dates, flows, sites):
    x = dates
    y_1, y_2, y_3, y_4, y_5 = flows
    plt.plot(x, y_1, label=sites[0], color = 'orange')
    plt.plot(x, y_2, label=sites[1], color = 'blue')
    plt.plot(x, y_3, label=sites[2], color = 'green')
    plt.plot(x, y_4, label=sites[3], color = 'red')
    plt.plot(x, y_5, label=sites[4], color = 'purple')
    plt.xlabel('Date')
    plt.ylabel('Flowrate (cfs)')
    plt.xticks(rotation=45)
    plt.title('Provo River Streamflow Data (2021)')
    plt.legend(loc = 'upper right', fontsize = 10)
    plt.grid(True)
    plt.show()

sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
