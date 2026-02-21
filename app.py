# Netflix Data Analysis 
# - Movies vs TV Shows analysis 
# - Year-wise growth trend 
# - Country distribution 
# - Most common genre 

import pandas as pd
df = pd.read_csv('Netflix_Synthetic_Large_Dataset_2025.csv')
print(df.head())

# - Movies vs TV Shows analysis 
print('Total Movies:', df[df['Type'] == 'Movie'].shape[0])
print('Total TV Shows:', df[df['Type'] == 'TV Show'].shape[0])
# Percentage share
print('Percentage Share',df['Type'].value_counts(normalize=True)*100)

# - Year-wise growth trend 
year = df['Release_Year'].value_counts().sort_index()
print(year)
peak_year = year.idxmax()
print('peak_year:',peak_year)

# - Country distribution 
country_dist = df['Country'].value_counts()
print('Country Distribution:',country_dist)
print('Top Country:',country_dist.idxmax())

# - Most common genre 
genre_dist = df['Genres'].value_counts()
print('Most Common Genre:', genre_dist.idxmax())
