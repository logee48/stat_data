import os
import psutil
from fastapi import FastAPI
from hurry.filesize import size

processor_count = psutil.cpu_count()

#RAm data
ram_data = psutil.virtual_memory()
ram_data_in_json = {
"wired_memory": ram_data[7],
"active_memory": ram_data[-3],
"total_memory": ram_data[0],
"percent_of_ram_used": ram_data[2],
"total_memory": ram_data[0],
"available_memory": ram_data[1] }
swap_data = psutil.swap_memory()
swap_data_in_json = {
    "total_swap_memory":swap_data[0],
    "used_swap_memory":swap_data[1],
    "free_swap_memory":swap_data[2],
    "percent_of_swap_memory":swap_data[4]
}

#battery data
battery = psutil.sensors_battery()

"""
Convert seconds into hours:minutes:seconds formate


"""
def time_convertion(seconds):
    minutes = seconds/60
    hours, minutes = divmod(minutes, 60)
    return {"hours":hours, "minuted":minutes}

battery_data_in_json = {
    "battery_percent": battery[0],
    "time_left": time_convertion(battery[1]),
    # "time_left_in_sec":battery[1],
    "pluged_in": battery[2]
}
# print(battery_data_in_json)


#CPU load

a,b,c = os.getloadavg()
# print(a,b,c)
# print((c/os.cpu_count())*100)
# print(psutil.cpu_percent())

res = [battery_data_in_json, swap_data_in_json, ram_data_in_json]



#cpu_count
# print(psutil.cpu_count())

# # battery details
# print(psutil.sensors_battery())

# # Ram data
# print(psutil.virtual_memory()[0]/1000000000)
# print(psutil.virtual_memory()[2])

# print(os.getloadavg())
# print(psutil.getloadavg())
# a,b,c = os.getloadavg()
# print((a/os.cpu_count())*100)
# #current system-wide CPU utilization
# #know to diff between cpu load and cpu usage

# a = psutil.cpu_percent(60)
# print(a)
# print(8*aˀ̀)




app = FastAPI()

@app.get("/")
async def root():
    return {"ram_data":ram_data_in_json,"battery_data":battery_data_in_json,"swap_memory_data":swap_data_in_json}
