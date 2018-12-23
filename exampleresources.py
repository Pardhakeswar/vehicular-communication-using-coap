import time

from coapthon import defines

from coapthon.resources.resource import Resource

__author__ = 'Giacomo Tanganelli'


##############direction class#################

class Direction(Resource):
    def __init__(self, name="DirectionResource", coap_server=None):
        super(Direction, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "Information about in which direction a vehicle is moving"
        self.resource_type = "rt1"
        self.content_type = "text/plain"
        self.interface_type = "if1"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.edit_resource(request)
        return self

    def render_POST(self, request):
        res = self.init_resource(request, Direction())
        return res

    def render_DELETE(self, request):
        return True

###########################Accidnet occurence ###############

class AccidentOccurence(Resource):
    def __init__(self, name="AccidentResource", coap_server=None):
        super(AccidentOccurence, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "Information about The Accident details"
        self.resource_type = "rt1"
        self.content_type = "text/plain"
        self.interface_type = "if1"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.edit_resource(request)
        return self

    def render_POST(self, request):
        res = self.init_resource(request, AccidentOccurence())
        return res

    def render_DELETE(self, request):
        return True


##############################Breaks apply #######################

class SuddenBreakes(Resource):
    def __init__(self, name="SuddenBreakesResource", coap_server=None):
        super(SuddenBreakes, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "Information about if any  vehicle has applied sudden breakes"
        self.resource_type = "rt1"
        self.content_type = "text/plain"
        self.interface_type = "if1"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.edit_resource(request)
        return self

    def render_POST(self, request):
        res = self.init_resource(request, SuddenBreakes())
        return res

    def render_DELETE(self, request):
        return True



####################################location resource##########################

class Location(Resource):
    def __init__(self, name="Location", coap_server=None):
        super(Location, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "Information about Location of vehicle"
        self.resource_type = "rt1"
        self.content_type = "text/plain"
        self.interface_type = "if1"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.edit_resource(request)
        return self

    def render_POST(self, request):
        res = self.init_resource(request, SuddenBreakes())
        return res

    def render_DELETE(self, request):
        return True


