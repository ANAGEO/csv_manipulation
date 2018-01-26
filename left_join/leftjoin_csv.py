## Function which execute a left join using individual .csv files.
## This ddddddddddddd
# The argument "indir" wait for a string containing the path to the directory where the individual .csv files are stored.
# The argument "outfile" wait for a string containing the path to the output file to create.
# The argument "overwrite" wait for True/False value allow or not to overwrite existing outfile.
# The argument "pattern" wait for a string containing the pattern of filename to use. Use wildcards is possible (*.csv for all .csv files)

import os,sys,csv
import glob

def atoi(text):
    '''
    Function that return integer if text is digit - Used in 'natural_keys' function
    '''
    return int(text) if text.isdigit() else text


def natural_keys(text):   #Return key to be used for sorting string containing numerical values - Used in 'join_csv' function
    '''
    Trick was found here
    https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    import re  #Import needed library
    return [ atoi(c) for c in re.split('(\d+)', text) ]  #Split the string

def leftjoin_csv(fileList,outfile,separator_in=";",separator_out=";",overwrite=False,pattern=None):
    # Stop execution if outputfile exitst and can not be overwriten
    if os.path.isfile(outfile) and overwrite==False:
        print "File '"+str(outfile)+"' aleady exists and overwrite option is not enabled."
    else:
        if os.path.isfile(outfile) and overwrite==True:  # If outputfile exitst and can be overwriten
            os.remove(outfile)
            print "File '"+str(outfile)+"' has been overwrited."
        if len(fileList)<=1: #Check if there are at least 2 files in the list
            sys.exit("This function require at least two .csv files to be jointed together.")
        # Save all the value in a dictionnary with key corresponding to the first column
        headerdict={}
        valuedict={}
        for f in [open(f) for f in resultfiles]:
            reader=csv.reader(f, delimiter=separator_in)
            for i,row in enumerate(reader):
                key=row[0]
                value=row[1:]
                for v in value:
                    if i==0: # If first line (header)
                        try:
                            headerdict[key].append(v)
                        except:
                            headerdict[key]=[v,]
                    else:
                        try:
                            valuedict[key].append(v)
                        except:
                            valuedict[key]=[v,]
        # Write the dictionnary with header in a the output csv file
        outputcsv=open(outfile,"w")
        writer=csv.writer(outputcsv, delimiter=separator_out)
        # Header
        header_keys=list(headerdict.keys())
        if len(header_keys)>1:
            header_keys.sort(key=natural_keys)
        for key in header_keys:
            row_content=[key]
            [row_content.append(x) for x in headerdict[key]]
            writer.writerow(row_content)
        # Values
        values_keys=list(valuedict.keys())
        if len(values_keys)>1:
            values_keys.sort(key=natural_keys)
        for key in values_keys:
            row_content=[key]
            [row_content.append(x) for x in valuedict[key]]
            writer.writerow(row_content)
        outputcsv.close()
        # Create a .csvt file with type of each column
        csvt=open(outfile+"t","w")
        results=open(outfile,"r")
        header=results.next()
        typecolumn=[]
        typecolumn.append("Integer")
        for columns in header[1:]:
            typecolumn.append("Real")
        csvt.write(separator_out.join(typecolumn))
        csvt.close()
        # Print what happend
        print str(len(fileList))+" individual .csv files were joint together."
#         return headerdict,valuedict

# Define the path
outfile="/home/tais/Téléchargements/csv_manipulation/left_join/test/result.csv"
resultfiles=["/home/tais/Téléchargements/csv_manipulation/left_join/test/a","/home/tais/Téléchargements/csv_manipulation/left_join/test/b","/home/tais/Téléchargements/csv_manipulation/left_join/test/c"]

# Join all result files together in a new .csv file
leftjoin_csv(resultfiles, outfile, separator_in="|", separator_out=";", overwrite=True)



