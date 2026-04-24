from analyze import load_fits, show_image, brightness_histogram

file_path = "../data/m16.fits"

data = load_fits(file_path)

print(data.shape)

show_image(data, "Messier 16 (Hubble)","../plots/m16_image.png")
brightness_histogram(data, "Pixel Brightness Distribution","../plots/m16_histogram.png")






