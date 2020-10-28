#block 5 am spw2t9 calibration script
#casa version 5.4.1


#########################################################
#	variables for sources and measurement set	#
#########################################################
target = '3~562'
phscal = '2'
bcal= '1'
fcal = '0'
antref = 'ea04'
setjy_model = '3C286_U.im' #am block
#setjy_model = '3C48_U.im' #pm block

#write without the '.ms' which is included in the code
mset = '15A-043.sb5am.spw2-9'

#########################
#	Flagging	#
#########################

#pre inspection
#configuration scans
if kugars == 1:
	flag = 1
	execfile('mmscript_sb5am_2t9.flags.py')
#post inspection

if kugars == 2:
	flag = 2
	execfile('mmscript_sb5am_2t9.flags.py')

#########################################################
#	A priori  Antenna position corrections		#
#########################################################
if kugars == 3:
	gencal(vis = mset+'.ms',
		caltable = mset+'.antpos',
		caltype = 'antpos')

	gencal(vis = mset+'.ms',
		caltable = mset+'.gaincurve',
		caltype = 'gc')
	myTau = plotweather(vis = mset+'.ms', doPlot = True)

	gencal(vis = mset+'.ms',
		caltable = mset+'.opacity',
		caltype = 'opac',
		parameter = 'myTau')

	gencal(vis = mset+'.ms',
		caltable = mset+'.requantizer',
		caltype = 'rq')

#################################################
#		Flux density Scale		#
#################################################

if kugars == 4:
	setjy(vis = mset+'.ms',
	  field = fcal,
	  model = setjy_model)
#################################################
#		Initial Phase calibration	#
#################################################
'''
if kugars == 5:
	os.system('rm -rf '+mset+'.G0all')
	gaincal(vis = mset+'.ms',
	    caltable = mset+'.G0all',
	    field = fcal+','+bcal+','+phscal,
	    spw = '*:27~36',
	    solint = 'int',
	    refant = antref,
	    calmode = 'p',
	    gaintype = 'G',
	    minsnr = 5.0,
	    gaintable = [mset+'.antpos',mset+'.gaincurve',mset+'.requantizer',mset+'.opacity'])
'''
if kugars == 5:
	os.system('rm -rf '+mset+'.G0')
	gaincal(vis = mset+'.ms',
	    caltable = mset+'.G0',
	    field = bcal,
	    solint = 'int',
	    gaintype = 'G',
	    calmode = 'p',
	    gaintable = [mset+'.antpos',mset+'.gaincurve',mset+'.requantizer',mset+'.opacity'],
	    minsnr = 5,
	    refant = antref)

##########################################################
#		Delay Calibration			##
#bandpass calibration starting with antenna based delays##
#		Antenna based delays			##
##########################################################
if kugars == 6:
	gaincal(vis = mset+'.ms',
	    caltable = mset+'.K0',
	    field = bcal,
	    refant = antref,
	    solint = 'inf',
	    combine = 'scan',
	    minsnr = 5,
	    gaintype = 'K',
	    gaintable = [mset+'.antpos',mset+'.gaincurve',mset+'.requantizer',mset+'.opacity', mset+'.G0'],
	    spw = '*:5~58')
#################################################
#		Bandpass calibration		#
#################################################

#solve for bandpass#


if kugars == 7:
	os.system('rm -rf '+mset+'.B0')
	bandpass(vis = mset+'.ms',
	     caltable = mset+'.B0',
	     solint = 'inf',
	     field = bcal,
	     refant = antref,
	     gaintable = [mset+'.antpos',mset+'.gaincurve',mset+'.requantizer',mset+'.opacity',mset+'.G0', mset+'.K0'])

#################################################################
#	Complex gain on flux cal, bcal and phscal, respectively #
#################################################################
if kugars == 8:
	os.system('rm -rf '+mset+'.G1')
	gaincal(vis = mset+'.ms',
	    caltable = mset+'.G1',
	    field = fcal,
	    spw = '*:5~58',
	    solint = 'inf',
	    refant = antref,
	    gaintype = 'G',
	    gaintable = [mset+'.antpos',mset+'.gaincurve',mset+'.requantizer',mset+'.opacity', mset+'.K0', mset+'.B0'])

if kugars == 9:
    gaincal(vis = mset+'.ms',
	    caltable = mset+'.G1',
	    field = bcal,
	    spw = '*:5~58',
	    solint = 'inf',
	    refant = antref,
	    gaintype = 'G',
	    gaintable = [mset+'.antpos',mset+'.gaincurve',mset+'.requantizer',mset+'.opacity', mset+'.K0', mset+'.B0'],
	    append = True)
