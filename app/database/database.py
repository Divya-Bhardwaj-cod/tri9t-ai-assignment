from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///ct200.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

from app.models.document import Document
from app.models.document_version import DocumentVersion
from app.models.document_node import DocumentNode

from app.models.document import Document
from app.models.document_version import DocumentVersion
from app.models.document_node import DocumentNode
from app.models.selection import Selection
from app.models.selection_node import SelectionNode



Base.metadata.create_all(bind=engine)