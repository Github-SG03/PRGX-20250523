# file classifier update query

def classifier(dataset):
    file_pattern = 'lnb_lnb%'+dataset+'%.csv.zip%'+dataset+'%.csv'
    query = 'update file_classifier set file_pattern = \''+file_pattern+'\' where fc_id = \n\n'
    f1.write(query)

f = open('abc.txt','r')
f1 = open('update_query.txt','w')

while True:
    ds = f.readline()
    if ds == '':
        break
    classifier(ds)
f1.close()
f.close()
    


    
