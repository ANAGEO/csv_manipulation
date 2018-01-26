## Function which execute a left join using individual .csv files.
## This ddddddddddddd
# The argument "indir" wait for a string containing the path to the directory where the individual .csv files are stored.
# The argument "outfile" wait for a string containing the path to the output file to create.
# The argument "overwrite" wait for True/False value allow or not to overwrite existing outfile.
# The argument "pattern" wait for a string containing the pattern of filename to use. Use wildcards is possible (*.csv for all .csv files)


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

def leftjoin_2csv(file1,file2,separator=";"):
    import tempfile,csv,os
    header_list=[]
    file1_values_dict={}
    file2_values_dict={}
    reader1=csv.reader(open(file1), delimiter=separator) #Csv reader for file 1
    reader2=csv.reader(open(file2), delimiter=separator) #Csv reader for file 2
    # Make a list of headers
    header_list1=[ x for x in reader1.next()]
    header_list2=[ x for x in reader2.next()[1:]]
    # Make a list of unique IDs from the first and second table
    id_list=[ row[0] for row in reader1]
    [id_list.append(row[0]) for row in reader2]
    id_list=list(set(id_list))
    id_list.sort(key=natural_keys)
    # Build dictionnary for values of file 1
    reader1=csv.reader(open(file1), delimiter=separator)
    reader1.next()
    values_dict1={rows[0]:rows[1:] for rows in reader1}
    # Build dictionnary for values of file 2
    reader2=csv.reader(open(file2), delimiter=separator)
    reader2.next()
    values_dict2={rows[0]:rows[1:] for rows in reader2}
    # Built new content
    new_content=[]
    new_header=header_list1+header_list2
    new_content.append(new_header)
    for key in id_list:
        new_row=[key]
        try:
            [new_row.append(value) for value in values_dict1[key]]
        except:
            [new_row.append("NULL") for x in header_list1[1:]]
        try:
            [new_row.append(value) for value in values_dict2[key]]
        except:
            [new_row.append("NULL") for x in header_list2]
        new_content.append(new_row)
    #Return the result
    outfile=os.path.join(tempfile.gettempdir(),"temp")
    writer=csv.writer(open(outfile,"w"), delimiter=separator)
    writer.writerows(new_content) #Write multiples rows in the file
    return outfile

def leftjoin_multiplecsv(fileList,outfile,separator=";",overwrite=False):
    import os, sys, shutil
    # Stop execution if outputfile exitst and can not be overwriten
    if os.path.isfile(outfile) and overwrite==False:
        print "File '%s' aleady exists and overwrite option is not enabled."%outfile
    else:
        if os.path.isfile(outfile) and overwrite==True:  # If outputfile exitst and can be overwriten
            os.remove(outfile)
            print "File '%s' has been overwrited."%outfile
        nbfile=len(fileList)
        if nbfile<=1: #Check if there are at least 2 files in the list
            sys.exit("This function require at least two .csv files to be jointed together.")
        # Left join on the two first files
        file1=fileList.pop(0)
        file2=fileList.pop(0)
        tmp_file=leftjoin_2csv(file1,file2,separator=separator)
        # Left join on the rest of the files in the list
        while len(fileList)>0:
            file2=fileList.pop(0)
            tmp_file=leftjoin_2csv(tmp_file,file2,separator=separator)
        #Copy the temporary file to the desired output path
        shutil.copy2(tmp_file,outfile)
        # Print what happend
        print "%s individual .csv files were joint together."%nbfile

def create_csvt(csv_file,separator=";",first_col_type="Integer",rest_type="Real"):
    import csv
    writer=csv.writer(open(csv_file+"t","w"),delimiter=separator)
    reader=csv.reader(open(csv_file,"r"),delimiter=separator)
    header=reader.next()
    typecolumn=[]
    typecolumn.append(first_col_type)
    for columns in header[1:]:
        typecolumn.append(rest_type)
    writer.writerow(typecolumn)

# Test
test_folder=os.path.join(os.path.dirname(sys.argv[0]),"test")
outfile=os.path.join(test_folder,"result.csv")
fileList=[]
fileList.append(os.path.join(test_folder,"a"))
fileList.append(os.path.join(test_folder,"b"))
fileList.append(os.path.join(test_folder,"c"))
fileList.append(os.path.join(test_folder,"d"))
fileList.append(os.path.join(test_folder,"e"))
fileList.append(os.path.join(test_folder,"f"))

leftjoin_multiplecsv(fileList,outfile,separator="|",overwrite=True)
create_csvt(outfile,separator="|",first_col_type="Integer",rest_type="Real")