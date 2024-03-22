# Use official Python image as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port where Streamlit runs
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "user-interface.py"]

# Add a simple test
RUN echo "Running simple test..."
RUN python test.py
