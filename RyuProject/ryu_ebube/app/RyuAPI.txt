This is some documentation on the API endpoints that you would use if you are making API calls from the client directly to the 
Ryu network controller. However, it is more recommended to make the API calls through the Flask web server instead and for the
Flask server to make the API calls to the Ryu controller on your behalf.

************************************************************************************************************************************
# API Custom Endpoints (directly to the controller)

# Keys: 
# {dpid} = dpid number of the switch
# {port} = port from an OpenFlow switch
# {queue_id} = queue ID of an OpenFlow switch queue
# {queue} = the queue number of an OpenFlow switch
# {meterID} = the meter ID of an OpenFlow switch meter table
# {groupID} = the group table ID of an OpenFlow switch
# {command} = the URI endpoint command to manage a flow/meter/group table

/info/switches = Get the DPIDs of all the connected OpenFlow switches

/info/desc/{dpid} = Get a general description of an OpenFlow switch

/info/flows/{dpid} = Gets the flow information from an OpenFlow switch

/info/aggregateflows/{dpid} = Get the aggregate/total flows from an OpenFlow switch

/info/flowtables/{dpid} = Get the stats from the flow tables of an OpenFlow switch

/info/flowtablefeatures/{dpid} = Get the flow table features of an OpenFlow switch

/info/portinfo/{dpid} = Get the stats of all the ports from an OpenFlow switch

/info/portinfo/{dpid}/{port} = Get the stats of a single port of an OpenFlow switch

/info/queueinfo/{dpid} = Get all the queue information of all the ports of an OpenFlow switch

/info/queueinfo/{dpid}/{port} = Get all the queue information of a single port of an OpenFlow switch

/info/queueinfo/{dpid}/{port}/{queue_id} = Get the queue information of a single port of an OpenFlow switch by their queue ID

/info/queueconfiguration/{dpid} = Get the configuration information about the queues of all the ports of an OpenFlow switch

/info/queueconfiguration/{dpid}/{port} = Get the configuration information about the queues of a specific port of an OpenFlow switch

/info/meterspecs/{dpid} = Get the meter table stats of an OpenFlow switch

/info/meterconfiguration/{dpid} = Get the table meter configuration from an Openflow switch

/info/meterconfiguration/{dpid}/{meterID} = Get the table meter configuration from a specific meter table of an Openflow switch

/info/meterinfo/{dpid} = This gets the information about the meter tables of an OpenFlow switch

/info/meterinfo/{dpid}/{meterID} = This gets the information about a specific meter table of an OpenFlow switch

/info/group/{dpid} = Gets information about all the group tables of an OpenFlow switch

/info/group/{dpid}/{groupID} = Gets information about a specific group table by the group ID of an OpenFlow switch

/info/groupdescription/{dpid} = Gets the description information about the group tables of an OpenFlow switch

/info/groupdescription/{dpid}/{groupID} = Gets the description information about a group table by the group ID of an OpenFlow switch

/info/portdescription/{dpid} = Gets the port behavior information from an OpenFlow switch

/info/currentrole/{dpid} = Get the current role of the SDN controller from the OpenFlow switch

/info/ryuflow/{command} = Adds, changes or deletes a flow from the flow table of an OpenFlow switch. The action depends on the {command} value
 - 'add' => adds a flow
 - 'change_all' => change all matching flow entries
 - 'change_strict' => change a flow that strictly matches the wildcards and priority given
 - 'delete_all' => Deletes all maching flows
 - 'delete_strict' => Deletes a flow that strictly matches the wildcars and the priority given

/info/flows/erase/{dpid} = Deletes ALL the flows in the flow table of an OpenFlow switch.

/info/meter/{command} = Adds, changes or deletes the meter entries on the meter table of an OpenFlow switch based on the {command} value
 - 'add' => Adds a meter entry
 - 'change' => change a meter entry
 - 'remove' => remove a meter entry

/info/group/{command} = Adds, changes or deletes the group table entries on the group table of an OpenFlow switch based on the {command} value
 - 'add' => Adds a group entry
 - 'change' => change a group entry
 - 'remove' => remove a group entry

/info/portbehavior/modify = Changes the behavior of a port on an OpenFlow switch

/info/sendexperimenter/{dpid} = Sends an experimenter message to the OpenFlow switch from the controller

/info/updaterole = Changes the role of the controller for an OpenFlow switch

************************************************************************************************************************************