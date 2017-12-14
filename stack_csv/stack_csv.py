## Function which stack all individual .csv files each others and save them in a new .csv file.
## This is not a join function. This function will create a stack of .csv files.
# The argument "indir" wait for a string containing the path to the directory where the individual .csv files are stored.
# The argument "outfile" wait for a string containing the path to the output file to create.
# The argument "overwrite" wait for True/False value allow or not to overwrite existing outfile.
# The argument "pattern" wait for a string containing the pattern of filename to use. Use wildcards is possible (*.csv for all .csv files)

import os,sys
import glob

def stack_csv(indir,outfile,overwrite=False,pattern=None):
    os.chdir(indir)
    if pattern:
        fileList=glob.glob(pattern)
    else: fileList=glob.glob("*.csv")
    print fileList
    if len(fileList)<=1:
        sys.exit("This function require at least two .csv files to be stacked together."    )
    if os.path.isfile(outfile) and overwrite==False:
        print "File '"+str(outfile)+"' aleady exists and overwrite option is not enabled."
    else:
        if overwrite==True:
            os.remove(outfile)
        stacked_csv=open(outfile,"a")
        # first file including header:
        for line in open(fileList[0]):
            if len(line.split("\n")[0])>0:
                stacked_csv.write(line)
        stacked_csv.write("\n")
        # now the rest without header:
        for filename in fileList[1:]:
            f=open(filename)
            f.next() # skip the header
            for line in f:
                if len(line.split("\n")[0])>0:
                    stacked_csv.write(line)
            f.close() # not really needed
            if filename != fileList[-1]:
                stacked_csv.write("\n")
        stacked_csv.close()
        print str(len(fileList))+" individual .csv files will be stacked each other."


# Test without pattern
current_directory=os.path.dirname(os.path.abspath(" __file__ "))
indir=os.path.join(current_directory,"csv_manipulation","stack_csv","test_files","input")
outfile=os.path.join(current_directory,"csv_manipulation","stack_csv","test_files","output","stackcsv_results_A.csv")
stack_csv(indir, outfile,  overwrite=True)

# Test with pattern
outfile=os.path.join(current_directory,"csv_manipulation","stack_csv","test_files","output","stackcsv_results_B.csv")
stack_csv(indir, outfile, overwrite=True, pattern="test_*.csv")


# Test NO Overwrite
outfile=os.path.join(current_directory,"csv_manipulation","stack_csv","test_files","output","stackcsv_results_A.csv")
stack_csv(indir, outfile,  overwrite=False)