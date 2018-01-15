#### Function that check if rows of a .csv file have the same number of items than number of column in the first line (header)
### If rows's lenght are identical, the function return 0. If not, it return a list containing, for row that failed, the value of the first column
# 'csvfile' wait for the complete path (string) to the csvfile to be checked 
# 'separator' wait for the character used as separator in the .csv file (string) 

def check_lenght_row(csvfile,separator):
    listoffailedcat=[]
    afile=open(outfile,'r')
    header=afile.next()
    nb_item_control=len(header.split(separator))
    for row in afile:
        row_items=row.split(";")
        if len(row_items) != nb_item_control:
            listoffailedcat.append(row_items[0]) 
    if len(listoffailedcat)>0:
        return listoffailedcat
    else:
        return 0