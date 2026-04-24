import matplotlib
matplotlib.use('Agg')

from astropy.io import fits
from astropy.visualization import ZScaleInterval
import numpy as np
import matplotlib.pyplot as plt

def load_fits (file_path):
	#loads a FITS file, return as NumPy array
	hdul = fits.open(file_path, memmap=True)

	data = None

	for hdu in hdul:
		if hdu.data is not None and hdu.data.ndim==2:
			data = hdu.data
			break

	hdul.close()

	if data is None:
		raise ValueError(f"No image found in {file_path}")
	data = np.nan_to_num(data)
	data = data[::4, ::4]

	return data


def show_image(data, title, save_path=None):
	interval = ZScaleInterval()
	try:
		vmin, vmax = interval.get_limits(data)
		if vmin == vmax:
			raise ValueError("vmin equals vmax")
	except:
		vmin, vmax = np.percentile(data, [2, 98])

	sources = data>(np.mean(data) + 3*np.std(data))

	plt.figure(figsize=(6,6))
	plt.imshow(data, cmap='gray', vmin=vmin, vmax=vmax)
	plt.contour(sources, colors = 'red', linewidths = 0.5)
#	plt.colorbar()
	plt.title(title)
	if save_path:
		plt.savefig(save_path, dpi=200, bbox_inches='tight')
	plt.close()


def brightness_histogram(data, title, save_path=None):
	plt.figure()

	sample = data.flatten()[::10]
	plt.hist(sample, bins=100)
	plt.xlabel("Pixel Value")
	plt.ylabel("Count")
	plt.title(title)
	if save_path:
		plt.savefig(save_path, dpi=200, bbox_inches='tight')
	plt.close()

def detect_sources(data, sigma=3):
	import numpy as np

	mean = np.mean(data)
	std = np.std(data)

	threshold = mean + sigma* std

	source = data > threshold

	return sources
