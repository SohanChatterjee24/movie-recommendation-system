#importing necessary packages
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

df = pd.read_csv("../data/processed_file.csv")

#tfidf vectorisation
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["soup"])

#computing cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

#reverse map of indices and movie titles
indices = pd.Series(df.index, index=df["title"]).drop_duplicates()

#recommendation system
def recommend(title, num_recommendations=10):
    if title not in indices:
        return f"Movie {title} not found in dataset."
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return df["title"].iloc[movie_indices].tolist()

#example usage
movie_name = "The Dark Knight"
recommendations = recommend(movie_name, 10)

print(f"Top 10 recommendations for {movie_name}:")
for i, rec in enumerate(recommendations, 1):
    print(f"{i}. {rec}")