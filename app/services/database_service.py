from app.database.database import SessionLocal
from app.models.document_node import DocumentNode
from app.services.hash_service import generate_hash


def save_node(node, version_id, parent_id=None):
    db = SessionLocal()

    db_node = DocumentNode(
        title=node.title,
        number=node.number,
        level=node.level,
        body=node.body,
        content_hash=generate_hash(node.body),
        version_id=version_id,
        parent_id=parent_id
    )

    db.add(db_node)
    db.commit()
    db.refresh(db_node)

    current_id = db_node.id

    db.close()

    for child in node.children:
        save_node(child, version_id, current_id)