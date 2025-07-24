FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y wget gnupg curl libnss3 libatk-bridge2.0-0 libxss1 libasound2 libx11-xcb1 libgtk-3-0 libgbm1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and its browser binaries
RUN pip install playwright
RUN playwright install --with-deps

# Copy the rest of the app
COPY . .

# Expose the port
EXPOSE 7860

# Launch Streamlit
CMD ["streamlit", "run", "src/streamlit_app.py", "--server.port=7860", "--server.address=0.0.0.0"]

