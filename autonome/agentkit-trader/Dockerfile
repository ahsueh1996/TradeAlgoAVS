# normal build command: docker buildx build --no-cache --platform linux/amd64 --push -t akfhsueh/autonome-test-extended-agentkit .
# debugging use: docker build --no-cache --progress=plain . 2>&1 | tee build.log
FROM python:3.10

# Copy all file and directories to /app folder of the container
WORKDIR /app
COPY . .

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
RUN python main.py