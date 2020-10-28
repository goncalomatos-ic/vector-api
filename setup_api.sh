echo "Running migrations..."
alembic upgrade hea

echo "Starting server..."
cd app
uvicorn main:app