import os
#opening the existing file or creating a new file in "write" mode
f = open("LOL.txt","w")

#getting list of file names
l1 = os.listdir('V:/lol/DL-49295/p2/delimited')

final = list()

#to skip the file names which are stored in 1st list i.e 'l1'(works as like operator)
for i in  range(len(l1)):
    if 'ca_capture' in l1[i]:
        continue
    else:
        final.append(l1[i])

##for i in  range(len(l1)):
##    if 'Metro_Ontario.zip' in l1[i]:
##        final.append(l1[i])
##    else:
##        continue

op1 = " "

#converting the list into string and dtoring the data into file
#f.write('***FED***')
f.write(op1.join(final))


f.close()

