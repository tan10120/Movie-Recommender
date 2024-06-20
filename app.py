import streamlit as st
import pickle
import pandas as pd
import requests  #for fetching the posters

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0def7954808ba72905ec27835b980e61&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances =similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_posters.append(fetch_poster(movie_id))  # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)  # since we want the name of the movies and not their indexes

    return recommended_movies,recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
#st.title("IT'S MOVIE TIME\n ")
video_file = open('2022 Year in Film __ Movie Mashup.mp4', 'rb')
video_bytes = video_file.read()

st.header("MOVIE RECOMMENDER")
st.video(video_bytes)

st.header("THERE YOU GO")
selected_movie_name= st.selectbox(
    '|| What kind of movie do you want me to recommend you? ||',
    movies['title'].values)
if st.button('RECOMMEND'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        print("\n")
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])


