from src import config
from src import utils

from typing import List
import boto3

def chunk_document(text: str, chunk_size: int = 1000, chunking_strategy: str=None) -> List[str]:
    """
    Split the document into chunks for indexing
    
    Args:
        text (str): text to chunk
        chunk_size (int): size of each chunk
        chunking_strategy (str): strategy to chunk the document
    
    Returns:
        List[str]: list of chunks
    """
    # return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    raise NotImplementedError

def generate_embeddings(text: str) -> List[float]:
    """
    Call bedrock API to generate embeddings

    Args:
        text (str): text to generate embeddings for
    
    Returns:
        List[float]: embeddings
    """
    raise NotImplementedError

def index_document(text: str, collection: str, metadata: dict):
    """
    Index the document to the postgres pgvector database
    
    Args:
        text (str): text to index
        collection (str): collection name
        metadata (dict): metadata of the document such as keywords and parent document path or title
    """
    embeds = generate_embeddings(text)
    raise NotImplementedError

class Document():
    def __init__(self, s3_path: str, collection: str = config.DEFAULT_COLLECTION):
        self.s3_path = s3_path
        self.collection = collection
        self.text = None
        self.embeddings = None
        self.metadata = None

        self.load_document()
    
    def load_document(self):
        # load the document from s3
        self.text = utils.load_file_from_s3(self.s3_path)
    
    def save_metadata(self, metadata: dict = {}):
        # save metadata to the database
        if not metadata:
            metadata = self.metadata
        raise NotImplementedError
    
    def index_document(self):
        # chunk the document to pgvector vector database
        chunks = chunk_document(self.text)
        self.metadata = {
            "s3_path": self.s3_path, 
            "collection": self.collection,
            "num_chunks": len(chunks),
            "keywords": [],
            }
        self.save_metadata()
        # generate embeddings
        for chunk in chunks:
            index_document(chunk, self.collection, self.metadata)
