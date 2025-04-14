-- SQLite initialization script for Railway deployment

-- Create the user_llm_configs table if it doesn't exist
CREATE TABLE IF NOT EXISTS user_llm_configs (
    id INTEGER PRIMARY KEY,
    provider_type TEXT NOT NULL,
    "key" TEXT NOT NULL,
    chat_endpoint TEXT,
    chat_api_key TEXT,
    chat_model_name TEXT,
    embedding_endpoint TEXT,
    embedding_api_key TEXT,
    embedding_model_name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert a default configuration if it doesn't exist
INSERT OR IGNORE INTO user_llm_configs (id, provider_type, "key", chat_endpoint, chat_api_key, chat_model_name, embedding_endpoint, embedding_api_key, embedding_model_name)
VALUES (1, 'default', 'default_key', 'https://api.example.com/chat', 'default_api_key', 'default_model', 'https://api.example.com/embed', 'default_embed_key', 'default_embed_model');