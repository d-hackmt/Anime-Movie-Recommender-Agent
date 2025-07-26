from src import vector_store
from src.data_loader import AnimeDataLoader 
from src.vector_store import VectorStorBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

# Load environment variables from .env file
load_dotenv()

# Initialize logger
logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipeline")
        
        # Load and process the original anime dataset
        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")
        processed_csv = loader.load_and_process()
        
        logger.info("Data loaded and processed")
        
        # Create the vector store from the processed CSV
        vector_builder = VectorStorBuilder(csv_path=processed_csv)
        vector_builder.build_and_save_vectorstore()
        
        logger.info("Vector store built successfully")  
        logger.info("Pipeline built successfully")      
        
    except Exception as e:
        logger.error(f"Failed to build pipeline: {str(e)}")
        raise CustomException("Error during pipeline building")  


if __name__ == "__main__":
    main()