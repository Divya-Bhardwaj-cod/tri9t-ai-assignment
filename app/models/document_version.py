from sqlalchemy import Column, Integer, ForeignKey

from app.database.database import Base


class DocumentVersion(Base):

    __tablename__ = "document_versions"

    id = Column(Integer, primary_key=True)

    document_id = Column(
        Integer,
        ForeignKey("documents.id")
    )

    version_number = Column(Integer, nullable=False)