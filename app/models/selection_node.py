from sqlalchemy import Column, Integer, ForeignKey

from app.database.database import Base


class SelectionNode(Base):

    __tablename__ = "selection_nodes"

    id = Column(Integer, primary_key=True)

    selection_id = Column(
        Integer,
        ForeignKey("selections.id")
    )

    node_id = Column(
        Integer,
        ForeignKey("document_nodes.id")
    )