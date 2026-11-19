
### Import Statements

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd

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
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


def summarize(dates, flows, sites):
    with open("streamflow_summary.csv", "w") as f:
        f.write("Streamflow Summary:\n")
        f.write(f'Gauge\t\tMax (cfs)\tDate of Max\t\t\t\tMin (cfs)\t\tMean (cfs)\n')
        for i in range(len(sites)):
            site_flows = flows[i]
            mean_flow = np.mean(site_flows)
            max_flow = np.max(site_flows)
            min_flow = np.min(site_flows)
            f.write(f"{sites[i]}\t{max_flow:.2f}\t\t{dates[np.argmax(site_flows)]}\t\t{min_flow:.2f}\t\t\t{mean_flow:.2f}\n")
    print("Streamflow Summary:")
    print(f'Gauge\t\tMax (cfs)\tDate of Max\t\tMin (cfs)\tMean (cfs)')
    for i in range(len(sites)):
        site_flows = flows[i]
        mean_flow = np.mean(site_flows)
        max_flow = np.max(site_flows)
        min_flow = np.min(site_flows)
        print(f"{sites[i]}\t{max_flow:.2f}\t\t{dates[np.argmax(site_flows)]}\t{min_flow:.2f}\t\t{mean_flow:.2f}")

#this function was written by AI 
#this function reports the number of hours each site has exceeded a given flow threshold.
def report_hours_above_threshold(flows, sites):
    while True:
        try: #try is a control flow statement that ensures the user input is valid. If it's not, the block starts over.
            threshold = float(input("Enter a flow threshold in cfs: "))
            break
        except ValueError:
            print("Please enter a numeric threshold.")

    print(f"\nHours with flow above {threshold:.2f} cfs:")
    for i, site_flows in enumerate(flows): #enumerate is a built-in function that returns both the index and the value of items in flows.
        hours_above = np.count_nonzero(site_flows > threshold) * 0.25 #each flow measurement is 0.25 hours
        print(f"{sites[i]}: {hours_above:.2f} hours")
        

sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
summarize(dates, flows, sites)
report_hours_above_threshold(flows, sites)
