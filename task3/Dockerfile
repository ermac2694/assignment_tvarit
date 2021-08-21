# getting the base image
FROM python:3.7

# setting up working directory
WORKDIR restAPIs

# copying all the files
COPY . .

# installing all the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# exposing the port to interact with the server
EXPOSE 5000

# running the server
CMD ["python3", "app.py"]