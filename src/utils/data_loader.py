from typing import Literal
import numpy as np
import pandas as pd

from config import Config

class DataLoader():
    """
    A class used to load data from JSON and CSV files.

    ...

    Methods
    -------
    load_json_data(dataset_type: Literal['train', 'val'], lang: Literal['en', 'hi']) -> pd.DataFrame
        Loads data from a JSON file based on the dataset type and language.

    load_csv_data(dataset_type: Literal['train', 'val'], lang: Literal['en', 'hi']) -> pd.DataFrame
        Loads data from a CSV file based on the dataset type and language.
    """
    
    @staticmethod
    def load_json_data(
        dataset_type: Literal['train', 'val'],
        lang: Literal['en', 'hi']
    ):
        df = pd.read_json(Config.Paths.json[f'{dataset_type}-{lang}'])
        return df

    @staticmethod
    def load_csv_data(
        dataset_type: Literal['train', 'val'],
        lang: Literal['en', 'hi']
    ):
        df = pd.read_csv(Config.Paths.csv[f'{dataset_type}-{lang}'])
        return df