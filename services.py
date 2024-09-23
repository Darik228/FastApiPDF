import io

import pdfplumber
from fastapi import HTTPException

from schemas import TextOutput


def parse_pdf(pdf_content: bytes) -> TextOutput:
    pdf_content = io.BytesIO(pdf_content)

    try:
        headings = []
        paragraphs = []

        with pdfplumber.open(pdf_content) as pdf:
            for page in pdf.pages:
                text = page.extract_text()

                if text:
                    lines = text.split("\n")
                    for line in lines:
                        if line.isupper():
                            headings.append(line)
                        else:
                            paragraphs.append(line)

        return TextOutput(headings=headings, paragraphs=paragraphs)

    except Exception as e:
        raise HTTPException(status_code=400, detail="Error processing PDF")