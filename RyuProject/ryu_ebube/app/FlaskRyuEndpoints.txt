This documentation provides key information on the Flask API endpoints used when running the Flask and Ryu software defined network architecture. 
In addition, it will tell you the HTTP/HTTPS request methods that you will need to use for each endpoint to work properly. All of the information about 
the API endpoints are below. Make sure that you use this documentation as a guide when making API requests to the Flask server that communicates with 
the Ryu SDN controller for managing the software defined network.

*****************************************************************************************************************************************
# Keys: 
# {dpid} = dpid number of the switch. The dpid is short for "Datapath ID"
# {port} = port from an OpenFlow switch
# {queue_id} = queue ID of an OpenFlow switch queue
# {queue} = the queue number of an OpenFlow switch
# {meterID} = the meter ID of an OpenFlow switch meter table
# {groupID} = the group table ID of an OpenFlow switch

# Endpoints:
    '/switches/all'
    ==> Gets the DPIDs of all the OpenFlow switches connected to the controller. 
    (Request method: GET)

    '/switches/description/{dpid}' 
    ==> Gets a general description of an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/flows/{dpid}' 
    ==> Gets all the flow data of an OpenFlow switch by its DPID. It is also used to get the flows that match a filter specified in the body 
    of a POST request. 
    (Request method: GET or POST (filter flows))
    - Example of a filter written in the request body:
        => {"table_id":0, "priority": 1} (Filters flows in Table 0 that have a priority of 1)

    '/aggregateflows/{dpid}' 
    ==> Gets all the aggregate flow data of an OpenFlow switch by its DPID. It is also used to get the flows that match a filter specified in 
    the body of a POST request. 
    (Request method: GET or POST (filter flows))
    - Example of a filter written in the request body:
        => { "table_id":0, "out_port": 1, "match": {"in_port":3} } (Filters aggregate flows in Table 0 that come in port 3 and out to port 1)

    '/table/stats/{dpid}' 
    ==> Get the table stats of all the flow tables of an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/table/features/{dpid}' 
    ==> Gets all the flow table features of an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/portinfo/{dpid}' 
    ==> Gets the stats of all the ports of an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/portinfo/{dpid}/{port}' 
    ==> Gets the stats of a given port on an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/queue/info/{dpid}' 
    ==> Gets all the queue information from all the ports of an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/queue/info/{dpid}/{port}' 
    ==> Gets all the queue information from a given port of an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/queue/info/{dpid}/{port}/{queue_id}' 
    ==> Gets the queue information by the given queue ID on the specified port of an OpenFlow switch. The switch is specified by its DPID.  
    (Request method: GET)

    '/queue/config/{dpid}' 
    ==> Gets all the queue configuration from all the ports of an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/queue/config/{dpid}/{port}' 
    ==> Gets all the queue configuration from a given port of an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/meter/specs/{dpid}' 
    ==> Gets all the meter table specifications/features of an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/meter/configuration/{dpid}' 
    ==> Gets all the meter table configurations of an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/meter/configuration/{dpid}/{meterID}' 
    ==> Gets the meter table configurations by its meter ID of an OpenFlow switch. The switch is given by its DPID. 
    (Request method: GET)

    '/meter/info/{dpid}' 
    ==> Gets all the meter table stats/information of an OpenFlow switch given by its DPID. 
    (Request method: GET)

    '/meter/info/{dpid}/{meterID}' 
    ==> Gets the meter table stats/information by its meter ID of an OpenFlow switch. The switch is given by its DPID. 
    (Request method: GET)

    '/group/{dpid}' 
    ==> Gets all the group table information of an OpenFlow switch by its DPID. 
    (Request method: GET)

    '/group/{dpid}/{groupID}' 
    ==> Gets the group table information specified by group ID of an OpenFlow switch by its DPID.
    (Request method: GET)

    '/group/description/{dpid}' 
    ==> Gets all the group table descriptions of an OpenFlow switch given by its DPID. 
    (Request method: GET)

    '/group/description/dpid/{groupID}' 
    ==> Gets the group table description specified by the group ID of an OpenFlow switch given by its DPID.
    (Request method: GET)

    '/port/behavior/{dpid}' 
    ==> Gets all the port behavior information on an OpenFlow switch by its DPID.
    (Request method: GET)

    '/role/current/{dpid}' 
    ==> Get the current role of the controller for the OpenFlow switch by its DPID.
    (Request method: GET)

    '/flow/entry' 
    ==> Manage the flow entries of an OpenFlow switch. 
    (Request methods: 
        POST => Adds a new flow 
        PUT => Modifies all flows that match the filter given in the request body
        DELETE => Deletes all flows that match the filter given in the request body)
    - Example of a flow written in the request body:
        => {"dpid":1, "table_id":0, "priority":120, "match": {"eth_type":0x0800,"nw_src":"10.0.0.2", "nw_dst":"10.0.0.1"}, 
                "actions": [{"type":"OUTPUT", "port":1}] }

    '/flow/strict' 
    ==> Modifies or deletes flows that strictly match the filters and the flow priority given in the request body.
    (Request methods:
        PUT => modifies strictly matching flows
        DELETE => deletes strictly matching flows)
    - Example of a flow written in the request body:
        => {"dpid":1, "table_id":0, "priority":100, "match": {"eth_type":0x0806,"ar_spa":"10.0.0.0/8", 
                "ar_tpa":"10.0.0.0/8"}, "actions": [{"type": "OUTPUT", "port": 4294967291}] }
                ==> "type": port number 4294967291 is the flood port to flood the network

    '/flows/erase/{dpid}' 
    ==> Erases all the flows on an OpenFlow switch given by its DPID.
    (Request method: DELETE)

    '/meter/entry' 
    ==> Manages the meter table entries of an OpenFlow switch. 
    (Request methods: 
        POST => Adds a meter entry 
        PUT => changes a meter entry that matches the request body
        DELETE => deletes a meter entry that matches the request body)
    - Example of a meter entry written in the request body:
        => {"dpid":1, "flags": "KBPS", "meter_id":3, "bands": [{ "type": "DSCP_REMARK", "rate": 30000 }] }

    '/group/entry' 
    ==> Manages the group table entries of an OpenFlow switch. 
    (Request methods:
        POST => Adds a group table entry
        PUT => changes a group table entry that matches the request body
        DELETE => deletes a group table entry that matches the request body)
    - Example of a group entry written in the request body:
        => {"dpid":4, "type": "ALL", "group_id":2, "buckets": [{ "actions": ["type":"OUTPUT", "port":3] }] }

    '/portbehavior/manage' 
    ==> Modifies the port behavior of an OpenFlow switch.
    (Request method: PUT)

    '/experimenter/send/{dpid}'
    ==> Send an experimenter message to the switch
    (Request method: POST)

    '/role/update' 
    ==> updates the role of the controller for the OpenFlow switch
    (Request method: PUT)
    
*****************************************************************************************************************************************