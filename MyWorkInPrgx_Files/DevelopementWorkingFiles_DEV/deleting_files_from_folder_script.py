import os
import re

#getting list of file names
loc = '//amer.prgx.com/dataservices/Production/Walmart/Working/US/DL-36752_NEXGEN_2018-12_2020-03/2019-12/p2'
l1 = os.listdir(loc)

final = list()

#to skip the file names which are stored in 1st list i.e 'l1'(works as like operator)
for i in  range(len(l1)):
    if 'ps_finance_tables' in l1[i]:
        continue
    else:
        final.append(l1[i])
#regex = re.compile(r'^md',re.I)
ls = ['md_items_aggr.txt','md_scenarios.txt']
for i in final:
    loc1 = loc+'/'+i
    li = os.listdir(loc1)
    for j in li:
        if j in ls:
            print(j)
            path = loc1+'/'+j
            os.remove(path)
print("Complete")

##for i in final:
##    loc1 = loc+'/'+i
##    li = os.listdir(loc1)
##    for j in li:
##        if regex.search(j) != '':
##            mo = regex.search(j)
##            print(mo)
##            if mo.group() != '':
##                print(j)
##                path = loc1+'/'+j
##                os.remove(path)
##print("Complete")

