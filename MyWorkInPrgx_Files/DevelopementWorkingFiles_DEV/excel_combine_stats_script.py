#Merging multiple csv files into separate sheets under one workbook.
#Please make sure all the packages are installed before executing the code.
#Update the path with forward slash(:/*)
from pandas import ExcelWriter
import glob
import os
import pandas as pd
import shutil

path = "Y:/LOL/Catchup/SAP_POS/"
root = os.listdir(path)
for i in range(len(root)):
    rootdir = path + '/' + root[i]
    trunk = os.listdir(rootdir)
    for j in range(len(trunk)):
        trunkdir = rootdir + '/' + trunk[j]
        stem = os.listdir(trunkdir)
        for k in range(len(stem)):
            stemdir = trunkdir + '/' + stem[k]
            leaf = os.listdir(stemdir)
            for l in range(len(leaf)):
                shutil.copy(stemdir + '/' + leaf[l], trunkdir)
            
        csv_files = glob.glob(os.path.join(trunkdir, "*.csv"))
        write = pd.ExcelWriter(trunkdir + '/Combine_Stats.xlsx' , engine='xlsxwriter')
        for f in csv_files:
            #print(f)
            df = pd.read_csv(f)
            sheet_name=os.path.basename(f)
            df.to_excel(write, sheet_name[17:-4])
        write.save()
print("***Combine Stats Generated***")
