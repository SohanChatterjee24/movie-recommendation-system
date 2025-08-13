# 🎬 Movie Recommendation System (Content-Based)

This project is a **Content-Based Movie Recommendation System** built using the [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).  
It recommends movies similar to a given title based on their **overview, genres, and keywords** using **TF-IDF** and **cosine similarity**.

---

## 📂 Dataset
The dataset used is `tmdb_5000_movies.csv`, which was cleaned and preprocessed into `processed_file.csv`:
- Removed irrelevant columns (`homepage`, `tagline`)
- Filled missing values with `"unknown"`
- Extracted and processed genres, keywords, and overview
- Created a combined text column (`soup`) for vectorization

---

## 🛠️ Tech Stack
- **Python 3**
- **Pandas** – Data processing  
- **Scikit-learn** – TF-IDF & cosine similarity  
- **Matplotlib / Seaborn** – EDA visualizations  

---

## 📊 Exploratory Data Analysis (EDA)
Key EDA steps:
- Checked missing values and handled them
- Extracted and analyzed top genres
- Visualized genre distribution
- Cleaned and saved the dataset as `processed_file.csv`

---

## 🚀 How It Works
1. **TF-IDF Vectorization**: Converts the combined text (`soup`) into numerical vectors while removing stop words.
2. **Cosine Similarity**: Measures similarity between movies based on vectorized text.
3. **Recommendation Function**: Returns top N most similar movies to a given title.

---

## 📜 Example Usage
```python
movie_name = "The Dark Knight"
recommendations = recommend(movie_name, 10)
print(recommendations)
