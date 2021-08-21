Install Docker befor following the below steps.

To run please follow the below steps:
1. Go to task 3 directory:<br>
    cd task3
2. Build the image:<br>
    docker build -t tvarit .
3. List the image:<br>
    docker images
4. Run the container:<br>
    docker run -d -p 5000:5000 --name tvarit tvarit
5. Check logs:<br>
    docker logs