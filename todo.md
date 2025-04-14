# Project TODO

## Railway Deployment Setup
- Create a Railway project and link your GitHub repository.
- Configure deployment using Docker Compose (e.g., `docker-compose up --build`).
- Set up environment variables from the existing .env file in the Railway dashboard.
- Add necessary plugins (e.g., PostgreSQL) if the project requires a database.
- Monitor logs and verify that both backend and frontend services start properly.

## Railway Config as Code
- Review the guide: [https://docs.railway.com/guides/config-as-code](https://docs.railway.com/guides/config-as-code)
- Understand how deployments are attempted, built, and run.
- Configure deployment controls to override defaults (e.g., rollback, service restart).
- Enable Auto Deploys to build and deploy on Git push.
- Set Regional Deployments for optimal performance across regions.
- Configure Scaling options for vertical auto-scaling and horizontal replicas.
- Set up Healthchecks to ensure deployments are healthy.
- Define monorepo structure if using multiple services in one repo.
- Schedule Cron Jobs for periodic tasks.
- Optimize usage by setting limits and auto-sleep for inactive services.

## Database Initialization for Railway Deployment
- Add database initialization script to create required tables before app startup
- Create a pre-start script to initialize the SQLite database
- Ensure the "user_llm_configs" table is created
- Add database migration commands to the Railway build or start process
- Consider using a persistent volume for SQLite database in Railway
- Update railway.toml to include database initialization in the build or start command

## Future Tasks
- Periodically update roocodelog.md with project progress.
- Review and adjust Dockerfiles and compose configurations as needed.
