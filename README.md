# webfortune
This program allows the user to use a linux command line through a browser to receive fortunes, use a function called cowsay, and a cow that gives you a fortune(combining both functions).

# How to run with Docker

# Building your Program
To build your own version, you need to install docker. Then to create your own docker image, run the command `docker build -t <repository> .` where `<repository>` will be the name of your image..

# How to Run
To run your image, use the command `docker run -dp <port>:5000 <repository>` where `<port>` is the port used to reach the webserver in the browser, and `5000` is what the container is set to, and `repository` is the same name as when building your image.

# How to stop Running
To stop running the docker container, first use the command `docker ps`. Look for the image with the name of your docker container and copy its id. Then run the command `docker stop <id>.` to close the container. 

# How to run Locally

# Setting up an environment
To set up your own environment, use the following commands.

  1.) `python3 -m virtualenv env`
  2.) `source env/bin/activate`
  3.) `pip3 install -r requirements.txt`

# How to test
Before running, you should test it by running the command `pytest`.

# How to Run
To run the webserver, use the command `FLASK_APP=appserver.py flask run --host=0.0.0.0`. Then in a browser, enter as a URL `<your_currnet_ip_address>:5000`.
