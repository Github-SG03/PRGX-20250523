import os
import shutil

inputpath = r'\\amer.prgx.com\dataservices\Production\Walmart\Working\US\DL-43525_Layaway_2021-04-2021-07\07rename'
outputpath = r'\\amer.prgx.com\dataservices\Production\Walmart\Working\US\DL-43525_Layaway_2021-04-2021-07\07'
cdmsbatch = 'wal0001'
countrycode = 'US'

# cdmsbatch = 'asd0008'
# countrycode = 'ASD'

for dirpath, dirnames, filenames in os.walk(inputpath):
    for filename in filenames:  
        try:                 
            if filename.lower().endswith('.dat'): 
                filenamewithoutextension = os.path.splitext(filename)[0]
                # MMDDYYYY (E.g A2EFILEIMS11012018.dat)
                #datepart = filenamewithoutextension[-4:] + '-' + filenamewithoutextension[-8:-6] + '-' + filenamewithoutextension[-6:-4]
                
                # YYYY-MM-DD (E.g. CA_PO_DISTR_2018-11-02.dat)
                #datepart = filenamewithoutextension[-10:-6] + '-' + filenamewithoutextension[-5:-3] + '-' + filenamewithoutextension[-2:]
                
                # YYYYMMDD (E.g. MarkDownZero20181106.dat)
                #datepart = filenamewithoutextension[-8:-4] + '-' + filenamewithoutextension[-4:-2] + '-' + filenamewithoutextension[-2:]
                                         
                # MMDDYYYY00000000 (E.g. LAYWAYREPT0213201906391921.DAT)
                datepart = filenamewithoutextension[-12:-8] + '-' + filenamewithoutextension[-16:-14] + '-' + filenamewithoutextension[-14:-12]
				
                # YYYYMMDD NGP-20200201090006_1.zip  
                #datepart = filenamewithoutextension[-16:-12] + '-' + filenamewithoutextension[-12:-10] + '-' + filenamewithoutextension[-10:-8]
                
                #NGP-20181219192315_11.zip
                #datepart = filenamewithoutextension[-17:-13] + '-' + filenamewithoutextension[-13:-11] + '-' + filenamewithoutextension[-11:-9]
                
				# YYYYMMDD NGP-20200201090006.zip 
                #datepart = filenamewithoutextension[-14:-10] + '-' + filenamewithoutextension[-10:-8] + '-' + filenamewithoutextension[-8:-6]
                
                # YYYYMMDD DOTCOMPOS_20190827.dat.gz
                #datepart = filenamewithoutextension[-12:-8] + '-' + filenamewithoutextension[-8:-6] + '-' + filenamewithoutextension[-6:-4]
                
                # YYYYMMDD   Cost_change-20191127070640
                #datepart = filenamewithoutextension[-14:-10] + '-' + filenamewithoutextension[-10:-8] + '-' + filenamewithoutextension[-8:-6]
                
                #Cost_change0505202010                
                #datepart = filenamewithoutextension[-4:0] + '-' + filenamewithoutextension[-8:-6] + '-' + filenamewithoutextension[-6:-4]
                                
                outputfilename = cdmsbatch[0:3] + '_' + cdmsbatch + '_' + datepart + '_1234' + '_' + countrycode + '_' + filename        
                os.rename(os.path.join(inputpath,filename),os.path.join(outputpath,outputfilename)) 
        except Exception as err:
            print('Error renaming file: ' + filename)
					
