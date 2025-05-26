import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns 

sales = pd.read_csv('PS4_GamesSales.csv', encoding='latin1')

sales.head()

game_details = sales[['Game', 'Year', 'Genre', 'Publisher']]

most_sale_games_in_europe = sales.sort_values(by='Europe', ascending=False)

top_games_europe = most_sale_games_in_europe[['Game', 'Year', 'Genre', 'Publisher']]

print(top_games_europe.head())

top10_europe = sales.sort_values(by='Europe', ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x='Europe', y='Game', data=top10_europe, palette='viridis')
plt.title('Top 10 Jogos mais vendidos na Europa (PS4)')
plt.xlabel('Vendas na Europa (milhões)')
plt.ylabel('Nome do Jogo')
plt.tight_layout()
plt.show()

