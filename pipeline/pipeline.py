from src.vector_store import VectorStoreBuilder
from src.recommender import Recommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class RecommendationPipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            logger.info("Initializing recommendation pipeline")
            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = vector_builder.load_vector_store().as_retriever()
            self.recommender = Recommender(retriever, GROQ_API_KEY, model_name=MODEL_NAME)
            logger.info("Pipeline initialized")
        except Exception as e:
            logger.error(f"Failed to initialize pipeline {str(e)}")
            #Adding this line for testing purposes only
            #This is not good practice
            raise CustomException("Error during pipeline initialization")
    
    def recommend(self, query:str) -> str:
        try:
            logger.info(f"Received a query {query}")
            recommdation = self.recommender.get_recommendation(query)
            logger.info(f"Recommendation generated successfully")
        except Exception as e:
            logger.error(f"Failed to initialize pipeline {str(e)}")