import matplotlib.pyplot as plt
import numpy as np
import time
import azurerm
import pprint
import datetime
import sys
sys.path.insert(0, '/home/negat/credentials/aad/')

from aadcredentials import *

pp = pprint.PrettyPrinter(indent=2)

access_token = azurerm.get_access_token(
    tenant_id,
    application_id,
    application_secret
)


x = []
y = []

fig = plt.figure()
ax = fig.add_subplot(111)
ax.axis([-60, -1, 0, 100])
ax.set_xlabel("Time (number of minutes before now)")
ax.set_ylabel("% CPU utilization")

li, = ax.plot(x, y)


# draw and show it
fig.canvas.draw()
plt.show(block=False)

# loop to update the data
while True:
        try:
                x = range(-60, 0, 1)
                y = []
                t = []
                metrics = azurerm.get_metrics_for_resource(access_token, subscription_id, 'nsghostmetrics', 'Microsoft.Compute', 'virtualMachineScaleSets', 'nsghostme')['value'][0]

                for datum in metrics['data']:
                        if 'average' in datum:
                                y.append(datum['average'])
                                t.append(datum['timeStamp'])

                print(y)
                print(t)

                if len(y) == len(x):
                        ax.set_title(str(datetime.datetime.now().time()) + " UTC")
                        #real_x = [elem.split(':')[1] for elem in x]
                        #print(x)
                        #print(y)
                        # set the new data
                        li.set_xdata(x)
                        li.set_ydata(y)
                
                        fig.canvas.draw()
                
                        time.sleep(2)
        except KeyboardInterrupt:
                break
