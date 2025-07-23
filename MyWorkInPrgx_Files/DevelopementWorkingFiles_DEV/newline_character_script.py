#fixing newline character
#update the path and pattern accordingly, make sure to keep "[a-z,A-Z,0-9,_,^]+" as it is in pattern.

import os
import re

path = "T:\\CNT catchup\\part9\\CLAIM_SCAN_NRG_SUMSUPFCT\\decomp\\fix"

count = 0
 
for fname in os.listdir(path):
    count += 1
    with open(os.path.join(path,fname),"r") as f:
        print(fname)
        for line in f.readlines():
            
            if line != '':
                store = line.replace("UNIX newline","\n")

                    
    with open(os.path.join(path,fname),"w") as f:
        for line in store:
            f.write(line)
            
    f.close()
    print("{0} files completed".format(count))
    
    
print("Task Complete!!")



