# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Flask directly (for simplicity in this guide)
RUN pip install flask

# Copy your code into the container
COPY app.py .

# Run the app
CMD ["python", "app.py"]
