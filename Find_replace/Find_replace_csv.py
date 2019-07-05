## Function which find specific value and replace it by another. It can also just count the number of values founded.
# Either a new .csv file is created with the updated values or the replacement is made inside the current .csv file a new .csv file with only specifics rows, according to specified values for the first row (primary key)
# The argument "findreplacedict" wait for a dictionary with find value as key and the replacing text as value.
# The argument "originalcsv" wait for a string containing the path to the .csv file from which selection will be made.
# The **argument "outputcsv" is optional and wait for a string containing the path to the output .csv file to create. If this parameter is not passed, it is considered the user want inplace replacement.
# The **argument "overwrite" wait for True/False value allow or not to overwrite existing outfile.
# The **argument "justcount" wait for True/False value indicate if the user only want the number of "find" string found.
# The **argument "sep" wait for string value indicating the delimiter of the .csv file. By default "sep"=';'.
# The **argument "findreplacedict" wait for a dictionary with find value indicating the delimiter of the .csv file. By default "sep"=';'.

import os
import csv
import sys
import tempfile
import shutil


def findreplace(findreplacedict,originalcsv,*args,**kwargs):
    # Initialise a empty string for print to return at the end
    message=""

    # Check if the originalcsv exists and is well .csv file (check extension)
    if not os.path.isfile(originalcsv):
        toprint="WARNING: original file does not exists."
        print toprint
        message+=toprint+"\n"
        return message[:-1]
    elif originalcsv[-4:]!='.csv':
        toprint="WARNING: original file extension is not CSV."
        print toprint
        message+=toprint+"\n"
        return message[:-1]
    
    if 'justcount' not in kwargs:
        kwargs['justcount']=False
    else:
        if type(kwargs['justcount']) is not bool:
            toprint="WARNING: argument 'justcount' should be a boolean"
            print toprint
            message+=toprint+"\n"
            return message[:-1]
   
    if 'overwrite' not in kwargs:
        kwargs['overwrite']=False
    else:
        if type(kwargs['overwrite']) is not bool:
            toprint="WARNING: argument 'overwrite' should be a boolean"
            print toprint
            message+=toprint+"\n"
            return message[:-1]

    if 'sep' not in kwargs:
        kwargs['sep']=';'
    else:
        if type(kwargs['sep']) is not str:
            toprint="WARNING: argument 'sep' should be a string"
            print toprint
            message+=toprint+"\n"
            return message[:-1]

    if kwargs['justcount']==False: 
        # Check if 'outputcsv' is in arguments, if it exists and if overwrite is allowed.
        if 'outputcsv' in kwargs :  
            outputcsv=kwargs['outputcsv']   #Save path to outputcsv
            if os.path.isfile(outputcsv) and kwargs['overwrite']==False: #If outputfile exists and overwrite not allowed
                toprint="File '"+str(outputcsv)+"' aleady exists and overwrite option is not enabled."
                print toprint
                message+=toprint+"\n"
                return message[:-1]
        
        # Check if 'outputcsv' is not in arguments (thus original file must be overwrited) and overwrite is not allowed.
        if 'outputcsv' not in kwargs and kwargs['overwrite']==False:  
            toprint="As no 'outputfile' argument was defined, the original data will be overwrite. Please change the 'overwrite' argument's value to True"
            print toprint
            message+=toprint+"\n"
            return message[:-1]

    # Create a reader for the original file
    readercsvSubset=open(originalcsv,"rb")
    readercsv=csv.reader(readercsvSubset, delimiter=kwargs['sep'])
    
    # Create a dictionary for counting items found
    itemfound={}      
    for k in findreplacedict.keys():
        itemfound[k]=0
    
    if kwargs['justcount']==False:
        # Create temporary file for work
        tmpfile=tempfile.mkstemp(suffix=".csv")
        # Create a writer for the tmpfile
        writercsvSubset=open(tmpfile[1],"wb")
        writercsv=csv.writer(writercsvSubset,delimiter=kwargs['sep'])
        # Write the header of the original file
        header=readercsv.next()
        writercsv.writerow(header)      

    # Loop on row of original file
    for row in readercsv:
        newline=[]  #Initialise a empty list to be completed
        #Loop on column of the current row
        for i, x in enumerate(row):
            if x not in findreplacedict: #the value is not the one wanted
                 #if user does not want just to have the count of item found
                    newline.append(row[i]) #append the original value to the 'newline' list                  
            else:   #the value is the one wanted
                if kwargs['justcount']==False:
                    newline.append(findreplacedict[x]) #append the replacing value to the 'newline' list                       
                itemfound[x]+=1  #increment the number of item found     
        if kwargs['justcount']==False:
            writercsv.writerow(newline) #at the end of the row, write the 'newline' in the tmpfile                 
    
    # Close the reader
    readercsvSubset.close()
    
    # Sum of itemfound
    countfound=0
    for k in findreplacedict.keys():
        countfound+=itemfound[k]
    
    # If nothing found, print a message and ends the script 
    if countfound==0:
        toprint="Nothing found. No items '"+",".join(findreplacedict.keys())+"' in the file. Nothing happens."
        print toprint
        message+=toprint+"\n"
        return message[:-1]    
    
    # Check where to save modified data (still in tmpfile)   
    if kwargs['justcount']==False:
        if 'outputcsv' not in kwargs: #If 'outputcsv' not passed in argument, copy the tmpfile in place of the original path
            os.remove(originalcsv)
            shutil.copy2(tmpfile[1], originalcsv)
            os.close(tmpfile[0])
            toprint="Items replaced inplace"
            print toprint
            message+=toprint+"\n"
        else: #If 'outputcsv' passed in argument, copy the tmpfile on the output path give as argument
            if os.path.isfile(outputcsv) and kwargs['overwrite']==True:  #If outputfile exists and overwrite allowed
                os.remove(outputcsv)
                toprint="Output file already exist and will be overwrited"
                print toprint
                message+=toprint+"\n"
            shutil.copy2(tmpfile[1], outputcsv)
            os.close(tmpfile[0])
            toprint="Items replaced from the original data and saved on "+str(outputcsv)
            print toprint
            message+=toprint+"\n"

    # Print and return message
    toprint=""
    for k in findreplacedict.keys():
        toprint+="Number of items '"+str(k)+"' found = "+str(itemfound[k])+"\n"
    toprint+="Total = "+str(countfound)
    print toprint
    message+=toprint+"\n"
    return message[:-1]
