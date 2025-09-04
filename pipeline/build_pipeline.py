from src.data_loader import RecommederDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()
logger = get_logger(__name__)

#this pipeline will create the vector store
def main():
    try:
        logger.info("Start build")
        loader = RecommederDataLoader("data/movie_synopsis.csv", "data/movie_processed.csv")
        processed_csv = loader.load_and_process()
        logger.info("Data loaded and processed")
        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstore()
        logger.info("vector store built successfully ... and ipeline built")
    except Exception as e:
        logger.error(f"Error in initializing pipeline {str(e)}")
        raise CustomException("Error during pipeline initialization", e)

#start pipeline
if __name__ == "__main__":
    main()