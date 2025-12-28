# Gunakan image Python 
FROM python:3.11.14-alpine3.23

# Paksa Python matikan buffering
ENV PYTHONUNBUFFERED=1

# Set folder kerja di dalam container
WORKDIR /app

# Salin file app.py ke dalam container
COPY app.py .

# Perintah untuk menjalankan aplikasi
CMD ["python", "app.py"]