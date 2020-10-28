python check_postgres.py

echo "Running migrations..."
alembic upgrade head

echo "Starting server..."

uvicorn app.main:app