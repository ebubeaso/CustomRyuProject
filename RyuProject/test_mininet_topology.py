"""
This Python script makes the Mininet software defined network topology to test out the API routes with.
I made this script to automate building the virtual topology so that anyone testing out my API collection
for Flask and Ryu can just focus on using the API requests. Here is how the topology is setup:

    - 1 Open vSwitch OpenFlow switch (to keep the testing simple for the users of the API requests)
    - 3 virtual hosts => they are on the 10.0.0.0/8 network.
        - h1 => IP address: 10.0.0.1
        - h2 => IP address: 10.0.0.2
        - h3 => IP address: 10.0.0.3
    - 1 controller, the Ryu controller => the Ryu controller will run on localhost, since for testing the controller
    will be run on the same machine that the user is running the Flask web server and the APIs for simplicity. If you
    happen to run the Ryu SDN controller on a remote computer, then you can change the IP address
"""

#import the Mininet modules
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class TestTopo(Topo):
    """Builds the Mininet virtual topology"""
    def build(self):
        #make the switch
        s1 = self.addSwitch('s1')
        #make the hosts
        for h in range(3):
            host = self.addHost("h" + str(h+1))
            #make the links
            self.addLink(s1, host)

"""Runs the Mininet virtual topology"""
def runTopology():
    topos=TestTopo()
    # make the network controller
    c0 = RemoteController('c0', ip='127.0.0.1', port=6653)
    net = Mininet(topo=topos, controller=c0)
    net.start()
    """The reason why the script_for_mininet_hackathon is because the
    script has some group entries, meter entries and queues to add in so 
    that the API user can see what the queues, meters and group entries 
    look like when they do the GET request for them."""
    CLI(net, script="script_for_mininet_hackathon")
    CLI(net)
    net.stop()

if __name__ == "__main__":
    setLogLevel('info')
    runTopology()