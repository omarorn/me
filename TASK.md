# Railway Deployment Tasks

## Current Tasks (2025-04-14)

- [x] Create railway.toml configuration file
- [x] Set up app.py entry point for Railway detection
- [x] Create requirements.txt with dependencies
- [x] Configure environment variables in railway.toml
- [ ] Fix database initialization issue
  - [ ] Create and test a database initialization script (init_db.py) to ensure required tables, such as `user_llm_configs`, are created before the application starts.
  - [ ] Update the start command to run the initialization script. For example, modify the start command to:
    ```
    python init_db.py && python app.py
    ```
  - [ ] Consider options for persistent database storage:
    - **Pre-start Initialization:** Use a pre-start script (init_db.py) to create missing tables on startup.
    - **Persistent Volume:** Configure Railway to use a persistent volume for SQLite, pre-populated with an initialized database.
    - **Switch Database Engine:** Switch from SQLite to PostgreSQL using Railway's PostgreSQL plugin, and update the application code to migrate the schema to PostgreSQL.
    
## Database Initialization Options

1. **Pre-Start Script:**
   - Run a script (e.g., `init_db.py`) during container startup to initialize the SQLite database.
   - Update `railway.toml`'s `startCommand` to execute:
     ```
     python init_db.py && python app.py
     ```
     
2. **Persistent Volume:**
   - Configure Railway to mount a persistent volume for the SQLite database file.
   - Pre-populate the volume with an initialized database containing all required tables.
     
3. **Switch to PostgreSQL:**
   - Use Railway's built-in PostgreSQL plugin.
   - Update the application configuration to use PostgreSQL instead of SQLite.
   - Migrate the database schema using an ORM migration tool.

## Discovered During Work

- The application expects a table `user_llm_configs` that does not exist in the current SQLite database.
- The error is triggered when the application attempts to use the database before it is properly initialized.
- Updating the start command to run `init_db.py` first should resolve this issue.

## Next Steps

- Test the pre-start script locally to ensure database tables are created.
- Update the Railway deployment commands to include the database initialization step.
- Verify that the container starts without database errors.