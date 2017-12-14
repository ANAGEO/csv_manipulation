## Function to visualise head of segment_statistics.csv file
# The argument "filepath" wait for a string containing the path to the .csv file to be use.
# The argument "saveoutput" wait for a string containing the path to the new .csv file containing the results.
# The argument "nbrline" wait for a INT value refering to the number of rows to be showed (header excluded).

import os
import tempfile
import shutil

def savecsvhead(filepath, saveoutput, nbrline):
    temp_path=os.path.join(tempfile.gettempdir(),"tempfile.csv")
    tmp=open(temp_path,"w")
    count=0
    for line in open(filepath):
        if count<=nbrline:
            tmp.write(line)
            count+=1
    tmp.close()
    shutil.copy2(temp_path, saveoutput)
    os.remove(temp_path)
    return "Done"

# Test with header + 0 lines
filepath="test_files/test.csv"
saveoutput="test_files/savecsvhead_test_results_0lines.csv"
savecsvhead(filepath, saveoutput, 0)

# Test with header + 10 lines
saveoutput="test_files/savecsvhead_test_results_10lines.csv"
savecsvhead(filepath, saveoutput, 10)