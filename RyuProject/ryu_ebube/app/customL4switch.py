"""This is a custom version of the layer 3 switch for Ryu. I decided to go with
the reinvent the wheel. This application relies on OpenFlow 1.3 """
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.lib.packet import in_proto
from ryu.lib.packet import ipv4
from ryu.lib.packet import icmp
from ryu.lib.packet import tcp
from ryu.lib.packet import udp

class Layer4Switch(app_manager.RyuApp):
    #Part 1: give the OpenFlow version and initialize the class
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    def __init__(self, *args, **kwargs):
        super(Layer4Switch, self).__init__(*args, **kwargs)
        #this is the mac address table
        self.mac_to_port = {}

    #Part 2: Adding a table miss entry to switch
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        """handles the message of a given OpenFlow switch, the OpenFlow protocol used and
        the parser to parse the OpenFlow message"""
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        #adds the table miss entry
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    #Part 3: Adding in Layer 3 flows
    def add_flow(self, datapath, priority, match, actions, buffer_id=None):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        #send instructions to the switch
        instructions = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        if buffer_id: #if there is a valid buffer id
            mod = parser.OFPFlowMod(datapath=datapath, buffer_id=buffer_id,
                                    priority=priority, match=match,
                                    instructions=instructions)
        else:
            mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                                    match=match, instructions=instructions)
        datapath.send_msg(mod)

    #Part 4: add a Packet In message to receive packets
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        """Handles the message from a given OpenFlow switch, as well as the OpenFlow protocol
        used and a parser to parse OpenFlow messages/data"""
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # ** This updates the MAC address table **
        # get the received port number from packet_in message.
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data) #get Packet object
        eth = pkt.get_protocols(ethernet.ethernet)[0] #get ethernet header

        #if the ethernet packet protocol is LLDP (Link Layer Discovery Protocol)
        if eth.ethertype == ether_types.ETH_TYPE_LLDP:
            #ignore it
            return
        dst = eth.dst
        src = eth.src

        dpid = format(datapath.id, "d").zfill(16)
        self.mac_to_port.setdefault(dpid, {})

        #Log the information
        self.logger.info("packet in %s %s %s %s", dpid, src, dst, in_port)

        # learn a mac address to avoid FLOOD next time.
        self.mac_to_port[dpid][src] = in_port
        if dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]
        else:
            #makes a network broadcast if port not in MAC table
            out_port = ofproto.OFPP_FLOOD

        actions = [parser.OFPActionOutput(out_port)]

        if out_port != ofproto.OFPP_FLOOD:
            #This is where we do the Layer 3 forwarding:
            if eth.ethertype == ether_types.ETH_TYPE_IP:
                ip = pkt.get_protocol(ipv4.ipv4) #get IP header
                source_ip = ip.src
                destination_ip = ip.dst
                protocol = ip.proto

                # if ICMP Protocol
                if protocol == in_proto.IPPROTO_ICMP:
                    match = parser.OFPMatch(eth_type=ether_types.ETH_TYPE_IP,
                    ipv4_src=source_ip, ipv4_dst=destination_ip, ip_proto=protocol)

                #  if TCP Protocol
                elif protocol == in_proto.IPPROTO_TCP:
                    t = pkt.get_protocol(tcp.tcp)
                    match = parser.OFPMatch(eth_type=ether_types.ETH_TYPE_IP,
                    ipv4_src=source_ip, ipv4_dst=destination_ip, ip_proto=protocol,
                    tcp_src=t.src_port, tcp_dst=t.dst_port)

                #  If UDP Protocol
                elif protocol == in_proto.IPPROTO_UDP:
                    u = pkt.get_protocol(udp.udp)
                    match = parser.OFPMatch(eth_type=ether_types.ETH_TYPE_IP,
                    ipv4_src=source_ip, ipv4_dst=destination_ip, ip_proto=protocol,
                    udp_src=u.src_port, udp_dst=u.dst_port)

                """Verify the buffer id to see if it is valid (to prevent sending both
                the flow mod and packet out at the same time)"""
                if msg.buffer_id != ofproto.OFP_NO_BUFFER:
                    self.add_flow(datapath, 100, match, actions, msg.buffer_id)
                    return
                else:
                    self.add_flow(datapath, 1, match, actions)

        #managing the OpenFlow message data
        data = None
        #checking for valid buffer id or not
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data
        output = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                    in_port=in_port, actions=actions, data=data)
        #send Packet Out message to the switch
        datapath.send_msg(output)
