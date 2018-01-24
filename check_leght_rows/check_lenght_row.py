#### Function that check if rows of a .csv file have the same number of items than number of column in the first line (header)
### If rows's lenght are identical, the function return 0. If not, it return a list containing the index number of row(s) that failed
### The index is starting with value 1 for the first line of data (the header row is indexed 0)
# 'csvfile' wait for the complete path (string) to the csvfile to be checked
# 'separator' wait for the character used as separator in the .csv file (string)
# 'allowemptycell' wait for a boolean value (True, False) depending if a empty cell should not be considered as a problem in the file

def check_lenght_row(csvfile,separator,allowemptycell=True):
    listofunequalrow=[]
    afile=open(csvfile,'r')
    header=afile.next()  # Save header row and go to the next one
    nb_item_control=len(header.split(separator))
    for x,row in enumerate(afile,1):    # Start counting at "1" because header is already skipped
        row_items=row.split(separator)
        if len(row_items) != nb_item_control: # Check it number of items is identical than the number of items in the header
            listofunequalrow.append(x)
        if not allowemptycell:
            if "" in row_items:
                listofunequalrow.append(x)
    listofunequalrow=list(set(listofunequalrow))   # Recreate a list with uniques values from the original list
    if len(listofunequalrow)>0:
        return listofunequalrow  # Return a list of indexes for line whose length is not equal to the header
    else:
        return 0

# Test
same_lenght="/home/tais/Téléchargements/csv_manipulation/check_leght_rows/testing_files/test_file_equals.csv"
different_lenght_1="/home/tais/Téléchargements/csv_manipulation/check_leght_rows/testing_files/test_file_nonequals_1.csv"
different_lenght_2="/home/tais/Téléchargements/csv_manipulation/check_leght_rows/testing_files/test_file_nonequals_2.csv"
different_lenght_3="/home/tais/Téléchargements/csv_manipulation/check_leght_rows/testing_files/test_file_nonequals_3.csv"

print check_lenght_row(same_lenght,";")
print check_lenght_row(different_lenght_1,";")
print check_lenght_row(different_lenght_2,";")
print check_lenght_row(different_lenght_3,";")
print check_lenght_row(different_lenght_3,";",allowemptycell=False)