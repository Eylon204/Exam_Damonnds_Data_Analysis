# Diamonds Data Analysis

## Overview
This project provides a menu-driven interface for performing data analysis on a dataset of diamonds using Python. The analysis includes checking the highest and average price of diamonds, finding out how many diamonds of a certain type exist, checking unique diamond colors, and other related statistics.

## Features
The project includes the following functionalities:
1. Check the highest price of diamonds.
2. Check the average price of diamonds.
3. Check how many diamonds of type "Ideal" exist.
4. Check unique diamond colors and how many there are.
5. Check the median carat for "Premium" diamonds.
6. Calculate the average carat per type of cut.
7. Get the carat values for "Premium" diamonds.

## Files Included
- **app.py**: The main application file that contains the menu and functions to handle user selections.
- **Daimonds_funcs.py**: Contains various functions that perform specific analysis tasks, such as calculating averages and medians.
- **Daimonds_data.csv**: The dataset of diamonds used in this analysis.
- **requirements.txt**: A file containing the list of dependencies needed to run the project.

## How to Run
1. Install the required dependencies by running:
    ```bash
   pip install -r requirements.txt
    ```
   	2.	Run the main program:
    ```bash
    python app.py.

## Dataset

The dataset Daimonds_data.csv is a CSV file that contains information about different diamonds, including attributes such as price, carat, cut, and color.

### Menu Options

Upon running the program, a menu will be displayed where you can select from the following options:

	•	1: Check the highest price of diamonds
	•	2: Check the average price of diamonds
	•	3: Check how many diamonds of type Ideal exist
	•	4: Check unique diamond colors and how many there are
	•	5: Check the median carat for Premium diamonds
	•	6: Calculate the average carat per type of cut
	•	7: Get the carat values for Premium diamonds
	•	8: Exit the program

## Dependencies

The project uses several Python libraries, which are listed in the requirements.txt file. Key libraries include:

	•	pandas: For data manipulation and analysis.
	•	Flask: For possible future extensions with a web interface.

### To install the dependencies, run:
pip install -r requirements.txt

License

This project is open-source and available for modification and distribution under the MIT License.

Author

Eylon Levy
This `README.md` provides a clear overview of your project, including instructions on how to run it, what files are included, and what each option in the menu does. You can modify it further according to your needs!