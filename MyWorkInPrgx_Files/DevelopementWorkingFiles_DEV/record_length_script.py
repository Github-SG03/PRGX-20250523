f = open("abc.txt","r")
f1 = open("out.txt","w")
d = {}
while f:
    str = f.readline()
    if str == '':
        break
    elif "originallength" in str:
        print(str)
        key, value = str.lstrip()[1:15], str.lstrip()[17:]
        print(value)
        d.setdefault(key,0)
        d[key] = d[key] + int(value)
    elif "fieldname" in str:
        print(str.lstrip())
        #pass
    elif "PIC" in str:
        print(str)
    else:
        pass

##while f:
##    str = f.readline()
##    if str == '':
##        break
##    if "fieldname" in str:
##        print(str)
##        f1.write(str)
##    elif "fieldname" in str:
##        #print(str.lstrip())
##        pass
##f1.close()
##    
print(d)
