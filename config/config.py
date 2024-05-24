from dataclasses import dataclass, fields
import os
from pathlib import Path

class Config:
    """
    A configuration class that encapsulates two nested dataclasses: Paths and Vars.
    Paths contains configurations related to file and directory paths within the project.
    Vars contains configurations for various operational parameters, typically sourced from environment variables.
    
    Attributes:
        Paths: A dataclass containing path-related configurations.
        Vars: A dataclass containing operational parameters and environment variables.
    """
    
    @dataclass(frozen=True)
    class Paths:
        """
        A dataclass for managing file and directory paths in the project.
        
        Attributes:
            ROOT_PATH (Path): The root directory of the project.
            CSV_DATA_PATH (Path): The directory path for csv data files.
            JSON_DATA_PATH (Path): The directory path for json data files.
            json: A dictionary containing the names and paths of all json files in the JSON_DATA_PATH directory.
            csv: A dictionary containing the names and paths of all csv files in the CSV_DATA_PATH directory.
        """
        ROOT_PATH: Path = Path(__file__).parent.parent
        JSON_DATA_PATH: Path = ROOT_PATH / 'data' / 'json'
        CSV_DATA_PATH: Path = ROOT_PATH / 'data' / 'csv'
        
        json = {
            path.stem: path for path in JSON_DATA_PATH.iterdir() if path.as_posix().endswith('.json')
        }
        csv = {
            path.stem: path for path in CSV_DATA_PATH.iterdir() if path.as_posix().endswith('.csv')
        }
    
    @dataclass(frozen=True)
    class Vars:
        """
        A dataclass for managing operational parameters, typically sourced from environment variables.
        
        Attributes:
            Attr (dtype):
        """
        pass
    
if __name__=='__main__':
    
    for name, path in Config.Paths.json.items():
        print(name, path)
    
    for var in fields(Config.Vars):
        print(getattr(Config.Vars, var.name))