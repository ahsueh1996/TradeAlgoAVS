FROM python:3.10

# Copy all file and directories to /app folder of the container
WORKDIR /app
COPY . .

# Expose the port (documentation purposes)
EXPOSE 3000

# Environment installs
RUN pip install poetry
RUN poetry install
RUN pip install python-dotenv

# Debugging purposes
RUN pip list

# Use CMD instead of RUN to avoid the main.py from getting run during docker build.
#CMD ["python", "main.py"]

# Run the main.py file FOR "Compile" debug
RUN python main.py