
import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "test")
DB_CONNECTION_STRING = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DOCS_BUCKET = os.getenv("DOCS_BUCKET", "docs")
APP_RUNNER_BASE_URL = os.getenv("APP_RUNNER_BASE_URL", "http://localhost:8000")

PGVECTOR_HOST = os.getenv("PG_HOST", "localhost")
PGVECTOR_PORT = os.getenv("PG_PORT", "5432")
PGVECTOR_USER = os.getenv("PG_USER", "postgres")
PGVECTOR_PASSWORD = os.getenv("PG_PASSWORD", "password")
PG_CONNECTION_STRING = f"postgresql+psycopg2://{PGVECTOR_USER}:{PGVECTOR_PASSWORD}@{PGVECTOR_HOST}:{PGVECTOR_PORT}/postgres"


VECTOR_SIZE = 2048
DEFAULT_COLLECTION = "default"