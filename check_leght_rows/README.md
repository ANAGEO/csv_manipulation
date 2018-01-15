# check_lenght_row.py

Function that check if rows of a .csv file have the same number of items than number of column in the first line (header).

If rows's lenght are identical, the function return 0. If not, it return a list containing, for row that failed, the value of the first column

- 'csvfile' wait for the complete path (string) to the csvfile to be checked 
- 'separator' wait for the character used as separator in the .csv file (string) 