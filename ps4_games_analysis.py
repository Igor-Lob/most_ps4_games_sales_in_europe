import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Loading the dataset
sales = pd.read_csv('PS4_GamesSales.csv', encoding='latin1')

# Displaying the first rows of the data for inspection
sales.head()

# Creating a list with the columns we want: 'Name', 'Year_of_Release', 'Genre', and 'Publisher'
game_details = sales[['Game', 'Year', 'Genre', 'Publisher']]

# Now, let's sort the games by the 'Europe' column, which represents sales in Europe
most_sale_games_in_europe = sales.sort_values(by='Europe', ascending=False)

# Creating a new dataframe with the top games in Europe, showing only the columns of interest
top_games_europe = most_sale_games_in_europe[['Game', 'Year', 'Genre', 'Publisher']]

# Displaying the list of top-selling games in Europe
print(top_games_europe.head())

