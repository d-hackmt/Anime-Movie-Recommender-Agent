import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        # Read the original CSV file, ignoring bad lines and dropping rows with any NaNs
        df = pd.read_csv(
            self.original_csv,
            encoding='utf-8',
            on_bad_lines='skip'
        ).dropna()

        # Define the required columns
        required_cols = {'Name', 'Genres', 'synopsis'}  # Fixed typo: was 'sypnopsis'

        # Check for missing required columns
        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError("Missing column in CSV file")

        # Combine fields to prepare data for Retrieval-Augmented Generation (RAG)
        df['combined_info'] = (
            "Title :" + df['Name'] + "..Overview :" + df['synopsis'] + "Genres : " + df['Genres']
        )

        # Save the combined information to a new processed CSV file
        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv
