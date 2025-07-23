import os
import shutil

destination = 'test'
path = "S:/DS_Talend/vnair01/py1/"

#move

##f1 = open("file_list.txt",'r+')
##for i in f1:
##    if '\n' in i:
##        shutil.copy(path + i[:-1], path + destination)
##    else:
##        shutil.copy(path + i, path + destination)

##print("***FILES COPIED TO DESTINATION SUCCESSFULLY***")



#rename

for j in os.listdir(path+destination):
    new_name = ''
    #print(j)
    for k in j:
        if ord(k) == 233:
            new_name += 'e'
        else:
            new_name += k
    print(j)
    os.rename(path+destination+'/'+j,path+destination+'/'+new_name)
    #print(new_name)
print("RENAME COMPLETE")
