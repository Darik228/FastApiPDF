from fastapi import FastAPI, UploadFile, File, HTTPException
from schemas import TextOutput, PDFInput
from services import parse_pdf
import base64

app = FastAPI()

@app.post("/parse-pdf-base64/", response_model=TextOutput)
async def parse_pdf_base64(pdf_input: PDFInput):
    try:
        pdf_content = base64.b64decode(pdf_input.base64_pdf)
        parsed_output = parse_pdf(pdf_content)
        return parsed_output
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error processing PDF from base64")

@app.post("/parse-pdf-file/", response_model=TextOutput)
async def parse_pdf_file(file: UploadFile = File(...)):
    try:
        pdf_content = await file.read()
        parsed_output = parse_pdf(pdf_content)
        return parsed_output
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error processing uploaded PDF file")
