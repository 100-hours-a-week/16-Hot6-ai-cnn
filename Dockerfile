FROM python:3.10.12

WORKDIR /app

COPY models/desk_classify.h5 ./models/desk_classify.h5
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt
COPY app/ ./app/

ENV CNN_MODEL=/app/models/desk_classify.h5

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
