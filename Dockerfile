# Use the official Python image as a base
FROM python:3.13-slim

# Arguments for Supabase (do not expose secrets in Dockerfile)
ARG SUPABASE_KEY
ARG SUPABASE_URL

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install build dependencies for Python and Rust
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    curl \
    && curl https://sh.rustup.rs -sSf | sh -s -- -y \
    && rm -rf /var/lib/apt/lists/*

# Add Cargo to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Install Python dependencies (prefer binary wheels)
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8000 to the outside world
EXPOSE 8000

# Set environment variables securely (passed at runtime)
ENV SUPABASE_URL=$SUPABASE_URL
ENV SUPABASE_KEY=$SUPABASE_KEY

# Command to run the application
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
