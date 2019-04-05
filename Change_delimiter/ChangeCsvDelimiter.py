# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:58:34 2019

@author: tais
"""

import csv, shutil

def ChangeCsvDelimiter(in_file, sep, new_sep, out_file=''):
    # Parameters for tempfile (path and sep)
    path, ext = os.path.splitext(in_file)
    tmp_file = "%s_tmp%s"%(path,ext)

    with open(in_file,'r') as f_in, open(tmp_file,'w') as f_out:
        csvreader = csv.reader(f_in, delimiter=sep)
        csvwriter = csv.writer(f_out, delimiter=new_sep)
        for in_row in csvreader:
            csvwriter.writerow(in_row)
        f_in.close()
        f_out.close()
    # Overwrite existing input file it 'out_file' not specified
    if out_file == '':
        os.remove(in_file)
        shutil.copy2(tmp_file,in_file)
        os.remove(tmp_file)
    else:
        shutil.copy2(tmp_file,out_file)
        os.remove(tmp_file)


# Test
infile_A = "/media/tais/data/Dropbox/ULB/Jupyter_notebooks/CSV_Manipulation/Github/csv_manipulation/Change_delimiter/test_file/sss.csv"
infile_B = "/media/tais/data/Dropbox/ULB/Jupyter_notebooks/CSV_Manipulation/Github/csv_manipulation/Change_delimiter/test_file/test.csv"
outfile = "/media/tais/data/Dropbox/ULB/Jupyter_notebooks/CSV_Manipulation/Github/csv_manipulation/Change_delimiter/test_file/test_result.csv"


ChangeCsvDelimiter(infile_A, ',', ';')
ChangeCsvDelimiter(infile_B, '|', ',', out_file=outfile)