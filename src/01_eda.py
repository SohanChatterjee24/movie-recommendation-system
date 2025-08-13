#importing necessary files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ast
from collections import Counter

df = pd.read_csv("../data/tmdb_5000_movies.csv")
print(df.info())
print(df.describe(include="all"))

#datacleaning
df.drop(columns=["homepage", "tagline"], inplace=True)
df.dropna(inplace=True)

#top genres
def extract_genres(x):
    try:
        genres = ast.literal_eval(x)
        return [g["name"] for g in genres]
    except:
        return []
df["genre_list"] = df["genres"].apply(extract_genres)

all_genres = sum(df["genre_list"], [])
genre_count = pd.Series(Counter(all_genres)).sort_values(ascending=False).reset_index()
print("\nTop Genres:\n", genre_count)
genre_count.columns = ["Genre", "Count"]

#release year
df["release_year"] = pd.to_datetime(df["release_date"], errors="coerce").dt.year
release_year_counts = df["release_year"].value_counts().sort_index()
print("\nYear Range:", release_year_counts.min(), " to ", release_year_counts.max())

print("\nTop 10 Movies by Revenue:\n", df.nlargest(10, "revenue")[["title", "revenue"]])
print("\nTop 10 Movies by Popularity:\n", df.nlargest(10,"popularity")[["title", "popularity"]])
print("\nTop Movies by Vote Average:\n", df.nlargest(10, "vote_average")[["title", "vote_average"]])

#Top 10 Genre Distribution Plot
plt.figure(figsize=(10,6))
sns.barplot(data=genre_count.head(10), x="Genre", y="Count", palette="viridis")
plt.title("Top Genres by Movie Count")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

#Release Year Distribution Plot
plt.figure(figsize=(17,6))
release_year_counts.plot(kind="bar")
plt.title("Number of Movies Released per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

#Revenue Distribution Plot
plt.figure(figsize=(12,6))
sns.histplot(df["revenue"], bins=50, kde=True)
plt.title("Revenue Distribution")
plt.xlabel("Revenue in Billions USD")
plt.show()

#Popularity Distribution Plot
plt.figure(figsize=(12,6))
sns.histplot(df["popularity"], bins=50, kde=True)
plt.title("Popularity Distrubution")
plt.xlabel("Popularity")
plt.show()

#extracting keywords_list
df["keywords_list"] = df["keywords"].apply(extract_genres)

#clean text
df["genre_list"] = df["genre_list"].apply(lambda x: [i.replace(" ","") for i in x])
df["keywords_list"] = df["keywords_list"].apply(lambda x: [i.replace(" ","") for i in x])

#creating a "soup" column
df["soup"] = (
    df["overview"] + " " +
    df["genre_list"].apply(lambda x: " ".join(x)) + " " +
    df["keywords_list"].apply(lambda x: " ".join(x))
)
df = df.reset_index(drop=True)

#saving file
df.to_csv("../data/processed_file.csv", index=False)