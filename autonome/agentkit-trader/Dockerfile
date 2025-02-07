# normal build command: docker buildx build --no-cache --platform linux/amd64 --push -t akfhsueh/autonome-test-extended-agentkit .
FROM python:3.10

# Copy all file and directories to /app folder of the container
WORKDIR /app
COPY . .

# Expose the port (documentation purposes)
EXPOSE 3000

# Environment installs
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-root
RUN poetry install

# Debugging purposes
# use: docker build --no-cache --progress=plain . 2>&1 | tee build.log
#RUN pip list    

# Use CMD instead of RUN to avoid the main.py from getting run during docker build.
CMD ["python", "main.py"]

# Deubbing: Run the main.py file to see what breaks
#RUN python main.py