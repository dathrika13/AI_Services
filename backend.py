from src import index
from src import utils
from src import pgutils as pgu

logger = utils.custom_logger(__name__)

async def index_document(path: str, collection: str, job_id: str): 
    try:
        # initiate job/task in the database
        # [do stuff]
        # index document
        doc = index.Document(path, collection)
        doc.index_document()
        logger.info(f"Document indexed: {path}")
        # update job/task status in the database
        return True
    except Exception as e:
        # update job/task status in the database
        logger.error(f"Error indexing document: {path}")
        logger.error(e)
        return False