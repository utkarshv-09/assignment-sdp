FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 AS backend

WORKDIR /app/backend

COPY ./ /app/backend

RUN pip install -r /app/backend/requirements.txt

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
