
#written to be run in casa v5.6.2

#mmset lists the input of measurement sets to be imaged (equivalent of imaging and concatinating
#mset, is the common portion of the image names

#path to the ms locations
path_vis = '/beegfs/car/mubela/VLA/15A-043/calibrated_ms_backup/no_dummy/'
#scheduling block
sb = 1

#edge spectral windows to put into spectral window range
spw_beg = 2
spw_end = 9
#note: original continuum spectral windows range is 2-33 (first two are system setup spws), the split out target spws range becomes 0-31
#hence one of "2-9, 10-17, 18-25, 26-33" and one of "0~7, 8~15, 16~23, 24~31" are in the image name and spw parameter, respectively.

ms1 = 'sb{}am.no_dummy.spw2-33.ms'.format(sb)
ms2 = 'sb{}pm.no_dummy.spw2-33.ms'.format(sb)
mmset = [path_vis+ms1, path_vis+ms2]
mset = 'sb{}.spw{}-{}'.format(sb, spw_beg, spw_end)
spw_var = '{}~{}'.format(spw_beg-2, spw_end-2)

#if the sb changes, so should the phasecenters
#nxm list of phasecenters to be entered here
phasecenters = [['J2000 19:03:59.663578 +07.56.29.301080',
 'J2000 19:05:31.663578 +07.56.29.301080',
 'J2000 19:07:3.663578 +07.56.29.301080',
 'J2000 19:08:35.663578 +07.56.29.301080',
 'J2000 19:10:7.663578 +07.56.29.301080',
 'J2000 19:11:39.663578 +07.56.29.301080'],
['J2000 19:04:10.744375 +08.01.47.301080',
 'J2000 19:05:42.744375 +08.01.47.301080',
 'J2000 19:07:14.744375 +08.01.47.301080',
 'J2000 19:08:46.744375 +08.01.47.301080',
 'J2000 19:10:18.744375 +08.01.47.301080',
 'J2000 19:11:50.744375 +08.01.47.301080'],
['J2000 19:04:21.825172 +08.07.5.301080',
 'J2000 19:05:53.825172 +08.07.5.301080',
 'J2000 19:07:25.825172 +08.07.5.301080',
 'J2000 19:08:57.825172 +08.07.5.301080',
 'J2000 19:10:29.825172 +08.07.5.301080',
 'J2000 19:12:1.825172 +08.07.5.301080']]

fields = [['0,1,2,3,4,5,6,7,8,54,55,56,57,58,59,60,61,62,108,109,110,111,112,113,114,115,116,162,163,164,165,166,167,168,169,170,9,63,117,171',
 '9,10,11,12,13,14,15,16,17,63,64,65,66,67,68,69,70,71,117,118,119,120,121,122,123,124,125,171,172,173,174,175,176,177,178,179,8,18,62,72,116,126,170,180',
 '18,19,20,21,22,23,24,25,26,72,73,74,75,76,77,78,79,80,126,127,128,129,130,131,132,133,134,180,181,182,183,184,185,186,187,188,17,27,71,81,125,135,179,189',
 '27,28,29,30,31,32,33,34,35,81,82,83,84,85,86,87,88,89,135,136,137,138,139,140,141,142,143,189,190,191,192,193,194,195,196,197,26,36,80,90,134,144,188,198',
 '36,37,38,39,40,41,42,43,44,90,91,92,93,94,95,96,97,98,144,145,146,147,148,149,150,151,152,198,199,200,201,202,203,204,205,206,35,45,89,99,143,153,197,207',
 '45,46,47,48,49,50,51,52,53,99,100,101,102,103,104,105,106,107,153,154,155,156,157,158,159,160,161,207,208,209,210,211,212,213,214,215,44,98,152,206'],
['162,163,164,165,166,167,168,169,170,216,217,218,219,220,221,222,223,224,270,271,272,273,274,275,276,277,278,324,325,326,327,328,329,330,331,332,171,225,279,333',
 '171,172,173,174,175,176,177,178,179,225,226,227,228,229,230,231,232,233,279,280,281,282,283,284,285,286,287,333,334,335,336,337,338,339,340,341,170,180,224,234,278,288,332,342',
 '180,181,182,183,184,185,186,187,188,234,235,236,237,238,239,240,241,242,288,289,290,291,292,293,294,295,296,342,343,344,345,346,347,348,349,350,179,189,233,243,287,297,341,351',
 '189,190,191,192,193,194,195,196,197,243,244,245,246,247,248,249,250,251,297,298,299,300,301,302,303,304,305,351,352,353,354,355,356,357,358,359,188,198,242,252,296,306,350,360',
 '198,199,200,201,202,203,204,205,206,252,253,254,255,256,257,258,259,260,306,307,308,309,310,311,312,313,314,360,361,362,363,364,365,366,367,368,197,207,251,261,305,315,359,369',
 '207,208,209,210,211,212,213,214,215,261,262,263,264,265,266,267,268,269,315,316,317,318,319,320,321,322,323,369,370,371,372,373,374,375,376,377,206,260,314,368'],
['324,325,326,327,328,329,330,331,332,378,379,380,381,382,383,384,385,386,432,433,434,435,436,437,438,439,440,486,487,488,489,490,491,492,493,494,333,387,441,495',
 '333,334,335,336,337,338,339,340,341,387,388,389,390,391,392,393,394,395,441,442,443,444,445,446,447,448,449,495,496,497,498,499,500,501,502,503,332,342,386,396,440,450,494,504',
 '342,343,344,345,346,347,348,349,350,396,397,398,399,400,401,402,403,404,450,451,452,453,454,455,456,457,458,504,505,506,507,508,509,510,511,512,341,351,395,405,449,459,503,513',
 '351,352,353,354,355,356,357,358,359,405,406,407,408,409,410,411,412,413,459,460,461,462,463,464,465,466,467,513,514,515,516,517,518,519,520,521,350,360,404,414,458,468,512,522',
 '360,361,362,363,364,365,366,367,368,414,415,416,417,418,419,420,421,422,468,469,470,471,472,473,474,475,476,522,523,524,525,526,527,528,529,530,359,369,413,423,467,477,521,531',
 '369,370,371,372,373,374,375,376,377,423,424,425,426,427,428,429,430,431,477,478,479,480,481,482,483,484,485,531,532,533,534,535,536,537,538,539,368,422,476,530']]


