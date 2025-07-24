# Use official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y wget gnupg libglib2.0-0 libnss3 libgconf-2-4 libatk1.0-0 libatk-bridge2.0-0 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libasound2 libpangocairo-1.0-0 libgtk-3-0

# Set workdir
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY setup_playwright.py .
COPY src ./src

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Playwright and Chromium
RUN python setup_playwright.py

# Expose port
EXPOSE 7860

# Run Streamlit app
CMD ["streamlit", "run", "src/streamlit_app.py", "--server.port=7860", "--server.address=0.0.0.0"]