if kugars == 10:
    gaincal(vis = mset+'.ms',
	    caltable = mset+'.G1',
	    field = phscal,
	    spw = '*:5~58',
	    solint = 'inf',
	    refant = antref,
	    gaintype = 'G',
	    gaintable = [mset+'.antpos',mset+'.gaincurve',mset+'.requantizer',mset+'.opacity', mset+'.K0', mset+'.B0'],
	    append = True)



###########
#fluxscale#
###########

if kugars == 11:
    myscale = fluxscale(vis = mset+'.ms',
			caltable = mset+'.G1',
			fluxtable = mset+'.fluxscale1',
			reference = [fcal],
			transfer = [bcal,phscal],
			incremental = False)

#################################################
#		Apply calibration		#
#################################################

if kugars == 12:
	applycal(vis = mset+'.ms',
	     field = fcal,
	     gaintable = [mset+'.antpos',mset+'.gaincurve',mset+'.requantizer',mset+'.opacity', mset+'.fluxscale1', mset+'.K0',mset+'.B0'],
	     gainfield = ['','','','',fcal,'',''],
	     interp = ['','','','','nearest','',''],
	     calwt = [False],
	     parang = False)
if kugars == 13:
	applycal(vis = mset+'.ms',
	     field = bcal,
	     gaintable = [mset+'.antpos',mset+'.gaincurve',mset+'.requantizer',mset+'.opacity', mset+'.fluxscale1', mset+'.K0',mset+'.B0'],
	     gainfield = ['','','','',bcal,'',''],
	     interp = ['','','','','nearest','',''],
	     calwt = [False],
	     parang = False)
if kugars == 14:
	applycal(vis = mset+'.ms',
	     field = phscal,
	     gaintable = [mset+'.antpos',mset+'.gaincurve',mset+'.requantizer',mset+'.opacity', mset+'.fluxscale1', mset+'.K0',mset+'.B0'],
	     gainfield = ['','','','',phscal,'',''],
	     interp = ['','','','','nearest','',''],
	     calwt = [False],
	     parang = False)
if kugars == 15:
	applycal(vis = mset+'.ms',
	     field = target,
	     gaintable = [mset+'.antpos',mset+'.gaincurve',mset+'.requantizer',mset+'.opacity', mset+'.fluxscale1', mset+'.K0',mset+'.B0'],
	     gainfield = ['','','','',phscal,'',''],
	     interp = ['','','','','linear','',''],
	     calwt = [False],
	     parang = False)

#########
# split #
#########
   
if kugars == 16:
	split(vis = mset+'.ms',
	      outputvis = mset+'target.ms',
	      field = target,
	      datacolumn = 'corrected')

if kugars == 17:
	split(vis = mset+'.ms',
	      outputvis = mset+'phase.ms',
	      field = phscal,
	      datacolumn = 'corrected')

if kugars == 18:	
	split(vis = mset+'.ms',
	      outputvis = mset+'flux.ms',
	      field = fcal,
	      datacolumn = 'corrected')
if kugars == 19:
	split(vis = mset+'.ms',
	      outputvis = mset+'bandpass.ms',
	      field = bcal,
	      datacolumn = 'corrected')


# this section is obsolete, clean is done using imaging pipeline now
###############
### tclean ####
###############
if kugars == 20:
	tclean(vis = mset+'target.ms',
	  imagename = mset+'noise',
	  datacolumn = 'data',
	  specmode = 'mfs',
	  niter = 0,
	  deconvolver = 'hogbom',
	  gridder = 'mosaic',
	  phasecenter = 'J2000 19:10:13.530 +09.06.12.44',
	  interactive = False,
	  imsize = [4000,4000],
	  cell = ['0.084arcsec'],
	  stokes = 'I',
	  weighting = 'briggs',
	  robust = 0.0)

if kugars == 21:
	noise_stat = imstat(imagename= mset+'noise.image')
	rms_var = noise_stat['rms'][0]
if kugars == 22:
	tclean(vis = mset+'target.ms',
	  imagename = mset+'_I',
	  datacolumn = 'data',
	  specmode = 'mfs',
	  niter = 89000,
	  gain = 0.1,
	  threshold = rms_var,
	  deconvolver = 'hogbom',
	  gridder = 'mosaic',
	  phasecenter = 'J2000 19:10:13.530 +09.06.12.44',
	  interactive = False,
	  imsize = [4000,4000],
	  cell = ['0.084arcsec'],
	  stokes = 'I',
	  weighting = 'briggs',
	  robust = 0.0)


