""" 
This function allows to create a new CSV file with only some columns extracted from an existing CSV file. 
It allows multiple ways of extraction: 
1) first column and several specific columns whose indexes are provided in 'indexcol'. 
2) first column and the X last columns according to the value provided in 'nb_col_from_end' 
3) first column, several specific columns ('indexcol') and the X last columns ('nb_col_from_end') 

Parameters:
- If provided, 'indexcol' should be a list
- If provided, 'nb_col_from_end' should be an integer

TODOs:
- For the moment, the function only allows to specify columns either by index or by number of columsn from the end (all last X columns). It could be great to allows specification using the name of the columns.
"""

import subprocess, sys

def CutCsv(input_csv, indexcol=False, nb_col_from_end=False):   
    # Check if at least one option is asked   
    if not indexcol and not nb_col_from_end:
        return "ERROR: At least parameter 'indexcol' or 'nb_col_from_end' should be provided"
        sys.exit()
    # Create a new .csv with only the first and the X lasts columns (X = nb_col_from_end. By default, first and last only)
    path, ext = os.path.splitext(input_csv)
    cut_csv = "%s_cut%s"%(path,ext)
    f = open(cut_csv, "w")
    if nb_col_from_end:
        # Get number of colums in the .csv
        p1 = subprocess.Popen(("head -1 %s"%input_csv).split(), stdout=subprocess.PIPE)
        p2 = subprocess.Popen(("tr ',' '\\n'").split(), stdin=p1.stdout, stdout=subprocess.PIPE)
        p3 = subprocess.Popen(("wc -l").split(), stdin=p2.stdout, stdout=subprocess.PIPE)
        nb_columns = int(p3.communicate()[0])
        index_start = nb_columns-nb_col_from_end
    #Extract first and several specific columns whose indexes are provided in 'indexcol' 
    if indexcol and not nb_col_from_end:
        cut_process =  subprocess.Popen(("cut -d, -f1,%s %s"%(','.join(indexcol),input_csv)).split(), stdout=f)
        cut_process.wait()
    #Extract first and the X last columns according to the value provided in 'nb_col_from_end' 
    if nb_col_from_end and not indexcol:
        cut_process =  subprocess.Popen(("cut -d, -f1,%s-%s %s"%(index_start,nb_columns,input_csv)).split(), stdout=f)
        cut_process.wait()
    #Extract first column, several specific columns ('indexcol') and the X last columns ('nb_col_from_end') 
    if nb_col_from_end and indexcol:
        cut_process =  subprocess.Popen(("cut -d, -f1,%s,%s-%s %s"%(','.join(indexcol),index_start,nb_columns,input_csv)).split(), stdout=f)
        cut_process.wait()
    f.close()
    return cut_csv
