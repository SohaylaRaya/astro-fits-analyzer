# Astronomical FITS Image Analyzer

##Overview
This project shows a basic data analysis pipeline built in python for astronomical FITS images.
Loads, visualizes, and analyzes real telescope data in FITS format.


## Features
- Load FITS files using Astropy
- Handle multi-extension FITS data
- Displays images with Z-scale normlization for better contrast
- Plots pixel brightness distributions
- Detects bright sourses using statistical thresholding


## Images Analyzed
- Horsehead Nebula (Astropy Sample Data)
- Messier 16 (Hubble Space Telescope via MAST)


## Tools and Libraries Used
- Python
- NumPy
- Matplotlib
- Astropy


## How to Run
'''bash
source venv/bin/activate
cd main
python main.py


## Output Images
![Horsehead Nebula](plots/horsehead_image.png)
![Horsehead Nebula Histogram](plots/horsehead_histogram.png)

![Messier 16](plots/m16_image.png)
![Messier 16 Histogram](plots/m16_histogram.png)


## Key Learning Outcomes
- How FITS files are structed and processed into images
- How to detect brightspots using statistical methods
- Working with real astronomical datasets








