# Use an official Python runtime as a base image
FROM python:3.11.2-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app
#update 
RUN pip install --upgrade pip
# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python3", "main.py"]
