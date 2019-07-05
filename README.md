# Csv manipulation
This repository is dedicated to some pieces of code allowing manipulation of .csv files. 

CSV manupilation functionalities are provided by existing python (external) libraries such as, e.g., [Pandas library](https://pandas.pydata.org/). However, the use of these external libraries create some dependencies that should be avoided in some applications.

If you add code to this repository, please try to make it well documented (and clean is better but not mandatory ;) ). Also, if you can provide some test files it's great.

## Change_delimiter
Change the delimiter of the csv file

## check_leght_rows
Function that check if rows of a .csv file have the same number of items than number of column in the first line (header). If rows's lenght are identical, the function return 0. If not, it return a list containing the index number of row(s) that failed

## Concatenate
Function similar to "stack_csv". Function which concatenate (stack them vertically) several individual .csv files each others.

## Concat_Find_replace
Function which concatenate (stack them vertically) several individual .csv files each others. The function allows also to replace some values at the same time. Values to replace should be provided in a python dictionary with key=value correspondance.
It is a combination of "Concatenate" and "Find_replace" functions.

## Cut_multiple_columns
This function allows to create a new CSV file with only some columns extracted from an existing CSV file. 

## Find_replace
Function which find specific value and replace it by another. It can also just count the number of values founded.

## multiple_join
Functions that allow to join (left or inner joint, for the moment) csv files together, according to the first column only (primary key should be on first column). Provides also a function that create a .csvt file with the same type of all columns except for the first one. 

## save_head
Function that save the header of a CSV, or the header+n first rows, in a new csv file. Usefulle to have a quick look of a CSV file which is too big to be opened with traditional csv reader. 

## Select_from_first_column
Function which create a new .csv file with only specifics rows, identified by their value on the first column (typically ID).

## Show_head
Based on PANDAS. Function to visualise head of segment_statistics.csv file.

## stack_csv
Function similar to "Concatenate". Function which concatenate (stack them vertically) several individual .csv files each others. 