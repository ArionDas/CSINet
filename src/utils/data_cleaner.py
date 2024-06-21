import numpy as np
import pandas as pd
from pathlib import Path

from utils.data_loader import DataLoader
from config import Config

class DataCleaner:
    """A class for cleaning and processing data."""

    def __init__(self, data: pd.DataFrame):
        """
        Initialize DataCleaner with data.

        Args:
            data (pd.DataFrame): The input DataFrame.
        """
        
        self.data = data

    def clean_claim(self):
        """Clean claims data."""
        
        clean_claims_func = lambda claims: [{
            'start': claim['start'],
            'end': claim['end']
        } for claim in claims]
        
        self.data['claims'] = self.data['claims'].apply(np.frompyfunc(clean_claims_func, 1, 1))

    def add_claim_idx(self):
        """Add claim index to data."""
        
        claim_idx = lambda claims: set().union(*[set(range(claim['start'], claim['end'])) for claim in claims])
        
        self.data['claim_idx'] = self.data['claims'].apply(np.frompyfunc(claim_idx, 1, 1))

    def add_claim_vector(self):
        """Add claim vector to data."""
        
        claim_vector = lambda tokens, claim_idx: [1 if i in claim_idx else 0 for i in range(len(tokens))]
        
        self.data['claim_vector'] = self.data.apply(
            lambda row: claim_vector(row['text_tokens'], row['claim_idx']),
            axis=1
        )
    
    def save_clean_data(self, path: str):
        """Save cleaned data to a file."""
        
        self.data.to_csv(path, index=False)

if __name__ == '__main__':
    
    for json_path in Config.Paths.json.values():
        data = pd.read_json(json_path)
        cleaner = DataCleaner(data)
        cleaner.clean_claim()
        cleaner.add_claim_idx()
        cleaner.add_claim_vector()
        csv_path = json_path.parent.parent / 'csv' / json_path.stem
        cleaner.save_clean_data(csv_path.with_suffix('.csv'))