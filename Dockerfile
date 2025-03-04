# Python image
FROM python:3.13.2-alpine3.21

# Work directory
WORKDIR /app

# Copy project files into the /app folder
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# FastAPI port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]



