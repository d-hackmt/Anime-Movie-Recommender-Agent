from src.vector_store import VectorStorBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

# Initialize logger for this module
logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline")
            
            # Empty CSV path because we're only loading the existing vector store (not creating it)
            vector_builder = VectorStorBuilder(csv_path="", persist_dir=persist_dir)
            
            # Load retriever from persisted Chroma vector store
            retreiver = vector_builder.load_vec_store().as_retriever()
            
            # Initialize the AnimeRecommender with retriever, API key, and model name
            self.recommender = AnimeRecommender(
                retriever=retreiver,
                api_key=GROQ_API_KEY,
                model_name=MODEL_NAME
            )
            
            logger.info("Pipeline initialized successfully.")
        
        except Exception as e:
            logger.error(f"Failed to initialize pipeline: {str(e)}")
            raise CustomException("Pipe mai problem hai")  # Custom message (intentionally kept informal as per your logic)

    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Received a query: {query}")  # Fixed string interpolation with f-string
            
            # Get recommendation from the recommender
            recommendation = self.recommender.get_recommendation(query)
            
            logger.info("Recommendation generated successfully.")
            return recommendation
        
        except Exception as e:
            logger.error(f"Failed to get recommendation: {str(e)}")
            raise CustomException("Error during getting recommendation")  