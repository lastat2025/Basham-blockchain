# Minimal Python Dockerfile for Basham-blockchain node
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_ENV=production
CMD ["python", "node.py"]
