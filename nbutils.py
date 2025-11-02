import os
import wget
import zipfile
import json
import numpy as np
import pandas as pd
from ast import literal_eval

def fast_parse_vector(vector_str):
    """Much faster than literal_eval for numeric arrays"""
    try:
        # json.loads is often faster than literal_eval for arrays
        return json.loads(vector_str)
    except:
        # Fallback to literal_eval if json fails
        return ast.literal_eval(vector_str)

def read_wikipedia_sample_fast(data_path: str = './data/', 
                              file_name: str = "vector_database_wikipedia_articles_embedded",
                              n_rows: int = 300) -> pd.DataFrame:
    csv_file_path = os.path.join(data_path, file_name + ".csv")
    
    print(f"Loading first {n_rows} rows...")
    data = pd.read_csv(csv_file_path, nrows=n_rows)
    
    print("Processing title vectors...")
    data['title_vector'] = data['title_vector'].apply(fast_parse_vector)
    
    print("Processing content vectors...")
    data['content_vector'] = data['content_vector'].apply(fast_parse_vector)
    
    data['vector_id'] = data['vector_id'].apply(str)
    
    return data

def download_wikipedia_data(
    data_path: str = './data/',
    download_path: str = "./",
    file_name: str = "vector_database_wikipedia_articles_embedded") -> pd.DataFrame:

    data_url = 'https://cdn.openai.com/API/examples/data/vector_database_wikipedia_articles_embedded.zip'

    csv_file_path = os.path.join(data_path, file_name + ".csv")
    zip_file_path = os.path.join(download_path, file_name + ".zip")
    if os.path.isfile(csv_file_path):
        print("File Downloaded")
    else:
        if os.path.isfile(zip_file_path):
            print("Zip downloaded but not unzipped, unzipping now...")
        else:
            print("File not found, downloading now...")
            # Download the data
            wget.download(data_url, out=download_path)

        # Unzip the data
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(data_path)

        # Remove the zip file
        os.remove('vector_database_wikipedia_articles_embedded.zip')
        print(f"File downloaded to {data_path}")


def read_wikipedia_sample(data_path: str = './data/', 
                         file_name: str = "vector_database_wikipedia_articles_embedded",
                         n_rows: int = 10000) -> pd.DataFrame:
    """Load only first n_rows for testing"""
    csv_file_path = os.path.join(data_path, file_name + ".csv")
    
    print(f"Loading first {n_rows} rows...")
    data = pd.read_csv(csv_file_path, nrows=n_rows)
    
    print("Processing vectors...")
    data['title_vector'] = data['title_vector'].apply(literal_eval)
    data['content_vector'] = data['content_vector'].apply(literal_eval)
    data['vector_id'] = data['vector_id'].apply(str)
    
    return data

# Start with a small sample
sample_data = read_wikipedia_sample(n_rows=1000)
