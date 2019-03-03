class Point:
    'Point class'

    #Contructor
    def __init__(self, name, x, y, directions_result, traffic_flow, max_flow):

        self.name = name
        self.x = x
        self.y = y
        self.directions_result = directions_result
        self.traffic_flow = traffic_flow
        self.max_flow = max_flow

    def getName(self):
        return self.name

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDirections_result(self):
        return self.directions_result

    def getTraffic_flow(self):
        return self.traffic_flow

    def getMax_flow(self):
        return self.max_flow
