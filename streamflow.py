
### Import Statements

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

array2 = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv', delimiter=',',dtype=str,skip_header=1)
array2
x = array2[:,0].astype('datetime64')
y_1 = array2[:,1].astype(float)
y_2 = array2[:,2].astype(float)
y_3 = array2[:,3].astype(float)
y_4 = array2[:,4].astype(float)
y_5 = array2[:,5].astype(float)


plt.plot(x, y_1, label='Site 10163000', color = 'orange')
plt.plot(x, y_2, label='Site 10155200', color = 'blue')
plt.plot(x, y_3, label='Site 10155500', color = 'green')
plt.plot(x, y_4, label='Site 10154200', color = 'red')
plt.plot(x, y_5, label='Site 10155000', color = 'purple')
plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')
plt.xticks(rotation=45)
plt.title('Provo River Streamflow Data (2021)')
plt.legend(loc = 'upper right', fontsize = 10)
plt.grid(True)
plt.show()

