

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
import os

#to attach scan ID numbers to each scan uncomment 1.b. under Plots > Scans


#pompt user to enter coordinate file and read the file into a variable
print('Choose input file from below.\n')
os.system('ls ra_n_dec*')
coordinates_var = input('\nInput the text file with the coordinates of the sb you\'re working on.\n=> ')
print(f'\nRunning code on {coordinates_var}...\n')
f = ascii.read(coordinates_var)

#create plot columns

#read the first scan in every stripe for RA and Dec respectively
x_start = f[0:540:54]['RA']
y_start = f[0:540:54]['Decl']

#read the last scan in every stripe for RA and Dec respectively
x_end = f[53:540:54]['RA']
y_end = f[53:540:54]['Decl']



################# CONVERSION FACTORS ##########################
#convert ra - sexagesimal to degress
#1 hour = 15 degs
h = 15.0
#1 min = 0.25 degs
m = 0.25
#1 sec = 0.0041667 degs
s = 1/240.0
#1 amin = 1/60 deg
mac = 1/60.0
#1 asec = 1/3600 deg
sac = 1/3600.0
############################

################# CONVERSION FUNCTIONS ########################
####
#functions to convert ra and dec from sexagesimal to degrees
####
def ra_sexa2deg(ra_var):
    output=[]
    for i in range(len(ra_var)):
        ra_hour = float(ra_var[i][0:2])*h
        ra_min = float(ra_var[i][3:5])*m
        ra_sec = float(ra_var[i][6:15])*s
        sum_ra_components = ra_hour+ra_min+ra_sec
        output.append(sum_ra_components)
    return output;

def dec_sexa2deg(dec_var):
    output=[]
    for i in range(len(dec_var)):
        dec_hour = float(dec_var[i][1:3])
        dec_min = float(dec_var[i][4:6])*mac
        dec_sec = float(dec_var[i][7:15])*sac
        sum_dec_components = dec_hour+dec_min+dec_sec
        output.append(sum_dec_components)
    return output;

####
#functions to convert ra and dec degrees to sexagesimal
####
def ra_deg2sexa(var_ra):
    output = []
    for i in range(len(var_ra)):
        temp = var_ra[i]/15
        hour = int(temp)
        temp -= hour
        temp *= 60
        min_ra = int(temp)
        temp -= min_ra
        sec = temp*60
        output.append(str(hour)+':'+str(min_ra).zfill(2)+':'+str.format('{0:.6f}', sec))
    return output;

def dec_deg2sexa(var_dec):
    output = []
    for i in range(len(var_dec)):
        deg = int(var_dec[i])
        temp = var_dec[i] - deg
        temp *= 60
        amin = int(temp)
        temp -= amin
        asec = temp*60
        output.append('+'+str(deg).zfill(2)+'.'+str(amin).zfill(2)+'.'+str.format('{0:.6f}', asec))
    return output;
###############################################################


########################  ##CUTS##  ###########################
#size of ra in degrees divided by desired number of cuts in x-direction times size of decl in degrees divided by desired number of cuts in y-direction
#stripe length is 2.3 degrees
stripe_length = 2.3
#stripe height is 0.265 degrees
stripe_height = 0.265
#number of stripes in the block - used in phasecenter offset calculation
stripe_count = 10
#size of ra in degrees divided by desired number of cuts in x-direction
xcuts = 6
div_x = stripe_length/xcuts
#size of dec in degress divided by desired number of cuts in y-direction
ycuts = 3
div_y = stripe_height/ycuts
###############################################################
'''
Note: changing the ycuts variable affects the output phasecenter command. You need to manually append or remove the required number of lists in the list of lists.
'''

######################  PIXEL SIZE  ###########################
cell_size_asec = 0.084 #0.14
cell_size_deg = cell_size_asec/3600
#length and height of cuts @ 16384 px and 5000 px, respectively, using 5px/beam | pixels to degrees
#alternative: length and height of cuts @ 8192 px x 8192/4096 using either 3px or 5px/beam.
cut_length_px =  22318 #18600#16740 #18000 #8192
cut_length_deg = cut_length_px*cell_size_deg
cut_height_px =  6310 #5679 #5000 #4096
cut_height_deg = cut_height_px*cell_size_deg
###############################################################

