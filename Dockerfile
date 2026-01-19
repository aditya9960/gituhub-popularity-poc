FROM python:3.11-slim

WORKDIR /app

# Copy files
COPY requirements.txt .
# install
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and env
COPY app app
COPY .env .env

#main cmd to execute - configure later
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
