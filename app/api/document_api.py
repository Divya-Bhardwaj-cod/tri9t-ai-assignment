from fastapi import APIRouter, HTTPException, Body
from sqlalchemy import or_

from app.database.database import SessionLocal
from app.models.document_node import DocumentNode
from app.models.selection import Selection
from app.models.selection_node import SelectionNode

from app.services.version_service import compare_versions
from app.services.selection_service import create_selection

router = APIRouter()


@router.get("/sections")
def get_sections():

    db = SessionLocal()

    sections = (
        db.query(DocumentNode)
        .filter(DocumentNode.parent_id == None)
        .all()
    )

    db.close()

    return sections


@router.get("/nodes/{node_id}")
def get_node(node_id: int):

    db = SessionLocal()

    node = (
        db.query(DocumentNode)
        .filter(DocumentNode.id == node_id)
        .first()
    )

    if node is None:
        db.close()
        raise HTTPException(status_code=404, detail="Node not found")

    children = (
        db.query(DocumentNode)
        .filter(DocumentNode.parent_id == node_id)
        .all()
    )

    result = {
        "id": node.id,
        "number": node.number,
        "title": node.title,
        "level": node.level,
        "body": node.body,
        "content_hash": node.content_hash,
        "version_id": node.version_id,
        "parent_id": node.parent_id,
        "children": [
            {
                "id": child.id,
                "number": child.number,
                "title": child.title,
                "level": child.level
            }
            for child in children
        ]
    }

    db.close()

    return result


@router.get("/search")
def search_nodes(q: str):

    db = SessionLocal()

    results = (
        db.query(DocumentNode)
        .filter(
            or_(
                DocumentNode.title.ilike(f"%{q}%"),
                DocumentNode.body.ilike(f"%{q}%")
            )
        )
        .all()
    )

    db.close()

    return results


@router.get("/versions/{version1_id}/{version2_id}/diff")
def get_version_diff(version1_id: int, version2_id: int):

    return compare_versions(version1_id, version2_id)


@router.post("/selection")
def save_selection(data: dict = Body(...)):

    selection_id = create_selection(
        data["name"],
        data["version_id"],
        data["node_ids"]
    )

    return {
        "selection_id": selection_id
    }


@router.get("/selection/{selection_id}")
def get_selection(selection_id: int):

    db = SessionLocal()

    selection = (
        db.query(Selection)
        .filter(Selection.id == selection_id)
        .first()
    )

    if selection is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Selection not found"
        )

    mappings = (
        db.query(SelectionNode)
        .filter(SelectionNode.selection_id == selection_id)
        .all()
    )

    db.close()

    return {
        "id": selection.id,
        "name": selection.name,
        "version_id": selection.version_id,
        "node_ids": [
            mapping.node_id
            for mapping in mappings
        ]
    }