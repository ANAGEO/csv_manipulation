## Function to visualise head of segment_statistics.csv file
# The argument "filepath" wait for a string containing the path to the .csv file to use file.
# The argument "nbrline" wait for a INT value refering to the number of rows to be showed (header excluded).

import os
import tempfile

def showcsvhead(filepath, nbrline):
    temp_path=tempfile.gettempdir()+"\\tempfile.csv"
    tmp=open(temp_path,"w")
    count=0
    for line in open(filepath):
        if count<=nbrline:
            tmp.write(line)
            count+=1
        else: 
            break
    tmp.close()
    tmpdf=pd.read_csv(temp_path, sep='|',header=0)
    os.remove(temp_path)
    return tmpdf.head(nbrline)
