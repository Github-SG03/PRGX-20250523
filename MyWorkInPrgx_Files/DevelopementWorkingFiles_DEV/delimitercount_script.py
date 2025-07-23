import csv
import os, os.path, re,unicodedata,sys
d='\t'
path='\\\\atl20ds1103as18\\I\\Client_Data\\vparay01\\FED\\Test'
myfiles = os.listdir(path)
for f in myfiles:
    # split the filename and file extension for use in
    # renaming the output file
    file_name, file_extension = os.path.splitext(f)
    generated_output_file = file_name + "_delimitercount" + file_extension
    print("file_extension=",file_extension)
    print("generated_output_file=",generated_output_file)
    #if file_extension in ('.txt'):

        # Declare input and output files, open them,
        # and start working on each line.
    input_file = os.path.join(path, f)
    output_file = os.path.join(path, generated_output_file)



    with open(input_file, 'r') as f1, open(output_file, 'w', newline='') as f2:
        csv_reader = csv.reader(f1,delimiter=d)
        csv_writer = csv.writer(f2)
        for row in csv_reader:
            csv_writer.writerow([len([x for x in row])])
    
    
