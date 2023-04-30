import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
movies = pd.read_csv('movies.csv')

# Get the top 10 highest rated movies
top_rated = movies.sort_values(by='rating', ascending=False).head(10)

# Plot a bar chart of the top 10 highest rated movies
plt.bar(top_rated['title'], top_rated['rating'])
plt.xticks(rotation=90)
plt.show()
