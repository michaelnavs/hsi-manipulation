"""
Author: Michael Navarro

This program will open a HSI file and display spectral signature of a pixel in 
wavelength range of 460-530
"""
import sys
from spectral import open_image, imshow, get_rgb, BandInfo
import matplotlib
import matplotlib.pyplot as plt


def main(row: int, col: int) -> None:
    img = open_image("./images/first_data_2_12_2021.bil.hdr")

    wavelength_range = (460, 530)  # store desired wavelength range values

    pixel = img.read_pixel(row, col)  # get reflectance values
    wavelengths = img.bands.centers  # get wavelengths
    reduced_wavelengths = []  # store desired wavelength values
    # store index of wavelength values above to get respective reflectance value
    pixel_index = []

    # keep wavelength values and index in range 460-530
    for index, wavelength in enumerate(wavelengths):
        if wavelength_range[0] <= wavelength <= wavelength_range[1]:
            pixel_index.append(index)
            reduced_wavelengths.append(wavelength)

    # reduced pixel values to match the index of respective wavelength values
    pixel = [value for index, value in enumerate(pixel) if index in pixel_index]

    # plot spectral signature
    fig, ax = plt.subplots()
    ax.plot(reduced_wavelengths, pixel)
    ax.set(xlabel="wavelengths", ylabel="reflectance", title=f"Pixel {row}x{col}")
    ax.grid()
    fig.savefig("plot.png")
    plt.show()


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
