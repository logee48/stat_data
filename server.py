import os
import psutil

#cpu_count
print(psutil.cpu_count())

# battery details
print(psutil.sensors_battery())

# Ram data
print(psutil.virtual_memory()[0]/1000000000)
print(psutil.virtual_memory()[2])

print(os.getloadavg())
print(psutil.getloadavg())
a,b,c = os.getloadavg()
print((a/os.cpu_count())*100)
#current system-wide CPU utilization
#know to diff between cpu load and cpu usage

a = psutil.cpu_percent(60)
print(a)
print(8*aˀ̀)