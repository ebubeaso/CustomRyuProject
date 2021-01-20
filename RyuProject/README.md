This is my custom version of the Ryu software defined network controller where
it makes use of the powerful Python web framework known as Flask. I like
making APIs and I like the idea of using APIs to manage network infrastructure
instead of having to manually go into the CLI of each network device. This
custom version of Ryu gets rid of nearly all the default Python apps that came
with this controller, except for the ones that are needed to run my custom
REST API functionality. I decided to customize Ryu's REST API feature since I
personally did not like how the original ofctl_rest was set up. Included here
are the dependencies needed to use both the Ryu software defined network 
controller and to use Flask without any problems. Software defined networking
is the future of computer networking as it makes computer networks more agile
and easier to manage programmatically, especially when there are a lot of 
network nodes to manage. My skills in Python, API development, my personal 
research in understanding Ryu, as well as my strong background in computer 
networking and Linux, I now have a customized version of Ryu. It is open source,
so it is free for me to customize and use to practice my computer networking,
DevOps, API development and infrastructure skills. It has helped me understand 
software defined networking as well.

Here are the apps to use (that I have made):
customL3switch -> Layer 3 switch application
customL4switch -> Layer 4 switch application
custom_ryu_API -> custom REST API application (does not need the other applications
to run)

The name of the Flask application: FlaskRyuServer

To start the REST API controller:
type in the CLI => "ryu-manager custom_ryu_API.py" (It runs on port 8100 but you can change that
by changing the port in the file wsgi.py, since this application uses WSGI.)

To run the Flask server:
type in the CLI => python3 FlaskRyuServer.py (It runs on port 9900 but you can 
change that to another port directly in the Flask web application.)

# Endpoint documentation:
 -> RyuFlaskEndpoints.txt or RyuFlaskEndpoints.md

# Note:
The Flask server is the recommended device to talk to the controller. The 
intention of this is for security reasons since the controller controls the 
network so it is imperative to limit what devices can directly access the 
controller. Thus, you make API calls to the client via Postman or another API
client, and then the Flask web application sends a request to the controller. 
The controller responds to the request and then gives it back to you to read.
