#replacing delimiter

import os

path = "T:\\CNT catchup\\FGL_Franhise\\cnt_cnt0028_2021-01-14_1002_vendpackingslipTRANS\\fix"

##for fname in os.listdir(path):
##    with open(os.path.join(path,fname),"r",encoding = "utf-8") as f:
##        print(fname)
##        newlines = []
##        for line in f.readlines():
##            if line != '':
##                newlines.append(line.replace("|","╦"))
##                
##    with open(os.path.join(path,fname),"w",encoding = "utf-8") as f:
##        for line in newlines:
##            f.write(line)
##            
##    f.close()
##    
##print("Task Complete!!")

for fname in os.listdir(path):
    f1 = open(os.path.join(path,fname),"r",encoding = "utf-8")
    data = f1.read()
    data = data.replace("|",'"\u2566"')
    f1.close()

    f2 = open(os.path.join(path,"abc.txt"),"w",encoding = "utf-8")
    f2.write(data)
    f2.close()

print("task complete")

