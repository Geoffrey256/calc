# Use official Python image
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN mkdir /app/tmp

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]


# # Use an official Python base image
# FROM python:3.10-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set working directory in the container
# WORKDIR /app

# # Copy everything from local dir to container's /app dir
# COPY . /app

# # Install system dependencies and Python packages
# # RUN pip install --no-cache-dir streamlit requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt


# # Expose the default Streamlit port
# EXPOSE 8501

# # Run the app
# CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
