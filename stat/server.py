import os
import psutil
from fastapi import FastAPI
from hurry.filesize import size
import firebase_admin
from firebase_admin import db
import json
import time

cred_object = firebase_admin.credentials.Certificate('key.json')
firebase_admin.initialize_app(cred_object, {
	'databaseURL':'https://pythonconn-2578e-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})

ref = db.reference("/data")
ramref = db.reference("/sysdata/ram")
# with open("sample.json", "r") as f:
# 	file_contents = json.load(f)
# ref.set(file_contents)
# b = "sam"
# a = {"a":"jh", "c":"works"}
# ref.set(json.dumps(a))



processor_count = psutil.cpu_count()

#RAm data
def get_ram_data(vm):
    # ram_data = psutil.virtual_memory()
    ram_data = vm
    ram_data_in_json = {
    "wired_memory": ram_data[7],
    "active_memory": ram_data[-3],
    "total_memory": ram_data[0],
    "percent_of_ram_used": ram_data[2],
    "total_memory": ram_data[0],
    "available_memory": ram_data[1] }
    return ram_data_in_json

#swap_memory
def get_swap_data(sm):
    swap_data = sm
    swap_data_in_json = {
        "total_swap_memory":swap_data[0],
        "used_swap_memory":swap_data[1],
        "free_swap_memory":swap_data[2],
        "percent_of_swap_memory":swap_data[4]
    }
    return swap_data_in_json

#battery data

"""
Convert seconds into hours:minutes:seconds formate


"""
def time_convertion(seconds):
    minutes = seconds/60
    hours, minutes = divmod(minutes, 60)
    return {"hours":hours, "minuted":minutes}

def get_battery_data(bd):
    battery = bd
    battery_data_in_json = {
        "battery_percent": battery[0],
        "time_left": time_convertion(battery[1]),
        # "time_left_in_sec":battery[1],
        "pluged_in": battery[2]
    }
    return battery_data_in_json



"""
Disk Usage

"""

def get_disk_data(dd):
    disk_val = dd
    disk_data_in_json = {
        "total":disk_val[0],
        "percent_used":disk_val[3],
        "free":disk_val[2],
        "used":disk_val[1]
    }
    return disk_data_in_json
# print(disk_data_in_json)

#CPU load

def get_cpu_load(cpul):
    load1, load5, load15 = cpul
    cpuu = os.cpu_count()
    l1 = (load1/cpuu)*100
    l5 = (load5/cpuu)*100
    l15 = (load15/cpuu)*100
    return {"loadover_1min":l1,"loadover_5min":l5,"loadover_15min":l15}
# print(get_cpu_load(os.getloadavg()))




app = FastAPI()
rref = db.reference("/sysdata/counter/")
print(rref.get()["counter"])
# print(json.parse(rref.get()))
@app.get("/api/v1/")
async def root():
    # a = {
    #     "ram_data": get_ram_data(psutil.virtual_memory()),
    #     "disk_data": get_disk_data(psutil.disk_usage("/")),
    #     "battery_data": get_battery_data(psutil.sensors_battery()),
    #     "swap_data": get_swap_data(psutil.swap_memory()),
    #     "load_data": get_cpu_load(os.getloadavg())
    # }

    # ref.set(a)
    # ramref.set(a)

    db.reference("/sysdata/ram/"+str(rref.get()["counter"])).set(get_ram_data(psutil.virtual_memory()))
    db.reference("/sysdata/disk/"+str(rref.get()["counter"])).set(get_disk_data(psutil.disk_usage("/")))
    db.reference("/sysdata/battery/"+str(rref.get()["counter"])).set(get_battery_data(psutil.sensors_battery()))
    db.reference("/sysdata/swap/"+str(rref.get()["counter"])).set(get_swap_data(psutil.swap_memory()))
    db.reference("/sysdata/load/"+str(rref.get()["counter"])).set(get_cpu_load(os.getloadavg()))
    db.reference("/sysdata/counter").set({"counter":rref.get()["counter"]+1})
    return({
        "ram_data": get_ram_data(psutil.virtual_memory()),
        "disk_data": get_disk_data(psutil.disk_usage("/")),
        "battery_data": get_battery_data(psutil.sensors_battery()),
        "swap_data": get_swap_data(psutil.swap_memory()),
        "load_data": get_cpu_load(os.getloadavg())
    })
