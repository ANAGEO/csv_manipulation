## Function which create a new .csv file with only specifics rows, according to specified values for the first row (primary key)
# The argument "listofcat" wait for a list of strings containing the value of the first column to be selected in the .csv file.
# The argument "originalcsv" wait for a string containing the path to the .csv file from which selection will be made.
# The argument "outputcsv" wait for a string containing the path to the output .csv file to create.
# The argument "overwrite" wait for True/False value allow or not to overwrite existing outfile.

import os
import tempfile


def selectfromcsv(listofcat,originalcsv,outputcsv,overwrite=False):
    if not listofcat:
        print "WARNING: The list of items to find is empty."
        return
    if os.path.isfile(outputcsv) and overwrite==False:
        print "File '"+str(outputcsv)+"' aleady exists and overwrite option is not enabled."
    else:
        if os.path.isfile(outputcsv) and overwrite==True:
            open(outputcsv,"r").close
            os.remove(outputcsv)
        newfile=open(outputcsv,"a")
        item_queue=list(set(listofcat))
        #print "item in queue are "+" ".join(item_queue)
        newfile.write(open(originalcsv,"r").next())
        countline=1
        for line in open(originalcsv,"r"):
            if len(item_queue)>0:
                current_cat=line[:line.index('|')]
                #print current_cat
                if current_cat in item_queue:
                    #print "writing a line in new csv"
                    newfile.write(line)
                    countline+=1
                    index_queue=item_queue.index(current_cat)
                    del item_queue[index_queue]
            else:
                break
        newfile.close()
        if countline==1:
            print "WARNING: Nothing found"
            os.remove(outputcsv)
        if len(item_queue)>0:
            print "WARNING: item(s) "+",".join(item_queue)+" not found."

        print "Process finished"
        
listofcat=[]
listofcat.append('4426628')
listofcat.append('4251')
listofcat.append('406222')
listofcat.append('708')
listofcat.append('4332758')
listofcat.append('4251835')
listofcat.append('708')
listofcat.append('4')
listofcat.append('4251')
listofcat.append('406222')
listofcat.append('708')
listofcat.append('4332758')
listofcat.append('4251835')
listofcat.append('708')
listofcat.append('4')

originalcsv="C:\\Users\\Admin_ULB\\Desktop\\Temporaire\\test\\TMPcsv2 - Copie.csv"
outputcsv="C:\\Users\\Admin_ULB\\Desktop\\Temporaire\\test\\Test.csv"

selectfromcsv(listofcat,originalcsv,outputcsv,overwrite=True)
