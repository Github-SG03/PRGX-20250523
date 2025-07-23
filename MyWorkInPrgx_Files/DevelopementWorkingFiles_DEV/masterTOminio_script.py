#to create minio path using master_frt_id
import re


f = open('master_frt_id.txt','r')
f1 = open('minio.txt','w')
print("Task in progres...")
l = list()
while True:
    abc = f.readline()
    if abc not in l:
        l.append(abc)
        f1.write("/cnt-data-ps-payment-tbl/{0}-1/\n".format(abc))
        print(abc)
    elif abc == '':
        f1.close()
        exit()
    else:
        pass
    
f.close()
#f1.close()
print("Task completed!!")
