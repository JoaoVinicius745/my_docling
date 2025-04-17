# Whisper API in Docker Container

Whisper API built using FastAPI inside a Docker container.

## API Documentation

### POST /whisper/

This endpoint accepts a list of audio files, transcribes them using the Whisper model, and returns the transcripts in JSON format.

#### Request

*   **files**: A list of audio files to be transcribed.

#### Response

*   **results**: A list of dictionaries containing the filename and transcript for each uploaded file.

#### Example Response

```json
{
  "results": [
    {
      "filename": "audio1.mp3",
      "transcript": "This is the transcript of audio1.mp3"
    },
    {
      "filename": "audio2.wav",
      "transcript": "This is the transcript of audio2.wav"
    }
  ]
}
```

#### Example Usage with curl

```bash
curl -X 'POST' \
  'http://localhost:8003/whisper/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@audio1.mp3;type=audio/mpeg' \
  -F 'files=@audio2.wav;type=audio/wav'
```

## Dependencies

The project requires the following dependencies:

*   `fastapi`
*   `aiofiles`
*   `python-multipart`
*   `uvicorn`

These dependencies are listed in `requirements.txt`.

## Running the Application

1.  Build the Docker image using the provided `Dockerfile`.
2.  Run the Docker container using `docker-compose up`.
3.  Access the API documentation at `http://localhost:8000/docs`.

## Notes

*   The application uses the Whisper model for transcription, which is loaded onto the available GPU if one is present.
*   The `/` endpoint redirects to the API documentation.
