# Use the Alpine-based Python image
FROM python:3.12-alpine

# Expose port 5000
EXPOSE 5000/tcp

# Set the working directory
WORKDIR /app

# Install system dependencies required for scikit-learn and other packages
RUN apk add --no-cache \
    build-base \
    python3-dev \
    py3-pip \
    py3-setuptools \
    py3-wheel \
    gfortran \
    musl-dev \
    libffi-dev \
    lapack-dev \
    g++ \
    gcc \
    gfortran \
    openblas-dev \
    && rm -rf /var/cache/apk/*

# Copy the dependencies file
COPY requirements.txt .

# Install dependencies with --no-cache-dir to save space
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Set the default command
CMD [ "python", "./app.py" ]
