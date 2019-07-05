## Function which concatenate (stack them vertically) several individual .csv files each others
# The argument "indir" wait for a string containing the path to the directory where the individual .csv files are stored.
# The argument "pattern" wait for a string containing the pattern of filename to use. Use wildcards is possible (*.csv for all .csv files)
# The argument "outfile" wait for a string containing the path to the output file to create.
# The argument "overwrite" wait for True/False value allow or not to overwrite existing outfile.

import os
import glob

def concatenate(indir,pattern,outfile,overwrite=False):
                output_message=""
                output_message+="Start concatenate individual .csv files with segments' statistics on "+time.ctime()+"\n\n"
                print (output_message)
                os.chdir(indir)
                fileList=glob.glob(pattern)
                if os.path.isfile(outfile) and overwrite==False:
                    print "File '"+str(outfile)+"' aleady exists and overwrite option is not enabled."
                else: 
                    if overwrite==True:
                        os.remove(outfile)
                    concatcsv=open(outfile,"a")
                    countline=0
                    # first file:
                    for line in open(fileList[0]):
                        concatcsv.write(line)
                        countline+=1
                    # now the rest: 
                    for filename in fileList[1:]:
                        output_message+="Working on "+str(filename)+"\n"
                        f=open(filename)
                        f.next() # skip the header when not the first file
                        for line in f:
                            concatcsv.write(line)
                            countline+=1
                        f.close() # not really needed
                    concatcsv.close()
                    if len(fileList)>=1:
                        output_message+="\n"+str(len(fileList))+" individual .csv file(s) were concatened each other."
                    else:
                        output_message+="\n"+"Only one individual .csv files."               
                    output_message+=" "+str(countline)+" rows in the concatened .csv file."+"\n"
                    return output_message