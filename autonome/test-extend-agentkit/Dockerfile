FROM python:3.10

# Copy all file and directories to /app folder of the container
WORKDIR /app
COPY . .

# Expose the port (documentation purposes)
EXPOSE 3000

# Environment installs
RUN pip install poetry
RUN poetry install

# Use CMD instead of RUN to avoid the main.py from getting run during docker build.
CMD ["python", "main.py"]