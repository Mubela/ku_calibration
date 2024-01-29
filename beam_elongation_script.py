from astropy.table import Table
from astropy.io import fits
from radio_beam import Beam
import glob
import os


def image_data(fits_image_file):
    header = fits.getheader(fits_image_file)
    beam_temp = Beam.from_fits_header(header)
    beam = beam_temp.to_header_keywords()
    return beam, header;
    

output_prefix = input('Enter output name prefix (without extension):\n>')
fits_files = glob.glob('*.fits')
fits_files.sort()

# define variables
objects = []
id_num = []
majors = []
minors = []
ratios = []
count = 0

for i in fits_files:
    count += 1
    beam, header = image_data(i)
    objects.append(header['OBJECT'])
    majors.append(beam['BMAJ'])
    minors.append(beam['BMIN'])
    ratios.append(beam['BMAJ']/beam['BMIN'])
    id_num.append(count)
    
beam_table = Table([id_num, objects, majors, minors, ratios], names=['ID', 'Object', 'major axis', 'minor axis', 'Beam elongation'])

beam_table.write('{}_beam_elongation.csv', format='csv'.format(output_prefix))
beam_table.write('{}_beam_elongation.txt', format='ascii.rst'.format(output_prefix))
