# PDF to Markdown Converter API

This API is built using FastAPI and converts PDF files to Markdown format using Docling.

## API Documentation

### POST /convert_pdf_to_md/

This endpoint accepts a PDF file, converts it to Markdown, and returns the result in JSON format.

#### Request

*   **files**: A PDF file to be converted.

#### Response

*   **output**: The converted Markdown content.

#### Example Usage with curl

```bash
curl -X 'POST' \
  'http://localhost:8002/docling/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@example.pdf;type=application/pdf'
```

## Dependencies

The project requires the following dependencies:

*   `fastapi`
*   `aiofiles`
*   `python-multipart`
*   `uvicorn`
*   `docling`

These dependencies are listed in `requirements.txt`.

## Running the Application

1.  Install the dependencies using `pip install -r requirements.txt`.
2.  Run the application using `uvicorn fastapi_app:app --reload`.
3.  Access the API documentation at `http://localhost:8000/docs`.
