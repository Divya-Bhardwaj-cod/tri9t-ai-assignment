from app.database.database import SessionLocal
from app.models.document import Document
from app.models.document_version import DocumentVersion

from app.parser.heading_parser import parse_headings
from app.parser.tree_builder import build_tree
from app.services.database_service import save_node


def import_document(pdf_path):

    db = SessionLocal()

    # Check if the document already exists
    document = (
        db.query(Document)
        .filter(Document.name == "CT200 Manual")
        .first()
    )

    if document is None:
        document = Document(name="CT200 Manual")
        db.add(document)
        db.commit()
        db.refresh(document)

    # Find the latest version
    latest_version = (
        db.query(DocumentVersion)
        .filter(DocumentVersion.document_id == document.id)
        .order_by(DocumentVersion.version_number.desc())
        .first()
    )

    # Decide the next version number
    if latest_version:
        next_version = latest_version.version_number + 1
    else:
        next_version = 1

    # Create the new version
    version = DocumentVersion(
        document_id=document.id,
        version_number=next_version
    )

    db.add(version)
    db.commit()
    db.refresh(version)

    # Parse the PDF
    headings = parse_headings(pdf_path)
    # Build the hierarchy
    tree = build_tree(headings)

    db.close()

    # Save all nodes for this version
    for root in tree:
        save_node(root, version.id)

    print(f"Document Version {next_version} imported successfully!")


if __name__ == "__main__":
    import_document("data/ct200_manual.pdf")