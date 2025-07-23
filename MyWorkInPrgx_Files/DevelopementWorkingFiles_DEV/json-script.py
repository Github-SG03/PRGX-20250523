import os
import json

path = r'C:\Users\mdegwe01.APAC\Desktop\MultiSchemaToSingleSchema\Updated'

for subdir, dirs, files in os.walk(path):
    for filename in files:        
        inputdict = json.load(open(os.path.join(path,filename),encoding="utf-8"))
        outputlayouts = []        
        defaultdict = {}
        clientname = filename[0:3]
        for key in inputdict.keys():
            if key != 'fields':
                if key != 'filetype':
                    defaultdict[key] = inputdict[key]
                else:
                    defaultdict[key] = 'DELIMITED'
            else:
                for layout in inputdict[key]:
                    outputlayout = {}
                    updatedfields = []
                    finaldicttowrite = {}
                    outputfilename = ""
                    if 'outputfileconvention' in layout:
                        outputfilename = clientname + "_" + layout['outputfileconvention']
                    if 'fields' in layout:
                        for field in layout['fields']:
                            updatedfield = {}
                            for key in field.keys():
                                if key != 'startposition':
                                    updatedfield[key] = field[key]
                            updatedfields.append(updatedfield)
                    outputlayout['fields'] = updatedfields
                    finaldicttowrite = {**defaultdict, **outputlayout}
                    with open(os.path.join(path, outputfilename + '.layout.json'), 'w') as outfile:        
                        json.dump(finaldicttowrite, outfile, indent=4)
                        outfile.write("\n")
                    