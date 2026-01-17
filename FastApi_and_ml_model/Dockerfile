# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY Backend_api/ ./Backend_api/
COPY model/ ./model/
COPY schema/ ./schema/

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "Backend_api.app:app", "--host", "0.0.0.0", "--port", "8000"]
