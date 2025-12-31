# Menggunakan Python versi Alpine
FROM python:3.11.14-alpine

# Paksa Python matikan buffering
ENV PYTHONUNBUFFERED=1

# Menentukan folder kerja di dalam container
WORKDIR /app

# Copy file main.py dari folder laptop ke dalam container
COPY app.py .

# Perintah yang dijalankan saat container nyala
CMD ["python", "app.py"]