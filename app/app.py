## all the logic for our application 

import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender" , layout="wide")

load_dotenv()

# to initialize our anime recommender pipeline

def init_pipeline():
    return AnimeRecommendationPipeline()

# by doing this we can use pipleine functions anywhere

pipeline = init_pipeline()

st.title("Anime Recommender System")
st.text("where you give you preferences and we tell you about the similar ones")

query = st.text_input("Enter your anime preferences" , placeholder="Ligh Hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you ..."):
        response = pipeline.recommend(query=query)
        st.markdown('### Recommendations')
        st.write(response)
