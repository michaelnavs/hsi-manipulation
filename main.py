"""
Author: Michael Navarro

This program will open a HSI file and display spectral signature of a pixel in 
wavelength range of 460-530
"""
import sys
from typing import List, Tuple
from spectral import open_image, imshow, get_rgb, BandInfo
from scipy.stats import linregress
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import pandas as pd


def reduce_dataset(wavelengths: List, wavelength_range: Tuple) -> Tuple[List, List]:
    reduced_wavelengths = []  # store desired wavelength values
    # store index of wavelength values above to get respective reflectance value
    pixel_indices = []

    # keep wavelength values and index in range 460-530
    for index, wavelength in enumerate(wavelengths):
        if wavelength_range[0] <= wavelength <= wavelength_range[1]:
            pixel_indices.append(index)
            reduced_wavelengths.append(wavelength)

    return reduced_wavelengths, pixel_indices


def main() -> None:
    img = open_image("./dataset/first_data_2_12_2021.bil.hdr")
    rows, cols = img.shape[0], img.shape[1]
    wavelengths = img.bands.centers  # get wavelengths
    wavelength_range = (460, 530)  # store desired wavelength range values
    reduced_wavelengths, pixel_indices = reduce_dataset(wavelengths, wavelength_range)
    writer = pd.ExcelWriter("dataset.xlsx", engine="xlsxwriter")

    slopes = []

    for row in range(rows):
        print(f"Working on row {row}")
        row_slopes = []
        for col in range(cols):
            pixel = img.read_pixel(row, col)  # get reflectance values
            # reduced pixel values to match the index of respective wavelength values
            pixel = [
                value for index, value in enumerate(pixel) if index in pixel_indices
            ]
            # calculate slope using scipy.stats.linregress
            slope = linregress(reduced_wavelengths, pixel).slope
            row_slopes.append(slope)
        slopes.append(row_slopes)

    slopes_df = pd.DataFrame(slopes)
    slopes_df.to_excel(writer, sheet_name="data", index=False)

    writer.save()


if __name__ == "__main__":
    main()
