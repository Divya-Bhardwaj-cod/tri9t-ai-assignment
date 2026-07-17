import fitz
import re

heading_pattern = re.compile(r'^(\d+(?:\.\d+)*)(?:\.)?\s+(.+)$')


def parse_headings(pdf_path):

    doc = fitz.open(pdf_path)

    headings = []

    for page in doc:
        lines = page.get_text().split("\n")

        for line in lines:

            line = line.strip()

            match = heading_pattern.match(line)

            if match:

                number = match.group(1)
                title = match.group(2)

                # Ignore numbered list items
                if ":" in title:
                    continue

                level = number.count(".") + 1

                headings.append({
                    "number": number,
                    "title": title,
                    "level": level
                })

    return headings