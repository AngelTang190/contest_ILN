# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:38:22 2021

@author: ASUS
"""

#Function to print list
def print_list(new_list):
    for i in range(len(new_list)):
        for j in range(max_col):
            print(new_list[i][j],end=" ")
        print("\n")

input_file='trial_copy.txt'     

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
        



