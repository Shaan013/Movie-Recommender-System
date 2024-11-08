from operator import index

import requests
import streamlit as st
import pickle
import pandas as pd
from click import option
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    #st.text(data)
    # poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" +data["poster_path"]
   #st.text(full_path)
    return full_path


def recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distances =similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]

    recommenede_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        #movie_id = i[0]
        movie_id = movies.iloc[i[0]].id
        recommenede_movies.append(movies.iloc[i[0]].title)
       # st.text(movie_id)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommenede_movies ,recommended_movie_posters





movie_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))


st.title("🎬 Movie Recommender System")
st.markdown("<style>h1{text-align: center; color: #4A90E2;}</style>", unsafe_allow_html=True)

selected_movie_name = st.selectbox('Pick a movie to find similar recommendations', movies['title'].values)

if st.button('recommend'):
    recpmmendation,posters  = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recpmmendation[0])
        st.image(posters[0])
    with col2:
        st.text(recpmmendation[1])
        st.image(posters[1])

    with col3:
        st.text(recpmmendation[2])
        st.image(posters[2])
    with col4:
        st.text(recpmmendation[3])
        st.image(posters[3])
    with col5:
        st.text(recpmmendation[4])
        st.image(posters[4])

    #for i in recpmmendation:
       # st.write(i)
# Footer
st.markdown("""
    <hr style="border:1px solid #4A90E2">
    <div style="text-align:center;">
        <p>Made with ❤️ by Shaan Patel</p>
        <p>Powered by The Movie Database API</p>
          <a href="https://github.com/Shaan013" target="_blank"><img src="https://img.icons8.com/ios-glyphs/30/4A90E2/github.png"/></a>
            <a href="https://www.linkedin.com/in/shaan-patel-609879271/" target="_blank"><img src="https://img.icons8.com/ios-glyphs/30/4A90E2/linkedin.png"/></a>
    </div>
""", unsafe_allow_html=True)
