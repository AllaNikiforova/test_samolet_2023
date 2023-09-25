FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uvicorn

COPY . .

RUN adduser --disabled-password myuser
USER myuser

CMD ["uvicorn", "ex240823:app", "--host", "0.0.0.0", "--port", "8000"]
