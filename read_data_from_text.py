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

class User():
    def __init__(self,index,start_time,end_time,waypoints):
        self.index=index
        self.start_time=start_time
        self.end_time=end_time
        self.waypoints=waypoints
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
    def list_waypoints_x(self):
        list=[]
        for i in range(len(self.waypoints)):
            list.append(self.waypoints[i].waypoint_x)
        return list
    def list_waypoints_y(self):
        list=[]
        for i in range(len(self.waypoints)):
            list.append(self.waypoints[i].waypoint_y)
        return list            
            
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
for i in range(len(new_list)):
    if new_list[i][1]=="TYPE_WAYPOINT":
        waypoints.append(WayPoints(float(new_list[i][2]), 
                                   float(new_list[i][3])))
        
#Obtain starting time and ending time        
u1=User(1,int(new_list[0][1][10:]),           #Starting time
        int(new_list[-1][1][8:]),           #Ending time
        waypoints)

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
plt.plot(u1.list_waypoints_x(), u1.list_waypoints_y(), color="red")
plt.show()