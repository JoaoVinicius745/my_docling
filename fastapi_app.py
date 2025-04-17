from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import base64
from docling.datamodel.base import DocumentInput
from docling.document_converter import DocumentConverter

app = FastAPI()

@app.post("/docling/")
async def docling(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="No file was provided")

    file = files[0]
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    converter = DocumentConverter()
    document = DocumentInput(file.file.read())
    result = converter.convert(document)

    if result.document is not None:
        md_content = result.document.export_to_markdown()
        return JSONResponse(content={"output": md_content})
    else:
        raise HTTPException(status_code=500, detail="Failed to convert PDF to Markdown")

@app.get("/")
async def root():
    return {"message": "Welcome to the PDF to Markdown converter API"}
