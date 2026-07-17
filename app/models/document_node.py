from sqlalchemy import Column, Integer, String, Text, ForeignKey

from app.database.database import Base


class DocumentNode(Base):

    __tablename__ = "document_nodes"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    number = Column(String)

    level = Column(Integer)

    body = Column(Text)

    content_hash = Column(String)

    version_id = Column(
        Integer,
        ForeignKey("document_versions.id")
    )

    parent_id = Column(
        Integer,
        ForeignKey("document_nodes.id")
    )