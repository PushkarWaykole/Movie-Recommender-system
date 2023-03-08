import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=861a17e8ac5cb0906ebfbafebd358f7a&language=en-US'.format(movie_id))
    data=response.json()
    # st.write(data)
    return "https://image.tmdb.org/t/p/w780"+data['poster_path']

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

st.title("Movie Recommender system")

selected_movie_name=st.selectbox("Enter the Movie based on which you want the recommendations",movies.title)

if st.button('Recommend'):
 
    recommendations,posters=recommend(selected_movie_name)
    
    
    with st.container():
        col1, col2, col3,col4,col5= st.columns(5)
        with col1:
            st.text(recommendations[0])
            st.image(posters[0])
        with col2:
            st.text(recommendations[1])
            st.image(posters[1])
        with col3:
            st.text(recommendations[2])
            st.image(posters[2])
        with col4:
            st.text(recommendations[3])
            st.image(posters[3])
        with col5:
            st.text(recommendations[4])
            st.image(posters[4])
        
    with st.container():
        col6,col7,col8,col9,col10 =st.columns(5)
        with col6:
            st.text(recommendations[5])
            st.image(posters[5])
        with col7:
            st.text(recommendations[6])
            st.image(posters[6])
        with col8:
            st.text(recommendations[7])
            st.image(posters[7])
        with col9:
            st.text(recommendations[8])
            st.image(posters[8])
        with col10:
            st.text(recommendations[9])
            st.image(posters[9])

    
st.header("Made with love by Pushkar")