# 🎬 Movie Recommendation System

A content-based movie recommendation system built using the TMDB 5000 Movies dataset. The system recommends movies similar to a user-selected title based on metadata such as genres, cast, crew, keywords, and overview.

## 📁 Dataset

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

## 🚀 Features

- Extracts and cleans metadata from movie datasets
- Uses NLP techniques (lemmatization, stopword removal, etc.)
- Calculates similarity using cosine similarity over bag-of-words vectors
- Built with Streamlit for an interactive web interface

## 📦 Installation

**Note:** You may also need to download NLTK resources:
```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```

## 🧠 How It Works

- The metadata (genres, keywords, cast, crew, and overview) is combined into a single "tags" column.
- Text is processed using lemmatization.
- `CountVectorizer` creates a bag-of-words model of the 5000 most common words.
- Cosine similarity is calculated between all movie vectors.
- For a selected movie, the top 5 most similar movies are recommended.

## 💻 How to Run the App

The web app is built with **Streamlit** and runs using `app.py`.

```bash
streamlit run app.py
```

Once the server starts, it will open a browser tab where you can:

- Select a movie from the dropdown
- See the top 5 recommended similar movies

## ✅ Output Example

For **Avatar**, you may get recommendations like:

```
John Carter  
Aliens  
Battle: Los Angeles  
The Helix...Loaded  
The Matrix  
```

## 🛠️ Tools & Libraries

- Python
- Pandas, NumPy
- Scikit-learn
- NLTK
- Streamlit

## 📌 To Do

- Add poster/movie links via TMDB API
- Add genre/category filter
- Improve text preprocessing using TF-IDF or spaCy

## 🙌 Acknowledgements

- [Kaggle - TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
