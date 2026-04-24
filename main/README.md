# Astronomical FITS Image Analyzer

##Overview
This project shows a basic data analysis pipeline built in python for astronomical FITS images.
Loads, visualizes, and analyzes real telescope data in FITS format.

---

## Features
- Load FITS files using Astropy
- Handle multi-extension FITS data
- Displays images with Z-scale normlization for better contrast
- Plots pixel brightness distributions
- Detects bright sourses using statistical thresholding

---

## Images Analyzed
- Horsehead Nebula (Astropy Sample Data)
- Messier 16 (Hubble Space Telescope via MAST)

---

## Tools and Libraries Used
- Python
- NumPy
- Matplotlib
- Astropy

---

## Requirements
Make sure you have Python 3 installed. Then install the required libraries.

---

## How to Run

**1. Open a terminal**
If you're on Windows:
- Open **Windows Terminal**
- Select **Ubuntu (WSL)**

**2. Clone the repository**
```bash
git clone https://github.com/SohaylaRaya/astro-fits-analyzer.git
cd astro-fits-analyzer
```

**3. Set up virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**4. Install dependencies**
```bash
pip3 install astropy matplotlib numpy
```

**5. Add FITS file**
- Download a FITS file from [NASA MAST](https://mast.stsci.edu) or use the built-in Astropy sample
- Place it in the `data/` folder

**6. Run the pipeline**
```bash
cd scripts
python3 run.py
```

**7. View outputs**
- Images are saved to the `plots/` folder
- Open them with your file explorer

---

## Output Images
![Horsehead Nebula](plots/horsehead_image.png)
![Horsehead Nebula Histogram](plots/horsehead_histogram.png)

![Messier 16](plots/m16_image.png)
![Messier 16 Histogram](plots/m16_histogram.png)


## Key Learning Outcomes
- How FITS files are structed and processed into images
- How to detect brightspots using statistical methods
- Working with real astronomical datasets








