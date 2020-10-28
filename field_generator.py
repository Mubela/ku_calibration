#writen to accomodate python 2x string formating
#this version is not particularly generic. It will need editing to handle
#a starting shape [10,6,9] and a final shape other than 3(rows) 6(cuts) 4(cut rows) 9(fields) [3,6,4,9 or 3,6,36]

from astropy.io import ascii
import numpy as np
import os

#pompt user to enter coordinate file and read the file into a variable
print('Choose input file from below.\n')
os.system('ls ra_n_dec*')
coordinates_var = input('\nInput the text file with the coordinates of the sb you\'re working on.\n=> ')
print(f'\nRunning code on {coordinates_var}...\n')
f = ascii.read(coordinates_var)


#read list of field ID's into numpy array of 10 stripes with 6 cuts of 9 scans
#read field ID's into temp variable then pass temp to a numpy array variable, fld
#can be done in a single line as: fld = np.array(f['ID']).reshape(10,6,9)

temp = f['ID']
fld = np.array(temp).reshape(10,6,9)

#declare required variables

ycuts = 3
xcuts = 6
nrows = 4
n_row_fields = 9
n_cut_fields = nrows*n_row_fields

#create a  list of 3 lists of 6 lists (shape of numpy array above)
#using lists as opposed to numpy arrays allows you to edit the lists contents, starting empty and appending values where you want them
cuts = []
for i in range(ycuts):
    cuts.append([])
    for j in range(xcuts):
        cuts[i].append([])
        
#total number of tiles (cuts)
n_cuts = xcuts*ycuts

#number of rows per cut
if len(fld)%ycuts == 0:
    n_cut_rows = int(len(fld)/ycuts)
elif len(fld)/ycuts > 0:
    n_cut_rows = int(len(fld)/ycuts)+1

#create three rows of cuts with row 1 and row 2 overlaping on stripe 4 and row 2 and row 3 overlaping on stripe 7.
#these is done using a 4 dimensional list of lists (3x6x4x9)
for n in range(ycuts):
    for i in range(xcuts):
        if n == 0:
            for k in range(n_cut_rows):
                cuts[n][i].append(fld[k][i])
        elif n == 1:
            for k in range(n_cut_rows-1, n_cut_rows+3):
                cuts[n][i].append(fld[k][i])
        else:
            for k in range(n_cut_rows+2, n_cut_rows+6):
                cuts[n][i].append(fld[k][i])
                
#redifine the 4D list to a 3D numpy array (3x6x36)
fields_temp = np.array(cuts).reshape(ycuts,xcuts,n_cut_fields)

#create a 3D
fields = []
for i in range(ycuts):
    fields.append([])
    for j in range(xcuts):
        fields[i].append([])

for i in range(ycuts):
    for j in range(xcuts):
        temp = str(fields_temp[i][j][0])
        for k in range(1,n_cut_fields):
            temp += ',{}'.format(fields_temp[i][j][k])
        fields[i][j] = temp

fields_ext = fields

for i in range(ycuts):
    for j in range(xcuts):
        for k in range(0,36,9):
            if j == 0:
                fields_ext[i][j] += ',{}'.format(fields_temp[i][j+1][k])
            if j == xcuts-1:
                fields_ext[i][j] += ',{}'.format(fields_temp[i][j-1][k+8])
            elif j > 0 and j < xcuts-1:
                fields_ext[i][j] += ',{},{}'.format(fields_temp[i][j-1][k+8], fields_temp[i][j+1][k])

print('\n',fields_ext)
            
            

