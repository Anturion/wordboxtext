FROM python:3.8-slim-buster
RUN apt-get update\
    && apt-get install gcc -y\ 
    && apt-get install g++ -y\
    && apt-get install apt-transport-https\
    && apt-get update\
    && apt-get install -y libodbc1\
    && apt update\
    && apt install unixodbc -y\
    && apt install curl -y\ 
    && apt-get install -y gnupg2\
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -\
    && curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list\
    && apt-get update\
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17\
    && apt-get install unixodbc-dev -y

# copy files to the /app folder in the container
COPY . /
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
