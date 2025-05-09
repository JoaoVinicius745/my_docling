FROM python:3.10-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install git -y
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8000", "--timeout-keep-alive","300"]
