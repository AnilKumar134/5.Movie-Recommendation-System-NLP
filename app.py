import streamlit as st 
import pickle
import pandas as pd
import requests


def fetch_url(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=eb1447531057fd141f826e18f2c7754e&language=en-US".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def Recommend_movie(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recomm_movie=[]
    recomm_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id
        recomm_movie.append(movies.iloc[i[0]].title)
        recomm_poster.append(fetch_url(movie_id))
    return recomm_movie,recomm_poster


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))



st.title("Movie Recommender System")

selected_movie_name=st.selectbox(
"Movie name",movies['title'].values
)

if st.button("Recommend"):
    names,posters=Recommend_movie(selected_movie_name)
    col0, col1,col2, col3,col4 = st.columns(5)
    col_list=[col0, col1,col2, col3,col4]
    for i, col in enumerate(col_list):
        with col:
            st.write(names[i])
            st.image(posters[i])
