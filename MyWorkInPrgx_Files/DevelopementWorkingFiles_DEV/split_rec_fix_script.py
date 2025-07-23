#fixing split records
#update the path and pattern accordingly, make sure to keep "[a-z,A-Z,0-9,_,^]+" as it is in pattern.

import os
import re

path = "D:\\MCA\\PY\\rejects"

pattern = re.compile(r'\^Expected 134 fields but found 95[a-z,A-Z,0-9,_,^]+')

for fname in os.listdir(path):
    with open(os.path.join(path,fname),"r") as f:
        print(fname)
        newlines = []
        for line in f.readlines():
            
            if line != '':
                find = pattern.search(line)
                
                if find != None:
                    #print(find.group())
                    newlines.append(line.replace(find.group(),"  "))
                    
                elif '^prgxerrors^prgxfiletag^' in line:
                    #print("in elif")
                    newlines.insert(0,line)
                    
                else:
                    if len(newlines) == 0:
                        print("Inside if")
                        
                    else:
                        #print("Inside else")
                        line1 = newlines[-1]
                        newlines[-1] = line1.replace("  \n","") + line
                        #newlines[-1] += line                 
                    
    with open(os.path.join(path,fname),"w") as f:
        for line in newlines:
            f.write(line)
            
    f.close()
    
print("Task Complete!!")



