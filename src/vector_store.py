# data csv loader
from langchain_community.document_loaders.csv_loader import CSVLoader

# to separate our text based on chunks
from langchain_text_splitters import CharacterTextSplitter

# embeddings 
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# vectordb
from langchain_community.vectorstores import Chroma

# load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

class VectorStorBuilder:
    def __init__(self , csv_path:str , persist_dir:str="chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        # Initialize the embedding model using Gemini embedding model
        self.embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        
    def build_and_save_vectorstore(self):
        # Load CSV file using LangChain's CSVLoader
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding='utf-8',
            metadata_columns=[]  # No additional metadata columns
        )

        # Load the content from CSV
        data = loader.load()

        # Split text into chunks using a character-based text splitter
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        text = splitter.split_documents(data)

        # Convert text chunks into vector embeddings and store in Chroma DB
        db = Chroma.from_documents(
            documents=text,
            embedding=self.embedding,
            persist_directory=self.persist_dir
        )

        # Save the vector store to disk
        db.persist()

    def load_vec_store(self):
        # Load and return the Chroma vector store from disk
        return Chroma(persist_directory=self.persist_dir, embedding_function=self.embedding)
