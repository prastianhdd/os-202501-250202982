# Dockerfile
# Gunakan image python 
FROM python:3.14-alpine

# Set direktori kerja di dalam container
WORKDIR /app

# Salin semua file .py 
COPY *.py .

# Salin folder data
COPY data/ ./data/

# Jalankan aplikasi utama
CMD ["python", "main.py"]