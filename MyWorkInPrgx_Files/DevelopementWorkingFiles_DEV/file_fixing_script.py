import re

f= open("cnt_PS_VENDOR_LOC_20191205_99867_1","r+")
f1 = open("cnt_PS_VENDOR_LOC_20191205_99867_1_output","w")

##for line in f:
##    if line != '':
##        print(re.sub(',',' ',line,count=1))

#reg = re.compile('(.*),(.*),\s*900|(.*),(.*),(.*),\s*900')
#reg1 = re.compile('')
for line in f:
    if line != '':
        #print('line: ',line)
        ls = line.partition(',,,,,,D,D,')
        s1 = str(ls[2])
        s2 = s1.replace(","," ")
        #print(s2)
        s3 = str(ls[0]) + str(ls[1]) + s2
        #print(s3)
        f1.write(s3)
f1.close()
        #s = str(ls[0]) + str(ls[1])
        #print('string',s)
        #l1 = reg.search(line)
##        if l1 == None:
##            pass
##        else:
##            print(l1.group())
