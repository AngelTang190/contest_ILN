# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:38:22 2021

@author: ASUS
"""
from datetime import datetime as dt
import matplotlib.pyplot as plt
import json

#Function to print list
def print_list(new_list):
    for i in range(len(new_list)):
        for j in range(max_col):
            print(new_list[i][j],end=" ")
        print("\n")

class WayPoints():
    def __init__(self,waypoint_x,waypoint_y):
        self.waypoint_x=waypoint_x
        self.waypoint_y=waypoint_y
        
class Accelerometer():
    def __init__(self,acceleration_x,acceleration_y,acceleration_z):
        self.acceleration_x=acceleration_x
        self.acceleration_y=acceleration_y
        self.acceleration_z=acceleration_z

class User():
    def __init__(self,index,start_time,end_time,waypoints,accelerometer):
        self.index=index
        self.start_time=start_time
        self.end_time=end_time
        self.waypoints=waypoints
        self.accelerometer=accelerometer
    def duration(self):
        end=dt.fromtimestamp(self.end_time/1000)
        start=dt.fromtimestamp(self.start_time/1000)
        duration=end-start
        return duration
    def print_waypoints(self):
        print("\nWaypoints of User ",self.index,":\n") 
        print("\t","%-20s"%"Waypoint X","%-20s"%"Waypoint Y")
        for i in range(len(self.waypoints)):
            print("\t","%-20f"%self.waypoints[i].waypoint_x,
                  "%-20f"%self.waypoints[i].waypoint_y)
        print("\n")
    def list_waypoints(self):
        list_1=[]
        list_2=[]
        for i in range(len(self.waypoints)):
            list_1.append(self.waypoints[i].waypoint_x)
            list_2.append(self.waypoints[i].waypoint_y)
        return list_1,list_2
    def print_acceleration(self):
        print("\nAcceleration of User ",self.index,":\n") 
        print("\t","%-20s"%"Acceleration X","%-20s"%"Acceleration Y",
              "%-20s"%"Acceleration Z")
        for i in range(len(self.accelerometer)):
            print("\t","%-20f"%self.accelerometer[i].acceleration_x,
                  "%-20f"%self.accelerometer[i].acceleration_y,
                  "%-20f"%self.accelerometer[i].acceleration_z)
        print("\n")    
    def list_acceleration(self):
        list_1=[]
        list_2=[]
        list_3=[]
        for i in range(len(self.accelerometer)):
            list_1.append(self.accelerometer[i].acceleration_x)
            list_2.append(self.accelerometer[i].acceleration_y)
            list_3.append(self.accelerometer[i].acceleration_z)
        return list_1,list_2,list_3          

#Files            
input_file='trial_copy.txt'     
info_file='trial_info.json'

# max_col=0
# with open(input_file,'r') as f:
#     for row in f:
#         row_list=(list(row.split("\t")))
#         length=len(row_list)
#         if length>max_col: #Find max number of columns
#             max_col=length

new_list=[]
max_col=10 #Determined maximum number of columns
with open(input_file,'r') as f:
    for row in f:
        row_list=(list(row.split("\t")))
        length=len(row_list)
        row_list[-1]=row_list[-1][:-1] #Remove new line
        if length<max_col:
            for i in range(max_col-length):
                row_list.append('0')
        new_list.append(row_list)
        
#Search data within list
waypoints=[]
accelerometer=[]
for i in range(len(new_list)):
    if new_list[i][1]=="TYPE_WAYPOINT":
        waypoints.append(WayPoints(float(new_list[i][2]), 
                                   float(new_list[i][3])))
    elif new_list[i][1]=="TYPE_ACCELEROMETER":
        accelerometer.append(Accelerometer(float(new_list[i][2]),
                                           float(new_list[i][3]),
                                           float(new_list[i][4])))
#Obtain starting time and ending time        
u1=User(1,int(new_list[0][1][10:]),           #Starting time
        int(new_list[-1][1][8:]),           #Ending time
        waypoints,accelerometer)

#Printing
print("\nDuration used by User 1 is ",u1.duration())  #Print user 1 duration
u1.print_waypoints()


#Visualise waypoints on map
with open(info_file) as f: #Read floor.json
  mapdict = json.load(f)

map_height=mapdict['map_info']['height'] 
map_width=mapdict['map_info']['width']

#Plot map and waypoints
img = plt.imread("trial_map.png")
fig,ax = plt.subplots()
ax.imshow(img,extent=[0, map_width, 0, map_height])
u1_x_waypoints, u1_y_waypoints=u1.list_waypoints()
plt.plot(u1_x_waypoints, u1_y_waypoints,'ro--', linewidth=0.5, markersize=2)
plt.show()

#Plot acceleration
plt.figure(1)
plt.subplot(311)
u1_acc_x,u1_acc_y,u1_acc_z=u1.list_acceleration()
vector_x=[*range(0,len(u1_acc_x))]
plt.plot(vector_x, u1_acc_x, c = "k")
plt.ylabel('Acceleration X')
plt.xlabel('Index')
plt.title("Graph of acceleration X against index")

plt.subplot(312)
plt.plot(vector_x, u1_acc_y, c = "r")
plt.ylabel('Acceleration Y')
plt.xlabel('Index')
plt.title("Graph of acceleration Y against index")

plt.subplot(313)
plt.plot(vector_x, u1_acc_z, c = "b")
plt.ylabel('Acceleration Z')
plt.xlabel('Index')
plt.title("Graph of acceleration Z against index")