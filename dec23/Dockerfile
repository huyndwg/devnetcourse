FROM python:3.7-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 6969
CMD ["python3", "app.py"]