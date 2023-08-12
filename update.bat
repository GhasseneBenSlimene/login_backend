REM This script builds and runs the new authenticate container using Docker Compose.

REM Build the new authenticate container
docker-compose build authenticate

REM Run the new authenticate container
docker-compose up -d authenticate