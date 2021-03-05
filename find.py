import os
import csv

start_dir = "D:\OneDrive\OneDrive - Monash University\indoor-location-navigation\B1-Copy"  # path of the directory to start searching
for path, dirs, files in os.walk(start_dir):  # os.walk returns a generator, that creates a tuple of values (current_path, directories in current_path, files in current_path)
    for name in files:  # loop through all the available files
        if name.endswith(".txt"):  # check if the file is a txt file
            filepath = os.path.join(path, name)  # filepath to the txt file
            filename = os.path.splitext(filepath)[0]  # remove the filename extension of the file
            write_filename = filename + ".csv"  # new filename to write to
            with open(filepath, "r") as in_file, open(write_filename, "w", newline='') as out_file:  # convert the txt file to csv file
                csv_reader = csv.reader(in_file, delimiter='\t')
                writer = csv.writer(out_file)
                writer.writerows(csv_reader)
