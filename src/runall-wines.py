import importlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as pit

subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

subset.main('data/raw/winemag-data-130k-v2.csv')
plotwines.main('data/interim/2018-05-09-winemag_priceGBP.csv')
county_sub.main('data/interim/2018-05-09-winemag_priceGBP.csv Chile')

raw_data = "data/raw/winemag-data-130k-v2.csv"
country = "Chile"

if __name__ == '__main__':
    subset_file = subset.process_data_GBP(raw_data)
    print(subset_file)
    plotwines.create_plots(subset_file)
    country_file = contry_sub.get_country(subset_file, country)
    print(country_file