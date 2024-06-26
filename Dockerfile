# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir morse_code
RUN pip install --no-cache-dir random2

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
