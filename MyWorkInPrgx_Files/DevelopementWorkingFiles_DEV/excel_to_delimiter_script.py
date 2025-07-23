
import xlrd
import csv
import os, os.path, re,unicodedata,sys
path = 'S:\\DS_Talend\\vnair01\\Excel To Tab'
myfiles = os.listdir(path)
delimeter=','






for f in myfiles:
    
    file_name, file_extension = os.path.splitext(f)
    generated_output_file = file_name
    print("file_extension=",file_extension)
    print("generated_output_file=",generated_output_file + ".txt")

    
    if file_extension in ('.xls','.xlsx','.xlsb'):

        
        input_file = os.path.join(path, f)
        output_file = os.path.join(path, generated_output_file)
        print("here")
#path="\\\\ATL20DS1CDAAS03\\Data\\Client_Data\\ysharm01\\excel\\kro_kro0127_2020-04-03_0918_Week of 03.30.2020 Credit and Rebill.xlsx"
#output_file='\\\\ATL20DS1CDAAS03\\Data\\Client_Data\\ysharm01\\jom'

        #file = pd.read_excel(input_file)


        #file.to_csv(output_file,
             #sep=delimeter)

 
        with xlrd.open_workbook(input_file) as wb:
            sh = wb.sheet_by_index(0)  # wb.sheet_by_name('sheet_name')
            with open(generated_output_file + '.txt', 'w', newline="") as f:
                col = csv.writer(f)
                for row in range(sh.nrows):
                    col.writerow(sh.row_values(row))
