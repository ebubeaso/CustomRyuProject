#! /usr/bin/env python

"""
This Flask web application is what is used to connect to the Ryu network controller so that the controller can only be
accessed from the Flask server. This is made for theoretical network security where you limit the access to the controller
to one device. The intention of this Flask web application is that the user will send the API calls to the Flask server, and
then the Flask server sends an API request to the controller and returns the data/information back to the user. This will use
Flask RESTful which was a personal choice for me. The Flask server will send the API requests by using the Python library known
as "requests". You can make requests to this server using an API client like Postman or by using Python Requests.
"""
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
import ast

#Get information of the Ryu controller
ryu_ip = input("Enter the IP address of the Ryu controller: ")
ryu_port = input("Enter the port number that the Ryu REST API is using: ")
#initialize the flask application
app = Flask(__name__)
api = Api(app)
app.secret_key = "EbubeAso"

@app.route('/')
def index():
    return jsonify("""This Flask web application is what is used to connect to the Ryu network controller so that the controller can only be
accessed from the Flask server.The intention of this Flask web application is that the user will send the API calls to the Flask server, and
then the Flask server sends an API request to the controller and returns the data/information back to the user.
Here are the different routes that you can do below.
Endpoints: See FlaskRyuEndpoints.md or FlaskRyuEndpoints.txt for all the endpoint information
""")

class Switches(Resource):
    def get(self):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/switches")
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Could not retrieve the switch data"), 500

