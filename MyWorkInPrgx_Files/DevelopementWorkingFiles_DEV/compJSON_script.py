f = open("abc.txt","r")
while f:
    str = f.readline()
    if str == '':
        break
    if "fieldname" in str:
        print(str)
    else:
        pass
