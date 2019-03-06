class Edges:
    'Point class'

    # Contructor
    def __init__(self, id, street_name, _from, _to, weight, traffic_flow, max_flow):
        self.id = id
        self.street_name = street_name
        self._from = _from
        self._to = _to
        self.weight = weight
        self.traffic_flow = traffic_flow
        self.max_flow = max_flow


    def getId(self):
        return self.id


    def getName(self):
        return self.street_name


    def getFrom(self):
        return self._from

    def getTo(self):
        return self._to

    def getWeight(self):
        return self.weight

    def getTraffic_flow(self):
        return self.traffic_flow

    def getMax_flow(self):
        return self.max_flow
