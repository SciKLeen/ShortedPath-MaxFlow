class Point:
    'Point class'

    #Contructor
    def __init__(self, id, name, longitude, latitude, address):
        self.id = id
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.address = address

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getLongitude(self):
        return self.longitude

    def getLatitude(self):
        return self.latitude

    def getAddress(self):
        return self.address
