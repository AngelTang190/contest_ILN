# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv

input_file='trial_copy.txt'
output_file='new_trial.csv'

with open(input_file, 'r') as in_file, open(output_file, 'w', newline='') as out_file:
    csv_reader = csv.reader(in_file, delimiter='\t')
    writer = csv.writer(out_file)
    writer.writerows(csv_reader)
        