#####################     SCANS     ###########################

#0. initialise two lists of lists of variables, x and y for ra and dec, respectively
#1. load the coordinates of each stripe into two temporal variables, one for ra and the dec, respectively
#2 (a). pass the temporal variables to the conversion functions for the respective coordnates, save result in another variable
#  (b). read result into the column corresponding to the stripe number in the list of lists variables x[i] and y[i], for ra and decl, respectively
#AUX. These will be used to iteratively plot each stripe onto the same figure.


#initialise two lists of lists of variables
#to account for the number of stripes (10 for KuGARS)
'''
x = [[],[],[],[],[],[],[],[],[],[]]
y = [[],[],[],[],[],[],[],[],[],[]]

x= [[]]*stripe_count
y= [[]]*stripe_count
'''
#0#
x = []
y = []
for i in range(stripe_count):
    x.append([])
    y.append([])
#1#

for i in range(len(x)):
#temporarily put RA and Dec columns into respective stripe variables
#each stripe has a length of 54 (Note: 56 is used below because there are 2 dummy scans preceding the start of each stripe)
#use multiples of 56 in steps of i and i+1 (beginning and end, respectively) to set range for iterative stripes
    stripe_x = f[(54*i):(54*(i+1))]['RA']
    stripe_y = f[(54*i):(54*(i+1))]['Decl']
#2#  (a) and (b)

# since x and y are lists of lists, the ra and dec of the ith
# stripe are put into the ith list of x and y, respectively.
# the step first converts the stripe from sexagesimal to degrees
# and then assigns the list of ra and dec to x[i] and y[i], respectively
    stripe_x_deg = ra_sexa2deg(stripe_x)
    x[i] = stripe_x_deg

    stripe_y_deg = dec_sexa2deg(stripe_y)
    y[i] = stripe_y_deg

###############################################################

###############################################################
#########################  OFFSETS  ###########################
###############################################################

#### 1. STRIPE FIRST SCAN OFFSET ####
#offset between the starting scan on two consecutive stripes
offset_x = x[1][0] - x[0][0]
offset_y = y[1][0] - y[0][0]
#starting offset
offset_start = (stripe_count-1)/(ycuts+1)*offset_x

#### 2. OFFSET ANGLE ####
offset_angle_rad  = np.arctan(offset_y/offset_x)
offset_angle_deg = offset_angle_rad*180/np.pi

#### 3. OFFSET BETWEEN CONSECUTIVE PHASECENTERS ####
#see phasecenters ***

###############################################################
 
############# BLOCK BOUNDARY LINES, LEFT AND RIGHT ############
#add lines defining the edges of the blocks (first and last scan of each stripe) to the plot of x[i],y[i]
#convert contents of first and last scan in each stripe variable to degrees
x_start_deg = ra_sexa2deg(x_start)
y_start_deg = dec_sexa2deg(y_start)
x_end_deg = ra_sexa2deg(x_end)
y_end_deg = dec_sexa2deg(y_end)
###############################################################

################    PHASECENTERS     ##########################
# this determines the number and position of the phasecenters
# based on the desired number of cuts and resolution
'''
phase_x = [[]]*ycuts
phase_y = [[]]*ycuts
'''

phase_x = []
phase_y = []

for i in range(ycuts):
    phase_x.append([])
    phase_y.append([])
    
x_phase_start = []
y_phase_start = []

#x_phase_start.append(x_start_deg[0]+(div_x/2)) #create generic squares without an offset to follow the slant
x_phase_start.append(x_start_deg[0]+(div_x/2)+offset_start) #comment this out if above is included in codex
y_phase_start.append(y_start_deg[0]+(div_y/2))

for i in range(ycuts-1):
    temp = y_phase_start[i]+div_y
    y_phase_start.append(temp)
    
#match the size of the number of y variables to x for plot
for i in range(ycuts):
    temp = y_phase_start[i]
    temp2 = []
    for r in range(xcuts):
        temp2.append(temp)
    phase_y[i] = temp2
    
for i in range(xcuts-1):
    temp = x_phase_start[i]+div_x
    x_phase_start.append(temp)
phase_x[0] = x_phase_start

#### ***OFFSET BETWEEN CONSECUTIVE PHASECENTERS***
offset_phase_y = phase_y[1][0]- phase_y[0][0]
offset_phase_x = offset_phase_y/np.tan(offset_angle_rad)

