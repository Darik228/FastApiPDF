from typing import List

from pydantic import BaseModel


class PDFInput(BaseModel):
    base64_pdf: str


class TextOutput(BaseModel):
    headings: List[str]
    paragraphs: List[str]
