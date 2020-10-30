python check_postgres.py

echo "Running migrations..."
alembic upgrade head

echo "Starting server..."

uvicorn --host 0.0.0.0 app.main:app