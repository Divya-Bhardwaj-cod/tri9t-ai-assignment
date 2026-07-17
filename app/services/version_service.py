from app.database.database import SessionLocal
from app.models.document_node import DocumentNode


def compare_versions(version1_id, version2_id):

    db = SessionLocal()

    version1_nodes = (
        db.query(DocumentNode)
        .filter(DocumentNode.version_id == version1_id)
        .all()
    )

    version2_nodes = (
        db.query(DocumentNode)
        .filter(DocumentNode.version_id == version2_id)
        .all()
    )

    version1_map = {
        node.number: node
        for node in version1_nodes
    }

    version2_map = {
        node.number: node
        for node in version2_nodes
    }

    added = []
    removed = []
    modified = []
    unchanged = []

    all_numbers = set(version1_map.keys()) | set(version2_map.keys())

    for number in sorted(all_numbers):

        node1 = version1_map.get(number)
        node2 = version2_map.get(number)

        if node1 is None:

            added.append({
                "number": node2.number,
                "title": node2.title
            })

        elif node2 is None:

            removed.append({
                "number": node1.number,
                "title": node1.title
            })

        elif node1.content_hash == node2.content_hash:

            unchanged.append({
                "number": node1.number,
                "title": node1.title
            })

        else:

            modified.append({
                "number": node1.number,
                "title": node1.title
            })

    db.close()

    return {
        "added": added,
        "removed": removed,
        "modified": modified,
        "unchanged": unchanged
    }