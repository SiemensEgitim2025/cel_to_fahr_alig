# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .


# Install the required Python packages
RUN pip install flake8 pytest
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code to the working directory
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 8080

# Set the environment variable for Flask
# ENV FLASK_APP=main.py

# Run the Flask app when the container starts
CMD ["python", "main.py"]
