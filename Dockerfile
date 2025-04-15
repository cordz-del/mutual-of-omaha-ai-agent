FROM python:3.8-slim
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./backend /app/backend
CMD ["uvicorn", "backend.api:app", "--host", "0.0.0.0", "--port", "80"]
