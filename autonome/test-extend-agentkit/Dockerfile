FROM python:3.10
		
WORKDIR /app
COPY main.py .

# Use this later when we have requirements file:
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Expose the port (documentation purposes)
EXPOSE 3000

# Environment installs
RUN pip install poetry
RUN poetry install

# Use CMD instead of RUN to avoid the main.py from getting run during docker build.
CMD ["python", "main.py"]