for i in range(1,ycuts):
    temp_list = []
    for j in range(xcuts):
        #temp = phase_x[0][j] #this and line below pair with previous comment
        temp = phase_x[0][j] + (offset_phase_x*i)
        temp_list.append(temp)
    phase_x[i] = temp_list

####### OUTPUT PHASECENTERS ########
phasecenters_x = []
for i in range(ycuts):
    phasecenters_x.append([])
    
    
for i in range(len(phase_y)):
    out_phase_x = phase_x[i]
    phasecenters_x[i] = ra_deg2sexa(out_phase_x)

out_phase_y = []
for i in range(len(phase_y)):
    out_phase_y.append(phase_y[i][0])

phasecenters_y = dec_deg2sexa(out_phase_y)

#initialize an empty list of lists to hold the output phasecenters, number of lists is based on the number of the rows of phasecenters, i.e. ycuts
output_phasecenters = []
for i in range(ycuts):
    output_phasecenters.append([])
    
for i in range(len(phasecenters_y)):
    for j in range(len(phasecenters_x[i])):
        print('J2000 {} {}'.format(phasecenters_x[i][j],phasecenters_y[i]))
        output_phasecenters[i].append('J2000 {} {}'.format(phasecenters_x[i][j],phasecenters_y[i]))
print('\n\n')
#print(output_phasecenters)

###############################################################

########################## PLOTS ##############################

#### 1. SCANS ####
  ## a.
#iteratively plot the ith list in x against the ith list in y on the same plot

for i in range(len(x)):
    plt.plot(x[i],y[i], linestyle='', marker='*', label='stripe '+str(i))
  ## b.
#### number on the scans using field ID ####
x_txt = []
y_txt = []
for i in range(len(x)):
    for j in range(len(x[i])):
        x_txt.append(x[i][j])
        y_txt.append(y[i][j])

count = []
for i in range(540):
    count.append(str(i))

for i, count in enumerate(count):
    txt = x_txt[i]
    tyt = y_txt[i]
    plt.text(txt, tyt, count, fontsize=9)
###########################################

#### 2. START AND END LINES ####

plt.plot(x_start_deg, y_start_deg, label='stripe start')
plt.plot(x_end_deg, y_end_deg, label='stripe end')

#### 3 PHASECENTERS ####
#overlay all the cutout phasecenters
for n in range(ycuts):
    plt.plot(phase_x[n], phase_y[n], marker='o', linestyle='', label='Phasecenters\nrow '+str(n+1))
    
#### 3. CUT BOXES ####

#################################################
#bounding boxes around phasecenters for each cut#
#################################################

#length of box edges on (ra) axis
x_side = cut_length_deg
#length of box edges on (dec) axis
y_side = cut_height_deg

#NOTE: if you use a cut length of 8192 px at 3px/beam gives ~7.2 cuts, leaving a residual ~0.22 cuts
#this essentially means there is a value of(in px) [stripe_length (8020/0.14)] divided by [cut length (8192)]
#minus integer number of cuts(7) of ~1798.86 unimaged

for i in range(ycuts):
    for j in range(xcuts):
        temp_x = phase_x[i][j]
        temp_y = phase_y[i][j]
        x1 = temp_x - (x_side/2)
        x2 = temp_x + (x_side/2)
        y1 = temp_y - (y_side/2)
        y2 = temp_y + (y_side/2)
        left_x=[x2,x2]
        left_y=[y1,y2]
        right_x=[x1,x1]
        right_y=[y1,y2]
        top_x=[x1,x2]
        top_y=[y2,y2]
        bottom_x=[x1,x2]
        bottom_y=[y1,y1]
        plt.plot(left_x, left_y,right_x,right_y, top_x,top_y, bottom_x,bottom_y)
        #plt.plot(right_x,right_y)
        #plt.plot(top_x,top_y)
        #plt.plot(bottom_x,bottom_y)

### 4. PLOT AESTHETICS ####

plt.xlim(289.5,285.7) #reverse x axis, ra counts right to left
plt.xlabel('Right Ascension (degrees)')
plt.ylabel('Declination (degrees)')
plt.legend(loc='upper left')
plt.show()




    

