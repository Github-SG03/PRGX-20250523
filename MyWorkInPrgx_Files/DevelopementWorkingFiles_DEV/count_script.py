#to check whether the record length is equal to total field size
import re

#opeing json file and reading the field with key 'size'
f = open('FED_WKLY.layout.json','r')
f1 = open('count.txt','w')

while True:
    abc = f.readline()
    if 'size' in abc:
        f1.write(abc)
    if abc == '':
        break
f.close()
f1.close()

# approx size of each record
f1 = open('count.txt','r')
count = 0
number = re.compile(r'(\d){1,3}')       #'r' indicates raw string

while True:
    ab = f1.readline()
    if ab == '':
        print("Record length:",count)
        break
    mo = number.search(ab)
    i = int(mo.group())
    count += i