class SwitchDescription(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/desc/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get description of the switch"), 500

class Flows(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/flows/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get flows from the switch"), 500
    def post(self, dpid):
        the_body = request.get_json()
        r = requests.post("http://"+ryu_ip+":"+ryu_port+"/info/flows/"+dpid, json=the_body)
        if r.status_code <= 201:
            return r.json()
        else:
            return jsonify("Could not get the flow info"), 500

class AggregateFlows(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/aggregateflows/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get aggregate flows from the switch"), 500
    def post(self, dpid):
        the_body = request.get_json()
        r = requests.post("http://"+ryu_ip+":"+ryu_port+"/info/aggregateflows/"+dpid, json=the_body)
        if r.status_code <= 201:
            return r.json()
        else:
            return jsonify("Could not get the aggregate flow info"), 500

class FlowTables(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/flowtables/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get flow table info from the switch"), 500

class FlowTableFeatures(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/flowtablefeatures/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get flow table features from the switch"), 500

class PortInfo(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/portinfo/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get the port information from the switch"), 500

class SpecificPortInfo(Resource):
    def get(self, dpid, port):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/portinfo/"+dpid+'/'+port)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get the port information from the switch"), 500

class QueueInfo(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/queueinfo/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get all the queue information from the switch"), 500

class QueueInfoByPort(Resource):
    def get(self, dpid, port):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/queueinfo/"+dpid+"/"+port)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get the queue information on port " + port + " of the switch"), 500

class QueueInfoByQueue(Resource):
    def get(self, dpid, port, queue_id):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/queueinfo/"+dpid+"/"+port+"/"+queue_id)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get the queue information from the queue ID " + queue_id + "on port" + port + " of the switch"), 500

class QueueConfiguration(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/queueconfiguration/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get all the queue configuration from the switch"), 500

class QueueConfigurationByPort(Resource):
    def get(self, dpid, port):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/queueconfiguration/"+dpid+"/"+port)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get all the queue configuration on port " + port + "from the switch"), 500

class MeterSpecs(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/meterspecs/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get all the meter specs from the switch"), 500

class MeterConfiguration(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/meterconfiguration/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get all the meter configuration info from the switch"), 500

class MeterConfigurationByID(Resource):
    def get(self, dpid, meterID):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/meterconfiguration/"+dpid+"/"+meterID)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Cannot get the meter configuration info from the switch"), 500

class MeterInfo(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/meterinfo/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Could not get the meter feature information from the switch"), 500

class MeterInfoByID(Resource):
    def get(self, dpid, meterID):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/meterinfo/"+dpid+"/"+meterID)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Could not get the meter feature information from the switch"), 500

class GroupStats(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/group/"+dpid+"/ALL")
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Could not get the group table information from the switch"), 500

class GroupStatsByID(Resource):
    def get(self, dpid, groupID):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/group/"+dpid+"/"+groupID)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Could not get the group table information from the switch"), 500

class GroupDescription(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/groupdescription/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Could not get the group table descriptions from the switch"), 500

class GroupDescriptionByID(Resource):
    def get(self, dpid, groupID):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/groupdescription/"+dpid+"/"+groupID)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Could not get the group table descriptions from the switch"), 500

class PortBehavior(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/portdescription/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Could not get info on the port behaviors of the switch"), 500

class CurrentRole(Resource):
    def get(self, dpid):
        r = requests.get("http://"+ryu_ip+":"+ryu_port+"/info/currentrole/"+dpid)
        if r.status_code == 200:
            return r.json()
        else:
            return jsonify("Could not get info on the Controller's role for this switch"), 500

class FlowEntry(Resource):
    def post(self):
        the_body = request.get_json()
        r = requests.post("http://"+ryu_ip+":"+ryu_port+"/info/ryuflow/add", json=the_body)
        if r.status_code <= 201:
            return jsonify("The flows were added successfully!")
        else:
            return jsonify("The request could not add a flow to the switch"), 500
    def put(self):
        the_body = request.get_json()
        r = requests.put("http://"+ryu_ip+":"+ryu_port+"/info/ryuflow/change_all", json=the_body)
        if r.status_code == 200:
            return jsonify("The flows were modified successfully!")
        else:
            return jsonify("The request could not modify the flow on the switch"), 500
    def delete(self):
        the_body = request.get_json()
        r = requests.delete("http://"+ryu_ip+":"+ryu_port+"/info/ryuflow/delete_all", json=the_body)
        if r.status_code == 200:
            return jsonify("The flows were deleted successfully!")
        else:
            return jsonify("The request could not delete the flow on the switch"), 500
class FlowEntryStrict(Resource):
    def put(self):
        the_body = request.get_json()
        r = requests.put("http://"+ryu_ip+":"+ryu_port+"/info/ryuflow/change_strict", json=the_body)
        if r.status_code == 200:
            return jsonify("The flows were changed successfully!")
        else:
            return jsonify("The request could not modify the strictly matching flow on the switch"), 500
    def delete(self):
        the_body = request.get_json()
        r = requests.delete("http://"+ryu_ip+":"+ryu_port+"/info/ryuflow/delete_strict", json=the_body)
        if r.status_code == 200:
            return jsonify("The flows were deleted successfully!")
        else:
            return jsonify("The request could not delete the strictly matching flow on the switch"), 500

class EraseFlows(Resource):
    def delete(self, dpid):
        r = requests.delete("http://"+ryu_ip+":"+ryu_port+"/info/flows/erase/"+dpid)
        if r.status_code == 200:
            return jsonify("All the flows were erased!")
        else:
            return jsonify("The request could not delete all the flows on the switch"), 500

class MeterEntry(Resource):
    def post(self):
        the_body = request.get_json()
        r = requests.post("http://"+ryu_ip+":"+ryu_port+"/info/meter/add", json=the_body)
        if r.status_code <= 201:
            return jsonify("The meter was added!")
        else:
            return jsonify("The request could not add the meter entry on the switch"), 500
    def put(self):
        the_body = request.get_json()
        r = requests.put("http://"+ryu_ip+":"+ryu_port+"/info/meter/change", json=the_body)
        if r.status_code == 200:
            return jsonify("The meter was changed!")
        else:
            return jsonify("The request could not change the meter entry on the switch"), 500
    def delete(self):
        the_body = request.get_json()
        r = requests.delete("http://"+ryu_ip+":"+ryu_port+"/info/meter/remove", json=the_body)
        if r.status_code == 200:
            return jsonify("The meter was deleted!")
        else:
            return jsonify("The request could not delete the meter entry on the switch"), 500

class GroupEntry(Resource):
    def post(self):
        the_body = request.get_json()
        r = requests.post("http://"+ryu_ip+":"+ryu_port+"/info/group/add", json=the_body)
        if r.status_code == 200:
            return jsonify("New group entry was added!")
        else:
            return jsonify("The request could not add the group table entry on the switch"), 500
    def put(self):
        the_body = request.get_json()
        r = requests.put("http://"+ryu_ip+":"+ryu_port+"/info/group/change", json=the_body)
        if r.status_code == 200:
            return jsonify("The group entry was modified!")
        else:
            return jsonify("The request could not change the group table entry on the switch"), 500
    def delete(self):
        the_body = request.get_json()
        r = requests.delete("http://"+ryu_ip+":"+ryu_port+"/info/group/remove", json=the_body)
        if r.status_code == 200:
            return jsonify("The group entry was deleted!")
        else:
            return jsonify("The request could not delete the group table entry on the switch"), 500

class ManagePortBehavior(Resource):
    def put(self):
        the_body = request.get_json()
        r = requests.put("http://"+ryu_ip+":"+ryu_port+"/info/portbehavior/modify", json=the_body)
        if r.status_code == 200:
            return jsonify("Port behavior was changed!")
        else:
            return jsonify("Could not change the port behavior on the switch"), 500

class SendExperimenter(Resource):
    def post(self, dpid):
        the_body = request.get_json()
        r = requests.post("http://"+ryu_ip+":"+ryu_port+"/info/sendexperimenter/"+dpid, json=the_body)
        if r.status_code == 200:
            return jsonify("Experimenter message sent successfuly!")
        else:
            return jsonify("Could not send an experimenter message to the switch"), 500

class UpdateRole(Resource):
    def put(self):
        the_body = request.get_json()
        r = requests.put("http://"+ryu_ip+":"+ryu_port+"/info/updaterole", json=the_body)
        if r.status_code == 200:
            return jsonify("The role updated successfully!")
        else:
            return jsonify("Could not change the role of the controller on the switch"), 500

api.add_resource(Switches, '/switches/all')
api.add_resource(SwitchDescription, '/switches/description/<string:dpid>')
api.add_resource(Flows, '/flows/<string:dpid>')
api.add_resource(AggregateFlows, '/aggregateflows/<string:dpid>')
api.add_resource(FlowTables, '/table/stats/<string:dpid>')
api.add_resource(FlowTableFeatures, '/table/features/<string:dpid>')
api.add_resource(PortInfo, '/portinfo/<string:dpid>')
api.add_resource(SpecificPortInfo, '/portinfo/<string:dpid>/<string:port>')
api.add_resource(QueueInfo, '/queue/info/<string:dpid>')
api.add_resource(QueueInfoByPort, '/queue/info/<string:dpid>/<string:port>')
api.add_resource(QueueInfoByQueue, '/queue/info/<string:dpid>/<string:port>/<string:queue_id>')
api.add_resource(QueueConfiguration, '/queue/config/<string:dpid>')
api.add_resource(QueueConfigurationByPort, '/queue/config/<string:dpid>/<string:port>')
api.add_resource(MeterSpecs, '/meter/specs/<string:dpid>')
api.add_resource(MeterConfiguration, '/meter/configuration/<string:dpid>')
api.add_resource(MeterConfigurationByID, '/meter/configuration/<string:dpid>/<string:meterID>')
api.add_resource(MeterInfo, '/meter/info/<string:dpid>')
api.add_resource(MeterInfoByID, '/meter/info/<string:dpid>/<string:meterID>')
api.add_resource(GroupStats, '/group/<string:dpid>')
api.add_resource(GroupStatsByID, '/group/<string:dpid>/<string:groupID>')
api.add_resource(GroupDescription, '/group/description/<string:dpid>')
api.add_resource(GroupDescriptionByID, '/group/description/<string:dpid>/<string:groupID>')
api.add_resource(PortBehavior, '/port/behavior/<string:dpid>')
api.add_resource(CurrentRole, '/role/current/<string:dpid>')
api.add_resource(FlowEntry, '/flow/entry')
api.add_resource(FlowEntryStrict, '/flow/strict')
api.add_resource(EraseFlows, '/flows/erase/<string:dpid>')
api.add_resource(MeterEntry, '/meter/entry')
api.add_resource(GroupEntry, '/group/entry')
api.add_resource(ManagePortBehavior, '/portbehavior/manage')
api.add_resource(SendExperimenter, '/experimenter/send/<string:dpid>')
api.add_resource(UpdateRole, '/role/update')

if __name__ == "__main__":
    app.run(port=9900, host='0.0.0.0')
