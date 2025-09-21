import streamlit as st
from pipeline.pipeline import RecommendationPipeline
from dotenv import load_dotenv


st.set_page_config(page_title="Recommendation Pipeline", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return RecommendationPipeline()

pipeline = init_pipeline()
st.title("Recommendation Pipeline")

query = st.text_input("Enter your query, e.g. Any query at all")
if query:
    with st.spinner("Fetching recommendations..."):
        response = pipeline.recommend(query)
        st.markdown(f"**Query:** {query}")
        st.write(response)

