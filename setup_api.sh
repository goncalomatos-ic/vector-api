python check_postgres.py

echo "Running migrations..."
alembic upgrade hea

echo "Starting server..."

uvicorn app.main:app