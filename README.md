# otfm_calibration_and_imaging

## Calibration 
1. Data Examination and Editing
2. Calibration
   a. a priori corrections
   b. Initial phase calibration
   c. Delay calibration
   d. Bandpass calibration
   e. Gain calibration
   f. Scaling amplitude gains
3. Apply calibration

## Pre-Imaging
1. Determine imaging resolution (and apply sampling e.g. 3px/beam or 5px/beam)
2. a. Geometrically map out scans on entire MS
   b. Image size - dependent on computational resources available
                 - and fields to be included in the image
      Note: For very large fields, the image will have to be subdivided. Therefore this step maps out the MS in order to determine appropriate cuts
   c. Overlay cuts on geometrical map of scans
3. Generate fields based on size and cuts in (2)
4. Common restoring beam (if desired) - requires sample imaging, image phase calibrators and use them in beam-elongation script
   a. analyse feasibility by looking at beam elongation
   b. decide what best suites your science, e.g circular gaussian
 

## Deconvolution and Imaging
Run imaging script using parameters in pre-imaging
