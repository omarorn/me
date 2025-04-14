FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git sqlite3 && apt-get clean

# Copy repository files
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create necessary directories
RUN mkdir -p /app/data /app/logs

# Initialize SQLite database (moved to container build)
RUN echo "CREATE TABLE IF NOT EXISTS user_llm_configs (id INTEGER PRIMARY KEY, provider_type TEXT NOT NULL DEFAULT \"openai\", key TEXT, chat_endpoint TEXT, chat_api_key TEXT, chat_model_name TEXT, embedding_endpoint TEXT, embedding_api_key TEXT, embedding_model_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);" | sqlite3 /app/data/lpm.db

# Set environment variables
ENV PORT=8000 \
    DB_TYPE=sqlite \
    DB_FILE=/app/data/lpm.db \
    BASE_DIR=/app \
    FLASK_ENV=production

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]