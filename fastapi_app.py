from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from docling.document_converter import DocumentConverter
import tempfile
import os
from fastapi.concurrency import run_in_threadpool

app = FastAPI()

async def convert_file_to_markdown(file_path: str) -> str:
    """Converts a document to Markdown."""
    try:
        converter = DocumentConverter()
        return await run_in_threadpool(converter.convert, file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao converter o arquivo: {str(e)}")

@app.post("/docling/")
async def convert_to_markdown(file: UploadFile = File(...)) -> JSONResponse:
    """Handles document conversion to Markdown."""
    if not file.filename.endswith(('.docx', '.odt', '.pdf')):
        raise HTTPException(status_code=400, detail="Formato de arquivo não suportado")

    try:
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            contents = await file.read()
            tmp.write(contents)
            tmp_path = tmp.name

        try:
            markdown_text = await convert_file_to_markdown(tmp_path)
        finally:
            os.remove(tmp_path)

        return JSONResponse(content={"markdown": markdown_text})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar o arquivo: {str(e)}")
