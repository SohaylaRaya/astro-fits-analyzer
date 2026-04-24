from astropy.io import fits
from astropy.visualization import ZScaleInterval
import numpy as np
import matplotlib.pyplot as plt


def load_fits (file_path):
	#loads a FITS file, return as NumPy array
	hdul = fits.open(file_path)
	data = None

	for hdu in hdul:
		if hdu.data is not None and hdu.data.ndim == 2:
			data = hdu.data
			break
	hdul.close()

	if data is None:
		raise ValueError(f"No image found in {file_path}")
	return np.nan_to_num(data)

def show_image(data, title, save_path=None):
	interval = ZScaleInterval()
	vmin, vmax = interval.get_limits(data)
	plt.figure(figsize=(6,6))
	plt.imshow(data, cmap='gray', vmin=vmin, vmax=vmax)
	plt.colorbar()
	plt.title(title)
	if save_path:
		plt.savefig(save_path, dpi=200, bbox_inches='tight')
	plt.show()
	plt.close()

def brightness_histogram(data, title, save_path=None):
	plt.figure()
	plt.hist(data.ravel(), bins=100)
	plt.xlabel("Pixel Value")
	plt.ylabel("Count")
	plt.title(title)
	if save_path:
		plt.savefig(save_path, dpi=200, bbox_inches='tight')
	plt.show()
	plt.close()

