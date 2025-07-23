f= open("cnt_rejects.txt","r+")
f1 = open("cnt_rejects_fixed","w")

#cnt file fixing
#mainly for dataset PS_RECV_IN_SHIP

for line in f:
    if line != '':
        #print('line: ',line)
        ls = line.partition(',N,Q,')
        s1 = str(ls[0])
        
        if ',USD,CAD,' in s1:
            lss1 = s1.partition(',USD,CAD,')
            ss = str(lss1[2])
            ss2 = ss.replace(","," ")
            ss3 = str(lss1[0]) + str(lss1[1]) + ss2
            s3 = ss3 + str(ls[1]) + str(ls[2])
            
        elif ',CAD,CAD,' in s1:
            lss2 = s1.partition(',CAD,CAD,')
            st = str(lss2[2])
            st2 = st.replace(","," ")
            st3 = str(lss2[0]) + str(lss2[1]) + st2
            s3 = st3 + str(ls[1]) + str(ls[2])
            
        else:
            s3 = s1 + str(ls[1]) + str(ls[2])
            
        #print(s3)
        f1.write(s3)
f1.close()
