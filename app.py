import pandas as pd
from enum import Enum
from Daimonds_funcs import average_carat_per_cut, average_price, carat_for_PR_diamonds, color, highest_price, ideal_count, main, median_carat_PR

# Load the dataset
file_path = "Daimonds_data.csv"
diamonds_df = pd.read_csv(file_path)

if __name__=='__main__':
    while True:
      main()