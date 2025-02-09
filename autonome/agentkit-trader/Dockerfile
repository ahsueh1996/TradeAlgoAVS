# normal build command: docker buildx build --no-cache --platform linux/amd64 --push -t akfhsueh/<GIVENAME HERE> .
# debugging use: docker build --no-cache --platform linux/amd64 --progress=plain . 2>&1 | tee build.log
#FROM python:3.10
FROM --platform=$TARGETPLATFORM ubuntu:22.04

# Set non-interactive mode to prevent prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install required dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3.10-venv \
    python3.10-distutils \
    python3-pip \
    wget \
    gnupg \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set python3.10 as the default python version
RUN ln -sf /usr/bin/python3.10 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

# Install Google Chrome
ARG TARGETARCH
RUN if [ "$TARGETARCH" = "amd64" ]; then \
        wget -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
        apt-get update && apt-get install -y /tmp/google-chrome.deb && \
        rm /tmp/google-chrome.deb; \
    else \
        apt-get update && apt-get install -y chromium-browser; \
    fi

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg2 \
    ca-certificates \
    libgconf-2-4 \
    libnss3 \
    libx11-xcb1 \
    libgbm-dev \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libxrandr2 \
    libgtk-3-0 \
    libnspr4 \
    libxtst6 \
    libxss1 \
    libgdk-pixbuf2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Verify installations
RUN python --version && google-chrome --version && pip --version


# Copy all file and directories to /app folder of the container
WORKDIR /app
COPY . .
RUN chmod +x /app/wealthsimple-core/wspy/chromedriver-linux64/chromedriver
RUN cp /app/wealthsimple-core/wspy/chromedriver-linux64/chromedriver /usr/bin/chromedriver

# Debugging purposes, do this quickly to see if the selenium works
RUN pip install selenium

# Set environment variables for headless Chrome
ENV DISPLAY=:99
ENV CHROME_BIN=/usr/bin/google-chrome
ENV CHROME_DRIVER=/usr/local/bin/chromedriver
ENV TZ=UTC
# Set display for headless Chrome to prevent crashes
RUN Xvfb :99 -screen 0 1280x1024x24 &

# Debugging purposes
RUN python /app/docker_test_selenium.py

# Debugging purposes: prints out the files in the container
#RUN ls -R . | awk '/:$/&&f{s=$0;f=0}/:$/&&!f{sub(/:$/,"");s=$0;f=1;next}NF&&f{ print s"/"$0 }'

# Expose the port (documentation purposes)
EXPOSE 3000

# Install poetry
RUN pip install poetry
# make sure not to create a virtual environment
RUN poetry config virtualenvs.create false && poetry install --no-root

# Environment installs.. we don't have the lock files so we need to install each package individually
WORKDIR /app/cdp-agentkit-core
RUN poetry lock
RUN poetry install
WORKDIR /app/wealthsimple-core
RUN poetry lock
RUN poetry install
WORKDIR /app/wealthsimple-langchain
RUN poetry lock
RUN poetry install
WORKDIR /app
RUN poetry lock
RUN poetry install

# Debugging purposes
#RUN pip list    

# Use CMD instead of RUN to avoid the main.py from getting run during docker build.
#CMD ["python", "main.py"]

# Deubbing: Run the main.py file to see what breaks
# You CANNOT do this without go and edit the .dockerignore to temp allow upload .env. 
COPY ./.env /app/.env 
RUN python main.py