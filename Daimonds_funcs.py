import pandas as pd
from enum import Enum

class Selection(Enum):
    print("Diamonds Data Analysis Menu")
    Check_the_highest_price_of_diamonds=1
    Check_the_average_price_of_diamonds=2
    Check_how_many_diamonds_of_type_Ideal_exist=3
    Check_unique_diamond_colors_and_how_many_there_are=4
    Check_the_median_carat_for_Premium_diamonds=5
    Calculate_the_average_carat_per_type_of_cut=6
    Get_the_carat_values_for_Premium_diamonds=7
    Exit=8

file_path = "Daimonds_data.csv"
diamonds_df = pd.read_csv(file_path)

def menu():
    for i in Selection:
        print(f'{i.value} - {i.name}')
    return Selection(int(input("Your selection: ")))


# 1. Check the highest price of diamonds:
def highest_price():
    highest_price = diamonds_df['price'].max()
    print(f"Highest Price: {highest_price}")


# 2. Check the average price of diamonds:
def average_price():
    average_price = diamonds_df['price'].mean()
    print(f"Average Price: {average_price:.2f}")

# 3. Check how many diamonds of type 'Ideal' exist:
def ideal_count():
    ideal_count = diamonds_df[diamonds_df['cut'] == 'Ideal'].shape[0]
    print(f"Number of Ideal diamonds: {ideal_count}")

# 4. Check unique diamond colors and how many there are:
def color():
    unique_colors = diamonds_df['color'].unique()
    unique_count = len(unique_colors)
    print(f"Unique Colors: {unique_colors}")
    print(f"Number of Colors: {unique_count}")


# 5. Check the median carat for Premium diamonds:
def median_carat_PR():
    median_carat_premium = diamonds_df[diamonds_df['cut'] == 'Premium']['carat'].median()
    print(f"Median Carat for Premium diamonds: {median_carat_premium}")


# 6. Calculate the average carat per type of cut
def average_carat_per_cut():
    average_carat_per_cut = diamonds_df.groupby('cut')['carat'].mean()
    print("Average Carat per Cut:")
    print(average_carat_per_cut)


# 7. Get the carat values for Premium diamonds
def carat_for_PR_diamonds():
    premium_carat_values = diamonds_df[diamonds_df['cut'] == 'Premium']['carat']
    print("Average Carat per Cut:")
    print(average_carat_per_cut)
    print("Carat values for Premium diamonds:")
    print(premium_carat_values)

def main():
    # Load the dataset
    file_path = "Daimonds_data.csv"
    diamonds_df = pd.read_csv(file_path)

    while True:
        user_selection = menu()
        if user_selection == Selection.Check_the_highest_price_of_diamonds:
            highest_price()
        elif user_selection == Selection.Check_the_average_price_of_diamonds:
            average_price()
        elif user_selection == Selection.Check_how_many_diamonds_of_type_Ideal_exist:
            ideal_count()
        elif user_selection == Selection.Check_unique_diamond_colors_and_how_many_there_are:
            color()
        elif user_selection == Selection.Check_the_median_carat_for_Premium_diamonds:
            median_carat_PR()
        elif user_selection == Selection.Calculate_the_average_carat_per_type_of_cut:
            average_carat_per_cut()
        elif user_selection == Selection.Get_the_carat_values_for_Premium_diamonds:
            carat_for_PR_diamonds()
        elif user_selection == Selection.Exit:
            print("Exiting the program. Goodbye!")
            break