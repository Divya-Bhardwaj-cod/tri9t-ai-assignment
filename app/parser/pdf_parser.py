import fitz

PDF_PATH = "data/ct200_manual.pdf"

doc = fitz.open(PDF_PATH)

print("=" * 60)
print("CT-200 PDF READER")
print("=" * 60)

print(f"Total Pages : {len(doc)}")

for page_number in range(len(doc)):

    page = doc.load_page(page_number)

    text = page.get_text()

    print("\n")
    print("=" * 60)
    print(f"PAGE {page_number + 1}")
    print("=" * 60)

    print(text)