def dirty_map(i,j):
    print('\nCreating dirty map of cut_{}_{} \n'.format(i+1,j+1))
    tclean(vis = mmset,
       imagename = mset+'_cut_'+str(i+1)+'_'+str(j+1)+'_dirty',
       datacolumn = 'corrected',
       specmode = 'mfs',
       spw = spw_var,
       field = fields[i][j],
       niter = 0,
       deconvolver = 'hogbom',
       gridder = 'mosaic',
       phasecenter = phasecenters[i][j],
       interactive = False,
       imsize = [44800,12800],
       cell = ['0.084arcsec'],
       stokes = 'I',
       weighting = 'briggs',
       robust = 0.0)
    return 0;
       
def rms_func(i,j):
    print('\nRunning imstat on dirty map: {}_cut_{}_{}_dirty.image\n'.format(mset,i+1,j+1))
    noise_stat = imstat(imagename= mset+'_cut_'+str(i+1)+'_'+str(j+1)+'_dirty.image')
    rms_temp = 5*noise_stat['rms'][0]
    return rms_temp;

def main_map(i,j):
    print('\nRunning tclean for map of cut_{}_{} \n'.format(i+1,j+1))
    tclean(vis = mmset,
       imagename = mset+'_cut_'+str(i+1)+'_'+str(j+1),
       datacolumn = 'corrected',
       specmode = 'mfs',
       spw = spw_var,
       field = fields[i][j],
       niter = 20202020,
       gain = 0.1,
       threshold = rms_var,
       deconvolver = 'hogbom',
       gridder = 'mosaic',
       phasecenter = phasecenters[i][j],
       interactive = False,
       imsize = [44800,12800],
       cell = ['0.084arcsec'],
       stokes = 'I',
       weighting = 'briggs',
       robust = 0.0)
    return 0;



# If something happens to stop the script partway through (e.g. qsub job ends before the script completes all the tiles) edit this section to run it from the point it terminates.
# How you edit it depends on where it breaks. change b_row to the row in which it breaks, b_col to the column in which it breaks and if the dirty map has already been created, change b_dirty to 2, otherwise it should be 1 (check that previous use of this script didn't leave it as 2)
# Before careful not to mix the index numbers with the descritpton numbers (numbers on the output image names) which are the index number + 1

b_row = 0 #change to row number if cut_2_3 (field[1][2]) then b_row = 1
b_col = 0 #change to col number if cut_2_3 (field[1][2]) then b_col = 2
b_step = 1 #set to 1 by default, set to 2 if the dirty map already exists
for n in range(b_row,len(phasecenters)): #number of columns of cuts i.e. number of lists
    if n == b_row:
        for m in range(b_col,len(phasecenters[n])):  #number of rows of cuts i.e. number in each list
            if m == b_col:
                for k in range(b_step,4):
                    step = k
                    if step == 1:
                        dirty_map(n,m)
                    if step == 2:
                        rms_var = rms_func(n,m)
                        print('cut_{}_{} rms = {}'.format(n+1,m+1,rms_var))
                    if step == 3:
                        main_map(n,m)
            else:
                for k in range(1,4):
                    step = k
                    if step == 1:
                        dirty_map(n,m)
                    if step == 2:
                        rms_var = rms_func(n,m)
                        print('cut_{}_{} rms = {}'.format(n+1,m+1,rms_var))
                    if step == 3:
                        main_map(n,m)
    else:
        for m in range(len(phasecenters[n])):  #number of rows of cuts i.e. number in each list
            for k in range(1,4):
                step = k
                if step == 1:
                    dirty_map(n,m)
                if step == 2:
                    rms_var = rms_func(n,m)
                    print('cut_{}_{} rms = {}'.format(n+1,m+1,rms_var))
                if step == 3:
                    main_map(n,m)

