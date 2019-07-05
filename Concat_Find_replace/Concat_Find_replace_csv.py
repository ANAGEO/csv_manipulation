""" Function which concatenate (stack them vertically) several individual .csv files each others. The function allows 
also to replace some values at the same time. Values to replace should be provided in a python dictionary with key=value correspondance.
# 'indir' parameter wait for a string with the path to the repertory to look for individual .csv files
# 'pattern' parameter wait for a string with the pattern of filename to look for (example: "TMP_*.csv")
# 'sep' parameter wait for a string with the delimiter of the .csv file
# 'replacedict' parameter wait for a dictionary containing the unwanted values as keys and the replace string as corresponding value
# 'outputfilename' parameter wait for the name of the outputfile (including extansion but without the complete path)
"""
import os
import glob
import csv

def concat_findreplace(indir,pattern,sep,replacedict,outputfilename):
    # Initialise some variables
    messagetoprint=None
    returnmessage=None
    countdict={}
    for k in replacedict:
        countdict[k]=0
    # Change the working directory
    os.chdir(indir) 
    # Get a list with file in the current directory corresponding to a specific pattern
    fileList=None
    fileList=glob.glob(pattern)
    # Print
    messagetoprint="Going to concatenate "+str(len(fileList))+" .csv files together and replace unwanted values."
    #print (messagetoprint)
    returnmessage=messagetoprint
    # Create a new file 
    outfile=os.path.join(indir, outputfilename)
    writercsvSubset = open(outfile, 'wb')
    writercsv=csv.writer(writercsvSubset,delimiter=sep)
    # Concatenate individuals files and replace unwanted values
    for indivfile in fileList:
        with open(indivfile) as readercsvSubset:
            readercsv=csv.reader(readercsvSubset, delimiter=sep)
            if indivfile!=fileList[0]:
                readercsv.next()
            count=0
            for row in readercsv:
                newline=[]
                for i, x in enumerate(row):
                    if x in replacedict:
                        newline.append(replacedict[x])
                        countdict[x]+=1
                    else:
                        newline.append(row[i])
                writercsv.writerow(newline)
        # Close the current input file
        readercsvSubset.close()
    # Close the outputfile
    writercsvSubset.close()
    # Count number of changes
    countchange=0
    for k in countdict:
        countchange+=countdict[k]
    # Print
    if countchange>0:
        messagetoprint="\n"
        returnmessage+=messagetoprint
        messagetoprint="Values have been changed:"+"\n"
        #print (messagetoprint)
        returnmessage+=messagetoprint
        for k in replacedict:
            if countdict[k]>0:
                messagetoprint=str(countdict[k])+" '"+k+"' value(s) replaced by '"+replacedict[k]+"'\n"
                #print (messagetoprint)
                returnmessage+=messagetoprint
    else:
        messagetoprint="Nothing changed. No unwanted values found !"
        #print (messagetoprint)
        returnmessage+=messagetoprint
    # Return
    return returnmessage[:-1]
