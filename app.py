import streamlit as st
import pickle
import requests

# ---------------- PAGE ----------------
st.title("🎬 Movie Recommender System")

API_KEY = "cb18efc97da0033cd559d9fb10bb4034"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"
PLACEHOLDER = "https://via.placeholder.com/300x450?text=No+Image"

# ---------------- FETCH POSTER ----------------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {"api_key": API_KEY}
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return PLACEHOLDER

        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return IMAGE_BASE_URL + poster_path
        else:
            return PLACEHOLDER

    except:
        return PLACEHOLDER

# ---------------- LOAD DATA ----------------
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies_list = movies["title"].values

# ---------------- SELECT MOVIE ----------------
selected_movie = st.selectbox("Select a movie", movies_list)

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, reverse=True, key=lambda x: x[1])

    names = []
    posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]["id"]   # change to movie_id if needed
        names.append(movies.iloc[i[0]]["title"])
        posters.append(fetch_poster(movie_id))

    return names, posters

# ---------------- BUTTON ----------------
if st.button("Show Recommendation"):
    movie_names, movie_posters = recommend(selected_movie)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(movie_names[i])
            if movie_posters[i] == PLACEHOLDER:
                st.text("Poster not available")
                st.image(PLACEHOLDER)
            else:
                st.image(movie_posters[i])








