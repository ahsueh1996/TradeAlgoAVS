# normal build command: docker buildx build --no-cache --platform linux/amd64 --push -t akfhsueh/<GIVENAME HERE> .
# debugging use: docker build --no-cache --progress=plain . 2>&1 | tee build.log
FROM python:3.10

# Copy all file and directories to /app folder of the container
WORKDIR /app
COPY . .
RUN ["chmod", "+x", "/app/wealthsimple-core/wspy/chromedriver-linux64/chromedriver"]
RUN ["chmod", "+x", "/app/wealthsimple-core/wspy/chromedriver-mac-arm64/chromedriver"]
RUN ["chmod", "+x", "/app/wealthsimple-core/wspy/chromedriver-win64/chromedriver.exe"]
# HACK for linux ditribution
RUN apt-get update
RUN apt-get install -y wget gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils


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
CMD ["python", "main.py"]

# Deubbing: Run the main.py file to see what breaks
# You CANNOT do this without go and edit the .dockerignore to temp allow upload .env. 
#COPY ./.env /app/.env 
#RUN python main.py