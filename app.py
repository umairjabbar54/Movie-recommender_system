import streamlit as st
import pickle
import pandas as pd
import requests

# Set page layout to wide mode
st.set_page_config(layout="wide")

st.title("Movie Recommender System")

# Load your pickled dataset and similarity matrix
movies_list = pickle.load(open('movies.pkl', 'rb'))

# Handle case if movies_list is saved as a dictionary
if isinstance(movies_list, dict):
    movies = pd.DataFrame(movies_list)
else:
    movies = movies_list

similarity = pickle.load(open('similarity.pkl', 'rb'))


# Function to fetch poster using TMDB API
def fetch_poster(movie_id):
    api_key = "b0ac8e420cf77aecb4fada4f64dd94e2"# Standard TMDb API key for recommender projects
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    try:
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception:
        pass

    # Fallback image if poster fetching fails
    return "https://via.placeholder.com/500x750?text=Poster+Not+Found"


# Recommender function using your 'id' column
def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]

    # Sort and take top 5 matches (excluding index 0)
    sorted_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_names = []
    recommended_posters = []

    for i in sorted_movies:
        # Changed from movie_id to id based on your dataset column
        movie_id = movies.iloc[i[0]].id
        recommended_names.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_names, recommended_posters


# Dropdown to select a movie
selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)

# Recommend Button
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    # Streamlit columns layout for displaying 5 posters side-by-side
    col1, col2, col3, col4, col5 = st.columns(5)

    columns = [col1, col2, col3, col4, col5]
    for i in range(5):
        with columns[i]:
            st.text(names[i])
            st.image(posters[i], use_container_width=True)


