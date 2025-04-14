"""
Database initialization script for Railway deployment.
This script creates the necessary SQLite database tables before the application starts.
"""

import os
import sys
import sqlite3

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import SQLAlchemy models if available
try:
    from lpm_kernel.api.models.user_llm_config import UserLLMConfig
    from lpm_kernel.common.repository.database_session import get_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    
    # Use SQLAlchemy to create tables
    def init_db_sqlalchemy():
        print("Initializing database using SQLAlchemy...")
        engine = get_engine()
        
        # Create all tables defined in the models
        from sqlalchemy.ext.declarative import declarative_base
        Base = declarative_base()
        Base.metadata.create_all(engine)
        
        # Create a default UserLLMConfig if it doesn't exist
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Check if default config exists
        default_config = session.query(UserLLMConfig).filter_by(id=1).first()
        if not default_config:
            print("Creating default UserLLMConfig...")
            default_config = UserLLMConfig(
                id=1,
                name="Default",
                model="gpt-3.5-turbo",
                api_base="https://api.openai.com/v1",
                api_key="",
                is_default=True
            )
            session.add(default_config)
            session.commit()
        
        session.close()
        print("Database initialization completed successfully.")
        
except ImportError:
    # Fallback to direct SQLite if SQLAlchemy models can't be imported
    def init_db_sqlite():
        print("Initializing database using direct SQLite...")
        
        # Determine the database path - use the same path as the application
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lpm_kernel", "database.sqlite")
        
        # Create the database directory if it doesn't exist
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create the user_llm_configs table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_llm_configs (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            model TEXT NOT NULL,
            api_base TEXT NOT NULL,
            api_key TEXT,
            is_default BOOLEAN NOT NULL DEFAULT 0
        )
        ''')
        
        # Check if default config exists
        cursor.execute("SELECT COUNT(*) FROM user_llm_configs WHERE id = 1")
        if cursor.fetchone()[0] == 0:
            print("Creating default UserLLMConfig...")
            cursor.execute('''
            INSERT INTO user_llm_configs (id, name, model, api_base, api_key, is_default)
            VALUES (1, 'Default', 'gpt-3.5-turbo', 'https://api.openai.com/v1', '', 1)
            ''')
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Database initialization completed successfully.")

if __name__ == "__main__":
    try:
        init_db_sqlalchemy()
    except Exception as e:
        print(f"SQLAlchemy initialization failed: {e}")
        try:
            init_db_sqlite()
        except Exception as e:
            print(f"SQLite initialization failed: {e}")
            sys.exit(1)