from langchain.chains.retrieval_qa.base import create_retrieval_chain  # New recommended method
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        # Initialize the language model using Groq and Gemini/Qwen or other supported model
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)

        # Load a custom prompt for anime recommendations
        self.prompt = get_anime_prompt()

        # Create the retrieval-based QA chain using the retriever and custom prompt
        self.qa_chain = create_retrieval_chain(
            retriever=retriever,  # Vector store retriever
            combine_docs_chain_kwargs={"prompt": self.prompt},  # Pass custom prompt to chain
            llm=self.llm,  # The language model to generate responses
            return_source_documents=True  # Optional: include source docs in the response
        )

    def get_recommendation(self, query: str):
        # Run the QA chain with user query and return the generated answer
        result = self.qa_chain.invoke({"query": query})
        return result["result"]  # 'answer' key contains the main output
