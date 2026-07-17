from app.database.database import SessionLocal
from app.models.selection import Selection
from app.models.selection_node import SelectionNode


def create_selection(name, version_id, node_ids):

    db = SessionLocal()

    selection = Selection(
        name=name,
        version_id=version_id
    )

    db.add(selection)
    db.commit()
    db.refresh(selection)

    for node_id in node_ids:

        mapping = SelectionNode(
            selection_id=selection.id,
            node_id=node_id
        )

        db.add(mapping)

    db.commit()

    db.close()

    return selection.id