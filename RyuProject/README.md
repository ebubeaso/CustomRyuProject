This is my custom version of the Ryu software defined network controller where it makes use of the powerful Python web framework 
known as Flask to manage the network infrastructure through APIs. I like making custom APIs and I like the idea of using them to 
programmatically configure and manage devices and servers on a network instead of having to manually go into the CLI of each 
machine. This custom version of Ryu gets rid of nearly all the default Python apps that came with this controller, except for the 
ones that are needed to run my custom REST API application and ones that I plan on using in future topology designs. I decided to 
customize Ryu's REST API feature since I personally did not like how the original ofctl_rest was set up. However, I used that original 
application as a guide to craft a custom version to show my understanding of the Ryu software defined networking framework. I believe 
that software defined networking is the future of computer networking as it makes computer networks more agile and easier to manage 
programmatically, especially when there are a lot of network devices to manage. I intend for this project to showcase the power of APIs 
when they are used in managing devices on a network environment. My skills in Python, API development, my personal research in understanding 
Ryu, as well as my strong background in computer networking and Linux have all helped me in making a customized version of Ryu. 
It is open source, so it is free for me and others to personalize and use to practice using software defined networking, DevOps, API development and
IT infrastructure.

Here are the apps to use (that I have made):
- customL3switch -> Layer 3 switch application
- customL4switch -> Layer 4 switch application
- custom_ryu_API -> custom REST API application (does not need the other applications
to run)

- The name of the Flask application: FlaskRyuServer


The custom_ryu_API is the main application to focus on, as it sets up a REST API that will communicate with the Flask server
via APIs. The Flask server serves as the "middle-man", as the clients send in the API requests to the Flask server, and then 
the Flask server forwards that API request to the controller, receives a response from the controller and returns the response
to the client.


To start the REST API controller:
type in the CLI => "ryu-manager ryu_ebube/app/custom_ryu_API.py" (It runs on port 8100 but you can change that
by changing the port in the file wsgi.py, since this application uses WSGI.)

To run the Flask server:
type in the CLI => "python3 ryu_ebube/app/FlaskRyuServer.py" (It runs on port 9900 but you can 
change that to another port directly in the Flask web application.)

# Endpoint documentation:
 -> RyuFlaskEndpoints.txt or RyuFlaskEndpoints.md

# Note:
The Flask server is the recommended device to talk to the controller. The intention of this is for security reasons since 
the controller controls the network so it is imperative to limit what devices can directly access it. Thus, you make API 
calls to the Flask server via Postman or another API client, and then the Flask web application sends a request to the controller. 
The controller responds to the request and then gives it back to you to read.
